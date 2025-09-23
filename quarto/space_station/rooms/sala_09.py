from helpers import text, hyperlink

def revisar(respuesta):

    lista = ['linterna', 'monitor principal', 'antena', 'filtro gases', 'lentes infrarojo', 'teclado']
    if respuesta == lista:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_10.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    objetos = ["linterna", "audífonos", "monitor principal", "motor de enfriador", "monitor de repuesto", "antena",
               "filtro gases", "lentes infrarojo", "teclado"]
    reparados = ["monitor de repuesto", "audífonos", "motor de enfriador"]
    por_reparar = []

    for objeto in objetos:
        if objeto not in reparados:
            por_reparar.append(objeto)

    revisar(None)
    revisar(por_reparar)
    revisar("lista")
