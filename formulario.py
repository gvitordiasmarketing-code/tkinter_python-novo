import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela =  tk.Tk()
janela.title("Formlário")
#ENTRADA DE TEXTO
label_entrada = ttk.Label(janela, text= "Nome")
label_entrada.pack()
entrada = tk.Entry(janela)
entrada.pack()
#CHECKBOX
checkbox = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os termos", variable= checkbox )
check.pack()
#OPÇÕES
opcao = tk.IntVar()
opc1 = tk.Radiobutton(janela, text= "masculino" , variable= opcao, value=1)
opc2 = tk.Radiobutton(janela, text= "feminino" , variable= opcao, value=2)
opc3 = tk.Radiobutton(janela, text= "outro" , variable= opcao, value=3)
opc1.pack()
opc2.pack()
opc3.pack() 

lista = tk.Listbox(janela)
lista.insert(1, "Python")
lista.insert(2, "Java")
lista.insert(3, "PHP")
lista.insert(4, "Javascript")
lista.pack()

#COMBOBOX
combo = ttk.Combobox(janela, values=["MG", "RJ", "RS", "RN"])
combo.set("Selecione um Estado")
combo.pack()

#BOTÃO
def clicar():
    messagebox.showerror("Aviso", "Botão Acionado!")

btn = tk.Button(janela, text= "Mostrar mensagem", command=clicar)
btn.pack()










janela.mainloop()


