import tkinter as tk

# significado jm = Junior y Maynor

def jm_abrir_archivo():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Ventana de Archivo")
    jm_ventana.geometry("250x150")
    jm_boton_cerrar = tk.Button(jm_ventana, text="Cerrar", command=jm_ventana.destroy)
    jm_boton_cerrar.pack()

def jm_abrir_editar():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Ventana de Editar")
    jm_ventana.geometry("250x150")
    jm_boton_cerrar = tk.Button(jm_ventana, text="Cerrar", command=jm_ventana.destroy)
    jm_boton_cerrar.pack()

def jm_abrir_ayuda():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Ventana de Ayuda")
    jm_ventana.geometry("250x150")
    jm_boton_cerrar = tk.Button(jm_ventana, text="Cerrar", command=jm_ventana.destroy)
    jm_boton_cerrar.pack()

jm_principal = tk.Tk()
jm_principal.title("Menú Principal")
jm_principal.geometry("300x250")

jm_titulo = tk.Label(jm_principal, text="Bienvenido a nuestro proyecto", font=("Arial", 14))
jm_titulo.pack(pady=20)
jm_titulo = tk.Label(jm_principal, text="Ingrese una opción", font=("Arial", 10))
jm_titulo.pack(pady=20)
jm_boton_archivo = tk.Button(jm_principal, text="Archivo", command=jm_abrir_archivo)
jm_boton_archivo.pack(pady=5)

jm_boton_editar = tk.Button(jm_principal, text="Editar", command=jm_abrir_editar)
jm_boton_editar.pack(pady=5)

jm_boton_ayuda = tk.Button(jm_principal, text="Ayuda", command=jm_abrir_ayuda)
jm_boton_ayuda.pack(pady=5)

jm_principal.mainloop()
