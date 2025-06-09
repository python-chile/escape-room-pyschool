from helpers import text, hyperlink

def revisar(respuesta):
    lista = ["GRANDE_10", "GRANDE_1", "GRANDE_3"]

    if respuesta is None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == lista:
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_08.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    test = ["GRANDE_10", "GRANDE_1", "GRANDE_3"]
    revisar("test")
    revisar(None)
    revisar(test)
