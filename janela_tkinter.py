import tkinter as tk


janela_main = tk.Tk() 
janela_main.title("jogador")

janela_main.configure(background="red")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("400x400")

#objetos em janela
tk.Label(janela_main, 
         text="HULK",
         bg="red",
         font=("Arial" ,20 ,"bold")
         ).pack()

tk.Label(janela_main, 
         text="\nJOGADOR DE FUTEBOL COM 39 ANOS" \
         "\nem atividade no esporte" \
         "\nmelhor jogador do brasil em atividade",
         bg="red",
         font=("Arial" ,20)
         ).pack()

#imagens
imagem = tk.PhotoImage(file="hulk.png")
tk.Label(janela_main, image=imagem).pack()





janela_main.mainloop()