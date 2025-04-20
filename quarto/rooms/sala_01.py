from helpers import text, hyperlink

def revisar(answer):
    if answer == "Hola Mundo":
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_02.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    revisar(None)
    revisar("Hola Mundo")
    revisar("Hola")