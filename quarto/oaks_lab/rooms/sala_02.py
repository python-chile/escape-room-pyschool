from helpers import text, hyperlink

def verificar(respuesta):
    if respuesta is None:
        text("Debes asignar el número total de tipos de Pokémon a la variable `respuesta`.", "info")
    elif respuesta == 18:
        hyperlink("¡Correcto! Existen 18 tipos de Pokémon. Avanza a la siguiente sala.", "3.html", "success")
    else:
        text("La puerta sigue cerrada... Revisa bien los datos y cuenta nuevamente los tipos de Pokémon.", "warning")

if __name__ == "__main__":
    verificar(None)
    verificar(5)
    verificar("2")
