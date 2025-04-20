########################################################
# UTILIDADES
########################################################

def text(text="", type="info"):
    text_str = f'<div class="btn btn-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


def verificar(url, df):
    url_correcta = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'
    if url is None or df is None:
        text("Debes asignar un valor a las variables `url` y `df`.", "info")
    elif url == url_correcta and len(df.columns) >= 10:
        hyperlink("¡Correcto! Has restaurado el sistema del laboratorio. Avanza a la siguiente sala.", "1.html", "success")
    else:
        text("Revisa bien las instrucciones... ¿Estás seguro que cargaste los datos correctamente?", "warning")