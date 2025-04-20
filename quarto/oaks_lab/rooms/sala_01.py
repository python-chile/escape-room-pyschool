from helpers import text, hyperlink

def verificar(desc):
    import pandas as pd

    if desc is None:
        text("Debes asignar valores a las variables `info` y `desc` ejecutando `df.info()` y `df.describe()`.", "info")
    
    elif not isinstance(desc, pd.DataFrame):
        text("La variable `desc` debe ser el resultado de `df.describe()`.", "warning")
    
    else:
        hyperlink("¡Perfecto! Has explorado correctamente el dataset. Avanza a la siguiente sala.", "2.html", "success")

if __name__ == "__main__":
    verificar(None)
    verificar(pd.DataFrame())
    verificar(pd.DataFrame(columns=['Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']))
