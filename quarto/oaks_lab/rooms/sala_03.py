from helpers import text, hyperlink

def verificar(respuesta_ataque, respuesta_defensa):
    if respuesta_ataque is None or respuesta_defensa is None:
        text("Debes definir las variables `respuesta_ataque` y `respuesta_defensa`.", "info")
    elif respuesta_ataque == 'Dragon' and respuesta_defensa == 'Normal':
        hyperlink("¡Correcto! Has identificado correctamente las fortalezas y debilidades. Avanza a la siguiente sala.", "sala_04.html", "success")
    else:
        text("Revisa bien los datos... ¿Estás seguro de haber calculado los promedios correctamente?", "warning")


if __name__ == "__main__":
    verificar(None, None)
    verificar("Dragon", "Normal")
    verificar("Dragon", "Fire")
    verificar("Dragon", "Water")
