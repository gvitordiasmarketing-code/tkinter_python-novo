import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("formulário")

def enviar():
    nome = entrada_nome.get() 
    estado = combo_estado.get()
    sexo = opc.get()

    sexo_texto = "masculino" if sexo == 1 else "feminino"


    msg = f"Nome: {nome}\n Estado{estado}\n Sexo: {sexo_texto}"
    messagebox.showinfo("Dados Enviados", msg)




tk.Label(janela, text= "Formulário de Cadastro", font=("Arial",14)).grid(column=1,pady=10)
tk.Label(janela, text="nome: ").grid(row=1,column=0)
entrada_nome = tk.Entry(janela ,font=("Ariel"))
entrada_nome.grid(row=1, column=1)
opc= tk.IntVar()


tk.Label(janela, text="sexo: ").grid(row=3, column=0)
tk.Radiobutton(janela, text= "masculino",font= ("Ariel") ,value=1,variable=opc)\
      .grid(row=4,column=1)
tk.Radiobutton(janela, text= "feminino",font= ("Ariel") ,value=2,variable=opc)\
      .grid(row=5,column=1)

tk.Label(janela, text= "Estado: ", font=("Ariel")).grid(row=6, column=0)
combo_estado = ttk.Combobox(janela, values= ["MG", "SP", "RJ", "RN", "BA"])
combo_estado.grid(row=6, column=1)



tk.Button(janela, text="enviar", comand= enviar).grid(row=7, column=1,pady=20)








janela.mainloop()