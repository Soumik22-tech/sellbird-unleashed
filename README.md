# Sellbird — Open-Source AI Outreach (Custom / OpenAI-Compatible Edition)

> **Community Fork & Extended Edition:** This repository is an open-source fork of [ethanplusai/sellbird](https://github.com/ethanplusai/sellbird) licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.  
> It extends original Sellbird functionality by unlocking **Custom OpenAI-Compatible APIs (Groq, Google Gemini / Antigravity, NVIDIA NIM, and self-hosted vLLM/Ollama)** without requiring an active Claude Pro or ChatGPT Codex plan.

---

## 🌟 What is New in this Edition?

Original Sellbird only allowed headless execution via official Claude Code or OpenAI Codex CLIs. This fork introduces **Direct API Brain Integrations**:

- ⚡ **Groq Support:** Superfast cold email drafting using models like `llama-3.3-70b-versatile` (free tier available).
- 🧠 **Google Gemini Support:** Direct integration with Google AI Studio API (`gemini-2.0-flash`).
- 🚀 **NVIDIA NIM Support:** Fast enterprise-grade inference (`meta/llama-3.3-70b-instruct`).
- 🔌 **Generic OpenAI-Compatible Endpoints:** Connect local vLLM, Ollama, DeepSeek, or any custom API gateway.
- 💻 **Easy Self-Hosting:** Designed for clean, friction-free deployment on any Linux VPS or local workstation.

---

## 🚀 Quick Start (Local & VPS)

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/Soumik22-tech/sellbird-openai-compatible-api-version.git sellbird
cd sellbird

# Create and activate Python virtual environment (Python 3.11+)
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies in editable mode
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 2. Configure Your API Key & Provider

Copy the template environment file:
```bash
cp .env.example .env
```

Open `.env` and fill in your desired API Key:

```env
# Groq Example:
GROQ_API_KEY=gsk_your_key_here

# Or Google Gemini Example:
# GEMINI_API_KEY=AIzaSy_your_key_here

# Or NVIDIA NIM Example:
# NVIDIA_API_KEY=nvapi_your_key_here
```

In `sellbird.yaml`, set your provider under the `brain:` section:
```yaml
brain:
  provider: "groq"                      # Options: groq | gemini | nvidia | custom | claude | codex
  model: "llama-3.3-70b-versatile"
```

### 3. Launch Dashboard & Worker

```bash
# Terminal 1: Launch Web Dashboard
sellbird dashboard

# Terminal 2: Start Outreach Loop
sellbird run
```

Access the dashboard at `http://127.0.0.1:5555`.

---

## ⚖️ License & Attribution

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)** in compliance with the upstream project license.

- **Original Project:** [Sellbird (formerly Harvey)](https://github.com/ethanplusai/sellbird)
- **Original Copyright:** (C) 2026 Ethan Rogers and the Sellbird contributors.
- **Modifications & Extensions:** Custom API Brain engine, OpenAI-compatible transport layer, and provider adapters developed by [Soumik22-tech](https://github.com/Soumik22-tech).
- Full legal terms and permissions can be inspected in the [LICENSE](LICENSE) and [NOTICE](NOTICE) files.
