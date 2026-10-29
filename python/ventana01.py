import tkinter as tk

def click():
    print("El usuario se llama: ", texto.get())

#crear ventana
ventana = tk.Tk()
ventana.title("Mi primer juego")
ventana.geometry("300x300+0+0")

#crear boton
boton = tk.Button(ventana, text="Mi primer boton", command = click)
boton.pack
boton.place(x=100, y=100)

#crear caja de texto
texto = tk.Entry(ventana, width=30)
texto.pack(pady = 30)
texto.get()
ventana.mainloop()