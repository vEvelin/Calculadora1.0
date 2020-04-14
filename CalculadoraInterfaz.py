import tkinter as tk
calculadora=''
root= tk.Tk()
mensaje = tk.StringVar()
resultado = tk.StringVar()
nro1=tk.StringVar()
nro2=tk.StringVar()


def operacion_suma():
    operacion_suma=int(nro1.get())+int(nro2.get())
    resultado.set(operacion_suma)


def operacion_resta():
    operacion_resta = int(nro1.get()) - int(nro2.get())
    resultado.set(operacion_resta)

def operacion_multiplicar():
    operacion_multiplicar= int(nro1.get())*int(nro2.get())
    resultado.set(operacion_multiplicar)

def operacion_dividir():
    if (nro2 != 0):
        operacion_dividir=int(nro1.get())/int(nro2.get())
        resultado.set(operacion_dividir)
    else:
        resultado.set('Operacion Indeterminada')

def limpiar_pantalla():
    nro1.set('')
    nro2.set('')
    resultado.set('')

root.geometry('530x490')
root.title('Calculadora')

root.configure(bg="#263238")
tk.Label(root, text='Calculadora', bg="#263238", fg='#009688', font=("Times", 34)).place(x=149, y=40)

tk.Label(root, text='Ingrese Primer número :', bg="#263238", fg='#009688', font=('Times', 10)).place(x=20, y=140)
tk.Entry(root, justify='center', textvariable=nro1,bg='#009688').place(x=170, y=140)

tk.Label(root, text='Ingrese Segundo número :', bg="#263238", fg='#009688', font=('Times', 10)).place(x=20, y=210)
tk.Entry(root, justify='center', textvariable=nro2,bg='#009688').place(x=170, y=210)

tk.Label(root, text='Resultado  :', bg="#263238", fg='#009688', font=('Times', 10)).place(x=25, y=280)
tk.Entry(root, justify='center', textvariable=resultado,bg='#009688').place(x=170, y=280)

#suma
tk.Button(root, text='+', bg="#263238", fg='#ff5722',font=('Times',35),command=operacion_suma, bd=0).place(x=336, y=115)

#resta
tk.Button(root, text='-', bg="#263238", fg='#ff5722',font=('Times',45), bd=0, command=operacion_resta).place(x=436, y=98)

#multiplicacion
tk.Button(root, text='*', bg="#263238", fg='#ff5722',font=('Times',42), bd=0, command=operacion_multiplicar).place(x=336, y=210)

#division
tk.Button(root, text='/', bg="#263238", fg='#ff5722',font=('Times',35), bd=0, command=operacion_dividir).place(x=436, y=211)

#limpiar_pantalla
tk.Button(root, text='Limpiar', bg="#263238", fg='#ff5722',font=('Times',16), bd=0 , command=limpiar_pantalla).place(x=376, y=297)

#salir
tk.Button(root, text='Salir', bg="#263238", fg='#009688',font=('Times',20), bd=0, command=root.destroy).place(x=225, y=388)

root.mainloop()