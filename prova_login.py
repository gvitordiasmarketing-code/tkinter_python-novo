import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("cadastro")
janela.configure(background="blue")
janela.geometry("400x300")

def enviar():
    nome =  entrada_login.get()
    msg = f"usuario logado com sucesso"
    messagebox.showinfo("dados enviados", msg)

tk.Label(janela, text= "formulário de cadastro", font=("Arial",14)).grid(column=1,pady=20)
tk.Label(janela, text="nome:").grid(row=1,column=0)
entrada_login = tk.Entry(janela ,font=("Arial"))
entrada_login.grid(row=1, column=1)

#senha
tk.Label(janela, text="senha:").grid(row=2,column=0)
entrada_senha = tk.Entry(janela ,font=("Arial"))
entrada_senha.grid(row=2, column=1)

#botão
tk.Button(janela, text="enviar", command= enviar).grid(row=11, column=1,pady=20)

imagem =tk.PhotoImage(file="cam.png")
imagem=imagem.subsample(3,3)
tk.Label(janela,image=imagem).place(x=250,y=20)



janela.mainloop()




