from helpers import text, hyperlink

def revisar(respuesta):
    lista = ["GRANDE_10", "GRANDE_1", "GRANDE_3"]
    if respuesta == None or type(respuesta) != list:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == lista:
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_08.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    objetos = ["MEDIANO_3", "MEDIANO_1", "MEDIANO_3", "GRANDE_1", "PEQUEÑO_10", "GRANDE_10", "GRANDE_3", "PEQUEÑO_1", "PEQUEÑO_10"]
    print(sorted(objetos, reverse=True))
    lista = ["GRANDE_10", "GRANDE_1", "GRANDE_3"]
    print(lista)
