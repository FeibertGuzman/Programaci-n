from PyQt6 import QtWidgets, uic  # Importamos PyQt6 y el módulo uic para cargar las interfaces gráficas

# Inicializamos la aplicación
app = QtWidgets.QApplication([])

# Cargar las tres ventanas desde archivos .ui
login = uic.loadUi("Login QrD V1.ui")  # Ventana principal de login
error = uic.loadUi("Ventana2.ui")  # Ventana de error
success = uic.loadUi("Ventana3.ui")  # Ventana de ingreso exitoso

# Función para manejar el inicio de sesión
def verificar_login():
    usuario = login.L_Usuario.text()  # Obtiene el texto del campo de usuario
    contrasena = login.L_Contrasena.text()  # Obtiene el texto del campo de contraseña

    # Validación de usuario y contraseña
    if len(usuario) == 0 or len(contrasena) == 0:
        login.label_5.setText("Ingrese todos sus datos")
    elif usuario == "salle" and contrasena == "12345":
        entrar()
    else: 
        salir_error()  

def entrar():
    login.hide()
    entrar.show()

def salir_error():
    login.hide()
    error.show()
    
def regresar_entrar():
    entrar.hide()
    login.label_5.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.show()

def salir():
    app.exit()

login.Bt_ingresar.clicked.connect(verificar_login)  
error.pushButton.clicked.connect(regresar_error)  


# Ejecutar la ventana principal de login
login.show()

# Ejecutar la aplicación
app.exec()
