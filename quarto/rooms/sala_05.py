from helpers import text, hyperlink

def revisar(respuesta):
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == True:
        hyperlink("¡Correcto! Avanza a la siguiente página", "2.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    revisar(None)
    revisar(True)
    revisar(False)
