# types: warning, danger, success, info, primary
########################################################
# UTILIDADES
########################################################

def text(text="", type="info"):
    text_str = f'<div class="alert alert-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


########################################################
# SALONES
########################################################

def salon_0(answer):
    if answer == "PySchool2025":
        hyperlink("¡Correcto! Avanza a la siguiente página", "1.html", "success")
    elif answer == None:
        text("No es correcto. Intenta de nuevo.", "danger")
    else:
        text("Estás probando nuevas respuestas, muy bien. Recuerda que la respuesta es PySchool2025", "warning")


def salon_1(answer):
    if answer == 5:
        hyperlink("¡Correcto! Avanza a la siguiente página", "2.html", "success")
    elif answer == None:
        text("No es correcto. Intenta de nuevo.", "danger")
    else:
        text("Tienes que escribir la respuesta en el cuadro de texto.", "alert")


def salon_2(answer):
    if answer == "2":
        hyperlink("¡Correcto! Avanza a la siguiente página", "end.html", "success")
    elif answer == None:
        text("No es correcto. Intenta de nuevo.", "danger")
    else:
        text("No no no...", "alert")

if __name__ == "__main__":
    salon_1(None)
    salon_1(5)
    salon_1("2")
