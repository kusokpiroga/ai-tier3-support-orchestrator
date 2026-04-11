# ai-tier3-support-orchestrator
Production-grade AI Incident Response Orchestrator. Automates Tier 3 diagnostics using multi-agent workflows, dual-RAG architecture (LightRAG + ELK), and complex DSL query generation. Designed to reduce MTTR in high-scale service environments by bridging the gap between raw logs and actionable insights.
<img width="1023" height="505" alt="image" src="https://github.com/user-attachments/assets/798a1db3-29f5-4296-aab6-68ee4bc303e1" />

<p align="center">
  <img src="https://img.shields.io/badge/n8n-Workflow_Automation-FF6600?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n" />
  <img src="https://img.shields.io/badge/OpenAI-Agentic_RAG-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres" />
</p>

<h1 align="center">AI Tier 3 Support Orchestrator</h1>

<p align="center">
  <b>Fair-cost AI support automation for SaaS hospitality. Replace expensive night shifts with an intelligent agent that solves L1/L3 issues 24/7.</b>
</p>

<p align="center">
  <img src="link_to_your_main_hero_gif.gif" alt="AI Support Orchestrator Workflow Preview" width="800">
  <br>
  <i>(Replace with a general GIF showing the n8n execution flow)</i>
</p>

## 📖 What is this?

The **AI Tier 3 Support Orchestrator** is an advanced workflow automation designed to act as a smart technical consultant. 

Instead of just "saving time," **this project is designed to save headcount.**

**The Problem:** A minority of restaurants operate late into the night (2:00 AM - 3:00 AM) or 24/7. They require round-the-clock technical support. When a waiter can't close a final order or calculate the till, they can't go home. Maintaining a human night-shift worker for these rare, but critical, emergencies often costs upwards of $100+ per shift, just to answer 3 or 4 calls. 

**The Solution:** Most of these late-night "emergencies" are actually simple L1 tasks (the equivalent of "unplug the cable and plug it back in") that can be easily resolved using database queries, standard logic, and system logs. This agent handles those tasks autonomously. For an entire night shift, the AI consumes at most $5 in API costs—and only if a complex issue actually occurs.

## ✨ Key Features

* **Zero-Headcount Night Shifts:** Fully automates after-hours L1 support for POS and hospitality SaaS environments, drastically reducing payroll waste.
* **Intelligent Consultant Architecture:** Rather than executing risky, direct operations on organizational data, the agent acts as an expert consultant—analyzing system logs and safely guiding the resolution process.
* **Lean Database Integration:** Bypasses the need for bloated microservices. Interacts with PostgreSQL directly and efficiently via n8n HTTP Request nodes.
* **State Machine Logic:** Utilizes Agentic RAG and branching logic to accurately diagnose issues, mimicking human troubleshooting steps.

---

## 🛠 How It Works

Here is a breakdown of the core architecture and logical routing:

### 1. The Supervisor Agent (Decision Making)
The agent acts as the brain, receiving the initial panic query (e.g., "I can't close the register!") and determining the appropriate troubleshooting path.
<p align="center">
  <img src="https://github.com/user-attachments/assets/e0c24536-a3c0-4488-ac12-1c099f8c023c" alt="Supervisor Agent Decision Tree" width="200">
</p>

### 2. Direct HTTP-to-Database Routing
Instead of spinning up external services, the workflow uses optimized HTTP nodes to fetch necessary operational data, keeping the architecture lean and failure points low.
<p align="center">
  <img src="https://github.com/user-attachments/assets/a36c90df-4d23-4661-8fb6-0c6ae833bed3" alt="HTTP Request Database Node" width="200">
  <br><br>
  <img src="https://github.com/user-attachments/assets/ee4d798b-129a-4bd0-ab6f-3082378eb49b" alt="HTTP Request Database Node Part 2" width="200">
</p>

### 3. Log Analysis & Resolution
The agent parses the retrieved logs, identifies the missing parameter or system error, and provides the exact "dummy-proof" steps to fix it.
<p align="center">
  <img src="https://github.com/user-attachments/assets/383c0a03-af26-4ed0-866a-a6b23c179c33" alt="Log parsing and output 1" width="200">
  <br><br>
  <img src="https://github.com/user-attachments/assets/3387fe95-3e0c-4c6f-bcaa-8f92257a4d8e" alt="Log parsing and output 2" width="200">
  <br><br>
  <img src="https://github.com/user-attachments/assets/caf4adbb-60a6-4092-8283-5ecd68121140" alt="Log parsing and output 3" width="200">
</p>
## 💻 Tech Stack

**Orchestration & Workflow:**
* **n8n** (State Machine logic, Webhooks, HTTP Requests)

**Custom Backend & API:**
* **Python 3**
* **FastAPI + Uvicorn** (High-performance asynchronous REST API)
* **ngrok** (Secure tunneling for microservice exposure)

**AI & Data Engine:**
* **LightRAG** (Graph-based Retrieval-Augmented Generation)
* **OpenAI API** (`gpt-4o-mini` for inference, `openai_embed` for vectorization)
* **PyMuPDF / fitz** (Automated document ingestion and parsing)

**Storage:**
* **Google Drive / Local Storage** (Graph mappings and KB data storage)
* **PostgreSQL** (Target database for logging and operational data)

