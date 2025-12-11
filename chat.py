from prompt_toolkit import prompt
from embed import ask_model
from memory import add_memory, search

def build_prompt(user_input):
    memories = search(user_input, n_results=3)
    context = "\n".join([f"- {m}" for m in memories])
    return f"""\nТи дружній локальний ШІ. Ось релевантні згадки з історії розмов:
{context}

Запит користувача:
{user_input}
"""


def main():
    print("=== Local AI Chat (Ollama) ===")
    print("Модель: llama3.1 (8B/13B/70B – залежно що завантажиш)")
    print("Введи 'exit' щоб вийти.\n")

    while True:
        user_msg = prompt("> ")

        if user_msg.lower() in ("exit", "quit"):
            break

        add_memory(user_msg)

        full_prompt = build_prompt(user_msg)
        print("AI:", end=" ", flush=True)

        for piece in ask_model(full_prompt):
            print(piece, end="", flush=True)

        print("\n")

if __name__ == "__main__":
    main()
