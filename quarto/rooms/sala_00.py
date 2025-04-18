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


########################################################
# SALONES
########################################################

def revisar(answer):
    if answer == "PySchool2025":
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_01.html", "success")
    else:
        incorrect_answer = f"""Estás probando nuevas respuestas, muy bien.  
        Recuerda que la respuesta es PySchool2025"""
        text(incorrect_answer, "warning")


if __name__ == "__main__":
    revisar(None)
    revisar("PySchool2024")
    revisar("PySchool2025")
