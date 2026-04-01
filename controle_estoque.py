import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox , simpledialog
import os 
from datetime import datetime
DB_FILE = "estoque.db"
#função segurança
def hash_senha(senha):
    return senha

#janela de login
class Janelalogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry("420x320")
        self.janela.title("LOGIN")
        self.janela.resizable(False,False)
        self.janela.eval("tk::PlaceWindow . center")
        #criação frame
        frame_principal = ttk.Frame(self.janela, padding="30 40")
        frame_principal.pack(fill="both" , expand=True)

        ttk.Label(frame_principal, text="Login controle de estoque",font=("Arial",14,"bold"))\
             .grid(row=0, column=1, columnspan=2,pady=(0,25), sticky="ew")
        ttk.Label(frame_principal, text="USUÁRIO: ").grid(row=1, column=0, sticky="e",pady=8)
        self.usuario_var = tk.StringVar(value="admin")
        entrada_usuario = ttk.Entry(frame_principal, textvariable=self.usuario_var,width=25)
        entrada_usuario.grid(row=1,column=1,pady=8,sticky="w")
        
        ttk.Label(frame_principal, text="SENHA: ").grid(row=2, column=0, sticky="e",pady=8)
        self.senha_var = tk.StringVar()
        self.entrada_senha = ttk.Entry(frame_principal,textvariable=self.senha_var,width=25, show="*")
        self.entrada_senha.grid(row=2,column=1,pady=8,sticky="w")
        #botão
        btn_frame = ttk.Frame(frame_principal)
        btn_frame.grid(row=4 , column=0, columnspan=2, pady=8, sticky="ew")
        ttk.Button(btn_frame,text="ENTRAR",command=self.verificar_login).pack(side='left')
        ttk.Button(btn_frame,text="SAIR").pack(side='left',padx= 10)
        #logar enter
        self.entrada_senha.bind("<Return>", lambda e: self.vericar_login())
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial",10,"bold"))
        self.entrada_senha.focus()

    def verificar_login(self):
        usuario = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()
        
        if usuario == "admin" and senha == "123":
            messagebox.showinfo("bem vindo" , f"login realizado com sucesso!, ola {usuario}")
            self.janela.destroy()
            abrir_sistema_estoque()
        else:
            messagebox.showerror("Erro de login", "Usuario ou senha incorretos")
            self.senha_var.set("") 
            self.entrada_senha.focus()   

class EstoqueApp:
    def __init__(self,janela_main):
        self.janela_main = janela_main
        self.janela_main.title("controle de estoque")
        self.janela_main.geometry("950x650")
        self.janela_main.minsize(850, 600)

        self.conn = sqlite3.connect(DB_FILE)
        self.criar_tabelas()
        self.criar_interface()

        style = ttk.Style()
        style.configure("Treeview.Heading", font= ("Arial" , 10))
        style.configure("Treeview", rowheight=26, font= ("Arial" , 10))

    def criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
            )
            ''')
        self.conn.commit()

    def criar_interface(self):
        #botões de interação
        frame_botoes = ttk.Frame(self.janela_main, padding="10")
        frame_botoes.pack(fill="x")

        botoes = [
            ("novo produto ", self.novo_produto),
            ("Editar produto ", self.editar_produto),
            ("Excluir produto ", self.excluir_produto),
            ("Entrada produto ", self.entrada_estoque),
            ("Saída produto ", self.saida_estoque),
            ("Atualizar produto ", self.atualizar_tabela),
            ("SAIR ", self.sair)
        ]   

        for texto, cmd in botoes:
            ttk.Button(frame_botoes, text=texto, command=cmd).pack(side="left" , padx = 5) 
        #tabela
        frame_tabela = ttk.Frame(self.janela_main, padding="10")
        frame_tabela.pack(fill="both", expand=True)
        colunas = ("id", "nome" , "quantidade" , "preco")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show= "headings", selectmode="browse")

        self.tree.heading("id" , text= "código")
        self.tree.heading("nome" , text= "Nome do produto")
        self.tree.heading("quantidade" , text= "quantidade")
        self.tree.heading("preco" , text= "preço R$")

        self.tree.column("id", width=50, anchor= "center")
        self.tree.column("nome", width=150)
        self.tree.column("quantidade", width=100, anchor= "center")
        self.tree.column("preco", width=50, anchor= "e")

        scrolibar = ttk.Scrollbar(frame_tabela, orient="vertical" , command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrolibar.set)

        self.tree.pack(side="left", fill="both",expand=True)
        scrolibar.pack(side='right',fill="y")

        self.status_var = tk.StringVar(value="produto")
        ttk.Label(self.janela_main, textvariable= self.status_var, relief="sunken",anchor='w')\
            .pack(side="bottom", fill= "x", ipady=5)
        
        self.atualizar_tabela()

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id , nome , quantidade, preco FROM produtos ORDER BY id")
        for row in cursor.fetchall():
            self.tree.insert("" ,"end", values=(row[0], row[1], row[2],f"{row[3]:.2f}"))    
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        self.status_var.set(f"total de produtos: {total}  |  Base de dados{DB_FILE}")

    def get_produto_selecionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("ATENÇÃO" , "Selecione um produto na tabela!")   
            return None
        id = self.tree.item(sel[0])["values"][0]
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome , quantidade , preco FROM produtos WHERE id=?",(id,))
        row = cursor.fetchone()
        return (id, {"nome": row[0], "quantidade": row[1], "preco": row[2]}) if row else None

    def novo_produto(self):
        janela_add = tk.Toplevel(self.janela_main)
        janela_add.title("Adcionar produto")
        janela_add.geometry("450x350")
        janela_add.transient(self.janela_main)
        janela_add.grab_set()

        ttk.Label(janela_add,text="ID:" ).pack(pady=(20,5))
        entrada_id = ttk.Entry(janela_add, width=25)
        entrada_id.pack()

        ttk.Label(janela_add,text="nome:" ).pack(pady=(20,5))
        entrada_nome = ttk.Entry(janela_add, width=25)
        entrada_nome.pack()

        ttk.Label(janela_add,text="quantidade:" ).pack(pady=(20,5))
        entrada_quantidade = ttk.Entry(janela_add, width=25)
        entrada_quantidade.pack()

        ttk.Label(janela_add,text="preço UND:" ).pack(pady=(20,5))
        entrada_preco = ttk.Entry(janela_add, width=25)
        entrada_preco.pack()   

        def salvar():
            id_prod = entrada_id.get().strip().upper()
            nome = entrada_nome.get().strip()
            try:
                qtd = int(entrada_quantidade.get())
                preco_str = entrada_preco.get().strip().replace(',', '.')
                preco = float(preco_str)
            except ValueError:
                messagebox.showerror("ERRO", 'Valores inválidos (Quantidade ou Preço)')
                return 
            
            if not id_prod or not nome:
                messagebox.showerror("ERRO", "ID e Nome são obrigatórios")
                return

            try:
                cursor = self.conn.cursor()
                # CORREÇÃO: Sintaxe correta do INSERT com placeholders
                cursor.execute("INSERT INTO produtos (id, nome, quantidade, preco) VALUES (?, ?, ?, ?)",
                               (id_prod, nome, qtd, preco))
                self.conn.commit()
                self.atualizar_tabela()
                janela_add.destroy()
                messagebox.showinfo("Sucesso", f"Produto {nome} cadastrado")
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Este ID já existe") 
        #botão    
        ttk.Button(janela_add, text= "salvar", command=salvar).pack(pady=25)   

    def editar_produto(self):
        item = self.get_produto_selecionado()
        if not item:
            return
        id,dados = item

        janela_edit = tk.Toplevel(self.janela_main)
        janela_edit.title("editar produto")
        janela_edit.geometry("450x350")
        janela_edit.transient(self.janela_main)
        janela_edit.grab_set()

        ttk.Label(janela_edit,text=f"ID: {id}").pack(pady=10)

        ttk.Label(janela_edit, text= "Nome: ").pack()
        entrada_nome = ttk.Entry(janela_edit,width=50)
        entrada_nome.insert(0, dados["nome"])
        entrada_nome.pack(pady=5)

        ttk.Label(janela_edit, text= "Quantidade: ").pack()
        entrada_quantidade = ttk.Entry(janela_edit,width=50)
        entrada_quantidade.insert(0,dados["quantidade"])
        entrada_quantidade.pack(pady=5)

        ttk.Label(janela_edit, text= "Preço R$: ").pack()
        entrada_preco = ttk.Entry(janela_edit,width=50)
        entrada_preco.insert(0,dados["preco"])
        entrada_preco.pack(pady=5)
        def salvar():
            try:
                nome = entrada_nome.get().strip()
                qtd = int(entrada_quantidade.get())
                preco = float(entrada_preco.get().replace(",","."))
                cursor = self.conn.cursor()
                cursor.execute("UPDATE produtos SET nome=? , quantidade=? , preco=?  WHERE id=?",
                                (nome , qtd , preco , id))
                self.conn.commit()
                self.atualizar_tabela()
                janela_edit.destroy()
                messagebox.showinfo("Sucesso!" , "produto Atualizado")
            except:
                messagebox.showerror("Error" , "verifique valores")
        ttk.Button(janela_edit, text="Salvar Alterações" , command=salvar).pack(pady=25)        


    def excluir_produto(self):
        item = self.get_produto_selecionado()
        if not item:
            return
        id,dados = item
        if messagebox.askyesno("confirmação" , f"excluir {dados['nome']}({id})"):
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
            self.conn.commit()
            self.atualizar_tabela()
            messagebox.showinfo("sucesso" , "produto exclúido")



    def movimentar_estoque(self, tipo):
        item = self.get_produto_selecionado()
        if not item:
            return
        id,dados = item
        titulo = "Entrada" if tipo == "entrada" else "saida"
        qnt_str = simpledialog.askstring(titulo , f"quantidade a {tipo} em {dados["nome"]}: ", parent=self.janela_main)
        if not qnt_str:
            return
        try:
            qtd = int(qnt_str)
            if qtd <=0:
                raise ValueError
            
            cursor = self.conn.cursor()
            if tipo == "entrada":
                cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id=?",(qtd , id))
            else:
                cursor.execute("SELECT quantidade FROM produtos WHERE id=?" , (id,)) 
                atual = cursor.fetchone()[0]
                if qtd > atual:
                    messagebox.showerror("Error", f"estoque insufuciente! Disponivel: {atual}")
                    return
                cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id=?", (qtd , id))
                self.conn.commit()
                self.atualizar_tabela()
                messagebox.showinfo("Sucesso!" f"Movimentação de {qtd} unidades realiza!")
        except:
            messagebox.showerror("error" , "informe um número inteiro Positivo")       

    def entrada_estoque(self):
        self.movimentar_estoque("entrada") 


    def saida_estoque(self): 
        self.movimentar_estoque("saida")
    def sair(self):   
        self.conn.close() 
        self.janela_main.quit()
                                

#====não mecher em nada======     
def abrir_sistema_estoque():
    janela_main = tk.Tk()
    EstoqueApp(janela_main)
    janela_main.mainloop()

if __name__ == "__main__":
    janela = tk.Tk()
    app = Janelalogin(janela) 
    janela.mainloop()      
