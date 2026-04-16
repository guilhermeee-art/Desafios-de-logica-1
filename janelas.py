import tkinter as tk
janela = tk.Tk()
janela.geometry("600x500")
janela.title("sixseven")

frame = tk.Frame(janela, bg="lightblue")
frame.place(relx=0.0,rely=0.0, relwidth=0.2, relheight=1)

frame2 = tk.Frame(janela, bg="yellow") 
frame2.place(relx=0.2 , rely=0.8, relwidth=1 , relheight=0.2)









janela.mainloop()