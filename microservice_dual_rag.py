# Install all required libraries for the microservice
!pip install -q pymupdf pyngrok fastapi uvicorn lightrag-hku nest_asyncio

# ============================================================================
# SECTION 1: PRODUCTION RUNTIME - SYSTEM DEPENDENCIES & CONFIGURATION
# ============================================================================

import os
import logging
import asyncio
import threading
import glob
import subprocess
import uvicorn
import nest_asyncio
import fitz  # PyMuPDF
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyngrok import ngrok
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from google.colab import drive

# --- System Environment Setup ---
nest_asyncio.apply()
drive.mount('/content/drive')

# --- Production Constants ---
# TODO: Replace with your actual keys when running in Colab, but NEVER commit real keys to GitHub.
OPENAI_KEY = "YOUR_OPENAI_API_KEY" 
NGROK_TOKEN = "YOUR_NGROK_TOKEN"

# Database paths
DIR_TAGS = "/content/drive/MyDrive/LightRAG_Tags_Services_Mapping"
DIR_KB = "/content/drive/MyDrive/LightRAG_Data"

os.environ["OPENAI_API_KEY"] = OPENAI_KEY

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AI_Microservice")

# ============================================================================
# DATABASE INITIALIZATION: DUAL LIGHTRAG INSTANCES
# ============================================================================

logger.info("Initializing Databases...")
rag_tags = LightRAG(working_dir=DIR_TAGS, llm_model_func=gpt_4o_mini_complete, embedding_func=openai_embed)
rag_kb = LightRAG(working_dir=DIR_KB, llm_model_func=gpt_4o_mini_complete, embedding_func=openai_embed)
logger.info("✅ Dual RAG Instances Ready.")

# ============================================================================
# REST API LAYER: FASTAPI MODELS & ENDPOINTS
# ============================================================================

app = FastAPI(title="AI Support Microservice")

# Strict schema: expecting only {"query": "text"}
class QueryRequest(BaseModel):
    query: str

@app.post("/get_tags")
async def endpoint_get_tags(request: QueryRequest):
    """Endpoint 1: Retrieve service tags for downstream routing"""
    try:
        await rag_tags.initialize_storages()
        response = await rag_tags.aquery(request.query, param=QueryParam(mode="mix"))
        return {"status": "success", "data": str(response)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask_kb")
async def endpoint_ask_kb(request: QueryRequest):
    """Endpoint 2: Retrieve answers from the Knowledge Base"""
    try:
        await rag_kb.initialize_storages()
        response = await rag_kb.aquery(request.query, param=QueryParam(mode="mix"))
        return {"status": "success", "data": str(response)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "online", "mode": "dual-rag"}

# ============================================================================
# INFRASTRUCTURE: LAUNCH SERVER & NGROK
# ============================================================================

def start_background_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="error")
    server = uvicorn.Server(config)
    server.run()

# Force cleanup of ports and old tunnels (to prevent Colab hangs)
subprocess.run(["pkill", "-f", "ngrok"])
subprocess.run(["fuser", "-k", "8000/tcp"])

ngrok.set_auth_token(NGROK_TOKEN)
public_url = ngrok.connect(8000).public_url

print("\n" + "🔥"*30)
print(f"🚀 SERVER IS LIVE AND RUNNING!")
print(f"🔗 Tags URL:    {public_url}/get_tags")
print(f"🔗 KB URL:      {public_url}/ask_kb")
print("🔥"*30 + "\n")

# Launch in a background thread
threading.Thread(target=start_background_server, daemon=True).start()

# ============================================================================
# 🛠️ UTILITY: DATA INGESTION (RUN ONLY FOR DATABASE UPDATES) 🛠️
# ============================================================================

async def update_database(rag_instance: LightRAG, folder_path: str):
    """Function to load PDF and TXT files into the selected database."""
    await rag_instance.initialize_storages()
    files = glob.glob(os.path.join(folder_path, '**', '*.pdf'), recursive=True) + \
            glob.glob(os.path.join(folder_path, '**', '*.txt'), recursive=True)

    for f_path in files:
        try:
            if f_path.endswith('.pdf'):
                doc = fitz.open(f_path)
                content = "".join([page.get_text() for page in doc])
            else:
                with open(f_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            if content.strip():
                await rag_instance.ainsert(content)
                print(f"✅ Successfully loaded: {os.path.basename(f_path)}")
        except Exception as e:
            print(f"❌ Error loading {f_path}: {e}")
