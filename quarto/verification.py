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
        print("¡Correcto! Avanza a la siguiente página")
        print('<a href="2.html">Siguiente página...</a>')
    else:
        print("No no no... intenta de nuevo.")

def check_answer_2(answer):
    if answer == "2":
        print("¡Correcto! Avanza a la siguiente página")
        print('<a href="3.html">Siguiente página...</a>')
    else:
        print("No no no... intenta de nuevo.")