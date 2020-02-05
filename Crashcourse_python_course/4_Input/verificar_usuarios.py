# !/usr/bin/python3.5


import time

# Creamos una lista de usuarios que necesitan confirmación
# Creamos otra lista donde almacenaermos a los usuarios verificados.

usuarios_pendientes = ['alicia', 'ernesto', 'jose']
usuarios_confirmados = []

# Verificamos todos los usuarios hasta que no haya usuarios pendientes
while usuarios_pendientes:
    usuario = usuarios_pendientes.pop()

    print("\nEstamos verificando tu cuenta, " + usuario.title() )
    time.sleep(2)
    usuarios_confirmados.append(usuario)

    print("Enhorabuena " + usuario.title() + ", su cuenta ha sido confirmada")
    time.sleep(1)