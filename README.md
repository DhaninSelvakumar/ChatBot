# 🤖 TinyLlama Local Chatbot

A lightweight **local chatbot application** built with **TinyLlama (1.1B)**, **FastAPI**, and **Streamlit**.  
This project lets you run a decoder-only LLM (instruction-tuned) **entirely on your own machine** with GPU quantization (4-bit using bitsandbytes).  

### ✨ Features
- 🧠 **TinyLlama-1.1B-Chat** model for fast, laptop-friendly inference  
- ⚡ **GPU acceleration with CUDA** (4-bit quantization via bitsandbytes to save VRAM)  
- 🌐 **FastAPI backend** serving a `/generate` endpoint for text generation  
- 💬 **Streamlit frontend** providing a simple chat UI  
- ⌨️ **Typing effect streaming** in UI (like ChatGPT)  
- 🧹 **Automatic input clearing** after sending messages  
- 🔄 Maintains **chat history** across conversation turns  

### 🛠️ Tech Stack
- [PyTorch](https://pytorch.org/) (CUDA-enabled)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes) (for 4-bit quantization)
- [FastAPI](https://fastapi.tiangolo.com/) (backend API)
- [Streamlit](https://streamlit.io/) (frontend chat interface)

### 🚀 How It Works
1. **Backend (FastAPI + TinyLlama)**  
   - Loads `TinyLlama/TinyLlama-1.1B-Chat-v1.0` with 4-bit quantization on GPU.  
   - Exposes `/generate` API endpoint for text generation.  

2. **Frontend (Streamlit)**  
   - Provides a chat interface that sends user input to the FastAPI backend.  
   - Displays responses with a **typing animation**.  
   - Maintains chat history between turns.  

### ▶️ Running the Project

**Start the backend (FastAPI):**
```bash
uvicorn decoder_api:app --host 0.0.0.0 --port 8000 --reload
