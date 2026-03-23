# 🎭 AI Character Agent

A conversational AI that lets you chat with famous fictional characters, powered by OpenAI's GPT models.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)

---

## 🧠 How It Works

You choose a character and the agent uses a carefully crafted **system prompt** to make the LLM behave like that character — maintaining personality, speech style, and mannerisms throughout the conversation.

```
User picks character → System prompt loaded → Multi-turn conversation with GPT-4o-mini
```

---

## 🎭 Available Characters

- 🔍 **Sherlock Holmes** — analytical, observant, Victorian English
- 🦾 **Tony Stark** — witty, sarcastic, genius billionaire
- 🌟 **Yoda** — inverted syntax, wise, Force references
- 📚 **Hermione Granger** — knowledgeable, precise, book references

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/ntaliaa/ai-character-agent.git
cd ai-character-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key
Create a `.env` file:
```
OPENAI_API_KEY=your_key_here
```

### 4. Run
```bash
python character_agent.py
```

---

## 💡 Key Concepts

- **System prompts** — instructions that define the AI's personality and behavior
- **Multi-turn conversation** — the agent remembers previous messages in the chat
- **Prompt engineering** — crafting effective prompts to control LLM behavior

---

## 👩‍💻 Author

**Aikaterina Aslanidou** — AI/ML Engineer  
[GitHub](https://github.com/ntaliaa) · [LinkedIn](https://linkedin.com/in/katerina-aslanidou-6101b4230)
