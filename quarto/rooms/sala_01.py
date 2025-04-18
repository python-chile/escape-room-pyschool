# types: warning, danger, success, info, primary
########################################################
# UTILIDADES
########################################################

def text(text="", type="info"):
    text_str = f'<div class="btn btn-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


def revisar(answer):
    if answer == "Hola Mundo":
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_02.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")