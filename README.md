# ai-tier3-support-orchestrator
Production-grade AI Incident Response Orchestrator. Automates Tier 3 diagnostics using multi-agent workflows, dual-RAG architecture (LightRAG + ELK), and complex DSL query generation. Designed to reduce MTTR in high-scale service environments by bridging the gap between raw logs and actionable insights.
<img width="1023" height="505" alt="image" src="https://github.com/user-attachments/assets/798a1db3-29f5-4296-aab6-68ee4bc303e1" />
![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/1cc4feb5-4dad-48e1-8adc-978a7323c974)
1
![ezgif com-video-to-gif-converter (7)](https://github.com/user-attachments/assets/25b21df9-db78-46da-a08c-c602aff2de24)
2
![ezgif com-video-to-gif-converter (6)](https://github.com/user-attachments/assets/1940f64b-f2f5-4aae-a258-40db5ebdd400)
3
![ezgif com-video-to-gif-converter (5)](https://github.com/user-attachments/assets/871e7abd-ed1a-4819-8c47-242f954e1db6)
4
![ezgif com-video-to-gif-converter (4)](https://github.com/user-attachments/assets/54b36d28-5089-4fec-9090-78170cd09cd1)
5
![ezgif com-video-to-gif-converter (3)](https://github.com/user-attachments/assets/e763198a-f653-4fad-b37c-56a84b002b1f)
6
![ezgif com-video-to-gif-converter (2)](https://github.com/user-attachments/assets/3ca8eaac-ad22-40be-a9dd-f66c72646085)
7
![ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/2e1f7ed7-9f6f-4adb-84c8-16970c60ab89)


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

### 1. The Supervisor Agent (Decision Making via n8n)
The n8n orchestrator acts as the central nervous system. It receives the initial panic query from the user, processes the state machine logic, and determines which specialized tool or microservice needs to be called to resolve the issue.

### 2. Custom AI Microservice (FastAPI + LightRAG)
Instead of overloading n8n with heavy data processing, HTTP Request nodes securely route complex RAG queries to a custom-built Python microservice. 
* **Dual RAG Instances:** The FastAPI backend runs two parallel `LightRAG` instances—one strictly for mapping service tags (routing) and one for deep Knowledge Base retrieval.
* **Seamless API:** n8n communicates with this microservice via optimized `/get_tags` and `/ask_kb` REST endpoints.

### 3. Data Ingestion & Resolution
The microservice autonomously handles data ingestion (parsing PDFs via `PyMuPDF` and text files), builds the relationship graphs, and feeds the precise, context-rich answers back to n8n to guide the L1/L3 troubleshooting process.

---

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

## 🚀 Getting Started

*(Add brief instructions here on how to import the `.json` workflow file into their own n8n instance and set up credentials).*

1. Clone this repository.
2. Import the `workflow.json` into your n8n workspace.
3. Configure your OpenAI API keys and PostgreSQL HTTP credentials.
4. Activate the webhook and test your first late-night support scenario!

## 🤝 Let's Connect

