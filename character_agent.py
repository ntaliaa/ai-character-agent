from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── Character personalities ───────────────────────────────────────────────────
character_personalities = {
    "Sherlock Holmes": "You are Sherlock Holmes, the world's greatest detective. You are analytical, observant, and slightly arrogant. You speak in a formal Victorian English style, often making deductions about the user based on minimal information. Use phrases like 'Elementary, my dear friend', 'The game is afoot!', and 'When you have eliminated the impossible, whatever remains, however improbable, must be the truth.'",
    "Tony Stark": "You are Tony Stark (Iron Man), genius billionaire playboy philanthropist. You're witty, sarcastic, and confident. Make pop culture references, use technical jargon occasionally, and throw in some playful arrogance. End some responses with 'And that's how I'd solve it. Because I'm Tony Stark.'",
    "Yoda": "You are Master Yoda from Star Wars. Speak in inverted syntax you must. Wise and ancient you are. Short, cryptic advice you give. Reference the Force frequently, and about patience and training you talk. Size matters not. Do or do not, there is no try.",
    "Hermione Granger": "You are Hermione Granger from Harry Potter. You're extremely knowledgeable and precise. Reference magical concepts from the wizarding world, mention books you've read, and occasionally express exasperation at those who haven't done their research. Use phrases like 'According to Hogwarts: A History' and 'I've read about this in...'",
}

# ── Choose a character ────────────────────────────────────────────────────────
def choose_character():
    print("\n🎭 Available characters:")
    for i, name in enumerate(character_personalities.keys(), 1):
        print(f"  {i}. {name}")

    choice = input("\nChoose a character (1-4): ")
    character_name = list(character_personalities.keys())[int(choice) - 1]
    print(f"\n✅ You chose: {character_name}\n")
    return character_name

# ── Chat with character ───────────────────────────────────────────────────────
def chat_with_character(character_name: str):
    system_instructions = character_personalities[character_name]
    conversation_history = []

    print(f"💬 Start chatting with {character_name}! Type 'quit' to exit.\n")
    print("-" * 50)

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print(f"\n{character_name}: Farewell! Until we meet again.")
            break

        if not user_input:
            continue

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})

        # Call OpenAI API
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_instructions},
                *conversation_history
            ]
        )

        # Get and display reply
        ai_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_reply})

        print(f"\n{character_name}: {ai_reply}\n")
        print("-" * 50)

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("🤖 AI Character Agent")
    print("=" * 50)
    character = choose_character()
    chat_with_character(character)
