from helpers import text, hyperlink

def revisar(respuesta):
    lista = ["GRANDE_10", "GRANDE_1", "GRANDE_3"]

    if type(respuesta) is not list:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")
    elif respuesta == lista:
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_08.html", "success")
    else:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")

if __name__ == "__main__":
    test = ["GRANDE_10", "GRANDE_1", "GRANDE_3"]
    revisar(test)
