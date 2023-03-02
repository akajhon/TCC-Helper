from chatbot import ChatBot
import argparse
import tkinter as tk

myChatBot = ChatBot()

parser = argparse.ArgumentParser(description='TCC-Helper: Um Chatbot para te ajudar com seu TCC.')
parser.add_argument('-t', '--train', help='Modo de Treinamento do Chatbot.', required=False, action='store_true')
parser.add_argument('-l', '--load', help='Carregar o modelo e executar a GUI.', required=False, action='store_true')

args = parser.parse_args()

if args.train:
    #criar o modelo
    myChatBot.createModel()
elif args.load:
    #apenas carregar um modelo pronto
    myChatBot.loadModel()
    #criar a GUI
    def get_response():
        user_input = input_box.get()
        response, intencao = myChatBot.chatbot_response(user_input)
        insert_user_message(user_input)
        insert_bot_message(response)
        input_box.delete(0, tk.END)
        if intencao[0]['intent'] == 'despedida':
            insert_bot_message(response)
            root.destroy()

    root = tk.Tk()
    root.title("TCC-Helper")
    root.configure(bg="white")

    messages_frame = tk.Frame(root, bg="white", bd=2, relief=tk.SUNKEN)
    messages_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10, expand=True)

    messages = tk.Text(messages_frame, height=20, width=60, bg="white", font=("Helvetica", 12), wrap=tk.WORD)
    messages.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)

    input_frame = tk.Frame(root, bg="white")
    input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    input_box = tk.Entry(input_frame, width=60, font=("Helvetica", 12))
    input_box.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    button = tk.Button(input_frame, text="Send", font=("Helvetica", 12), bg="#7289DA", fg="white", command=get_response)
    button.pack(side=tk.RIGHT, padx=10, pady=10)

    messages.tag_configure("bot", foreground="#7289DA", font=("Helvetica", 12, "bold"))
    messages.tag_configure("user", foreground="black")

    def insert_message(tag, text):
        messages.insert(tk.END, text + "\n\n", tag)
        messages.see(tk.END)

    def insert_user_message(text):
        insert_message("user", "Você: " + text)

    def insert_bot_message(response):
        insert_message("bot", "[+] TCC-Helper: " + response)

    width = messages_frame.winfo_reqwidth() + 700
    height = messages_frame.winfo_reqheight() + input_frame.winfo_reqheight() + 600
    root.geometry(f"{width}x{height}")
    insert_bot_message("Olá! Tudo bem?")
    insert_bot_message("Como posso te ajudar com seu TCC?!")

    root.mainloop()