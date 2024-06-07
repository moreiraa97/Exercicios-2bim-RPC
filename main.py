from tkinter import *
from xmlrpc.client import ServerProxy

def calculate():
    url_servidor = "a61990e3-7cdd-4188-9b68-e3d47ef25bbb-00-1epsoy4i1rui5.kirk.replit.dev"
    servidor = ServerProxy(f"https://{url_servidor}")
    operacao = operacao_var.get()
    resultado = "Operacao inválida"
    if operacao == "Soma":
        resultado = servidor.somaisoma(int(entry1.get()), int(entry2.get()))
    elif operacao == "Subtracao":
        resultado = servidor.sobtraisub(int(entry1.get()), int(entry2.get()))
    elif operacao == "Multiplicação":
        resultado = servidor.multiplicaismult(int(entry1.get()), int(entry2.get()))
    elif operacao == "Divisão":
        resultado = servidor.divideisdiv(int(entry1.get()), int(entry2.get()))
    label_result["text"] = f"Resultado: {resultado}"

root = Tk()

label1 = Label(root, text="Número 1:")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Número 2:")
label2.pack()

entry2 = Entry(root)
entry2.pack()

operacao_var = StringVar(root)
operacao_var.set("Soma") 

option_menu = OptionMenu(root, operacao_var, "Soma", "Subtracao","Divisão", "Multiplicação")
option_menu.pack()

button = Button(root, text="Calcular", command=calculate)
button.pack()

label_result = Label(root, text="Resultado: ")
label_result.pack()

root.mainloop()