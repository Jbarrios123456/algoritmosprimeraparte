import tkinter as tk

# significado jm = Junior y Maynor
# hola

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

    jm_boton_informacion = tk.Button(jm_ventana, text="Informacion", command=jm_informacion)
    jm_boton_informacion.pack()
    jm_boton_manual = tk.Button(jm_ventana, text="Manual de Usuario", command=jm_manual_usuario)
    jm_boton_manual.pack()
    jm_boton_integrantes = tk.Button(jm_ventana, text="Integrantes", command=jm_integrantes)
    jm_boton_integrantes.pack()

    jm_boton_cerrar = tk.Button(jm_ventana, text="Cerrar", command=jm_ventana.destroy)
    jm_boton_cerrar.pack()

def jm_informacion():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("informacion")
    jm_ventana.geometry("500x300")
    jm_titulo = tk.Label(jm_ventana, text="Informacion sobre nuestor proyecto", font=("Arial", 20))
    jm_titulo.pack(pady=20)
    jm_info = tk.Label(jm_ventana, text="Luego pondremos información", font=("Arial", 10))
    jm_info.pack(pady=20)

def jm_manual_usuario():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Manual de Usuario")
    jm_ventana.geometry("250x150")

def jm_integrantes():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Integrantes")
    jm_ventana.geometry("600x300")
    jm_junior = tk.Label(jm_ventana, text="Junior Alvaro René Barrios Flores" \
    " Carnet: 7690-25-16187", font=("Arial", 15))
    jm_junior.pack(pady=40)
    jm_maynor = tk.Label(jm_ventana, text="Maynor Suriel Del Valle Alvarado" \
    " Carnet: 7690-25-21809", font=("Arial", 15))
    jm_maynor.pack(pady=20)

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
