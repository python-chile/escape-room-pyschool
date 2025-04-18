def text(text="", type="info"):
    text_str = f'<div class="btn btn-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


def revisar(respuesta):
    if answer == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif answer == True:
        hyperlink("¡Correcto! Avanza a la siguiente página", "2.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")