from helpers import text, hyperlink
import statistics

def revisar(respuesta):
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == 27.75:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_07.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    lista_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    promedio = statistics.mean([lista_fibonacci[0], lista_fibonacci[2], lista_fibonacci[10], lista_fibonacci[-2]])
    revisar(None)
    revisar(promedio)
    revisar(False)
