import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input):
    # Basic rule-based responses
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm doing great, thanks for asking!",
        "what is your name": "I'm your offline AI chatbot.",
        "bye": "Goodbye! Have a nice day!",
        "thank you": "You're welcome!",
        "thanks": "No problem!"
    }
    user_input_lower = user_input.lower()

    for key in responses:
        if key in user_input_lower:
            return responses[key]

    return "Sorry, I don't understand that. Can you try asking something else?"

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Offline AI Chatbot")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', width=60, height=20, wrap='word')
        self.chat_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=10)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            self._append_text(f"You: {user_input}\n")
            response = chatbot_response(user_input)
            self._append_text(f"Bot: {response}\n")
            self.entry.delete(0, tk.END)

    def _append_text(self, text):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, text)
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
