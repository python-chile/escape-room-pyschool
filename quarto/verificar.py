# types: alert, danger, success, info, primary

def text(text="", type="info"):
    class_str = f'alert alert-{type}'
    text_str = f'<span class="{class_str}" w-100 h-100>{text}</span>'
    print(text_str)


def hyperlink(text, url, type="info"):
    print(f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>')

def salon_1(answer):
    if answer == 5:
        hyperlink("¡Correcto! Avanza a la siguiente página", "2.html","success")
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
