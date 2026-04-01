import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("formulário de cadastro")
janela.geometry("400x400")

def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    escola = escolaridade.get()
    atuacao = opc.get()
    

    atuacao = "Gerencia" if atuacao == 1 else "Administrativo"


    msg = f"Nome:  {nome}\n idade'{idade}\n escolaridade: {escola} \n area de atuacao: {atuacao}"
    messagebox.showinfo("Dados Enviados", msg)


tk.Label(janela, text= "Dados pessoais", font=("Arial",14)).grid(column=1,pady= 20)
#nome
tk.Label(janela, text="Dados pessoais" ,font=("Arial",14)).grid(row=1, column=0)
entrada_nome = tk.Entry(janela, font=("Arial"))
entrada_nome.grid(row=1, column=1)


#idade
tk.Label(janela, text="idade" ,font=("Ariel",14)).grid(row=2, column=0)
entrada_idade = tk.Entry(janela, font=("Arial"))
entrada_idade.grid(row=2, column=1)
    
#dados profissionais
tk.Label(janela, text= "dados profissionais", font=("Arial",14)).grid(column=0 ,pady=20)

#escolaridade
tk.Label(janela, text= "escolaridade", font=("Arial")).grid(row=4, column=0)
escolaridade = ttk.Combobox(janela, values= ["Ensino médio completo","Ensino médio incompleto", "Ensino fundamental completo","Ensino fundamental incompleto", "ensino superior"])
escolaridade.grid(row=4, column=1)

#atuacao
opc= tk.IntVar()
tk.Label(janela, text="area de atuacao: ").grid(row=5, column=0)
tk.Radiobutton(janela, text= "Gerencia", font= ("Arial") ,value=1,variable=opc)\
    .grid(row=6,column=1)
tk.Radiobutton(janela, text= "Administrativo", font= ("Arial") ,value=2,variable=opc)\
    .grid(row=7,column=1)
tk.Radiobutton(janela, text= "Analista de dados", font= ("Arial") ,value=3,variable=opc)\
    .grid(row=8,column=1)
tk.Radiobutton(janela, text= "tecnico de informatica", font= ("Arial") ,value=4,variable=opc)\
    .grid(row=9,column=1)
tk.Radiobutton(janela, text= "Atendente de telemarkting", font= ("Arial") ,value=5,variable=opc)\
    .grid(row=10,column=1)

tk.Button(janela, text="enviar", command= enviar).grid(row=11, column=1,pady=20)





janela.mainloop()   









