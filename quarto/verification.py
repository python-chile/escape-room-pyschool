# types: alert, danger, success, info, primary

def text(title="", text="", type="info", dismissable=False):
    class_str = f'alert alert-{type}'
    text_str = f'<div class="{class_str}">'
    if title: 
        text_str += f'<h4 class=\"alert-heading\">{title}</h4>'
    if dismissable: 
        text_str += f'<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>'
    if text: 
        text_str += f'<p class=\"mb-0\">{text}</p>'
    text_str += '</div>'
    print(text_str)


def hyperlink(url, text, type="info"):
    print(f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>')


def check_answer(answer, room_number):
    """
    Verifica si la respuesta es correcta para la habitación especificada.
    
    Args:
        answer: La respuesta proporcionada por el usuario.
        room_number (int): El número de la habitación a verificar.   
    """
    if room_number == 1:
        check_answer_1(answer)
    elif room_number == 2:
        check_answer_2(answer)
    else:
        print("No hay una habitación con ese número")
    return


def check_answer_1(answer):
    if answer == 5:
        hyperlink("2.html", "¡Correcto! Avanza a la siguiente página", "success")
    elif answer == None:
        text("No hay una respuesta", "intenta de nuevo.", "warning")
    else:
        text("No no no...", "intenta de nuevo.", "warning")


def check_answer_2(answer):
    if answer == "2":
        hyperlink("end.html", "¡Correcto! Avanza a la siguiente página", "success")
    else:
        text("No no no...", "intenta de nuevo.", "warning")

if __name__ == "__main__":
    check_answer(None, 1)
    check_answer(5, 1)
    check_answer("2", 2)
