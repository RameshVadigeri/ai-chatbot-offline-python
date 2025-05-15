import tkinter as tk
from tkinter import scrolledtext

# Define some basic Q&A logic
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm Ramesh's chatbot assistant!"
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm still learning. Can you ask something else?"

# Function to send message
def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(tk.END, f"You: {user_msg}\n")
    bot_response = get_response(user_msg)
    chat_window.insert(tk.END, f"Bot: {bot_response}\n\n")
    user_input.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("AI Chatbot (Offline)")
window.geometry("400x500")

chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD)
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat_window.config(state='normal')

user_input = tk.Entry(window, font=("Arial", 14))
user_input.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()
