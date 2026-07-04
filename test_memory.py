from backend.memory import MemoryManager

memory = MemoryManager()

memory.add_user_message("Hello")

memory.add_ai_message("Hi!")

memory.add_user_message("Summarize this agreement.")

print(memory.get_history())