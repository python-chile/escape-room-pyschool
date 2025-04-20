from helpers import text, hyperlink

def verificar(col_x, col_y, respuesta):
    import pandas as pd
    url = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'
    df = pd.read_csv(url)
    
    if col_x is None or col_y is None or respuesta is None:
        text("Debes definir las variables `col_x`, `col_y` y `respuesta`.", "info")
    else:
        df['suma'] = df[col_x] + df[col_y]
        respuesta_correcta = df.loc[df['suma'].idxmax(), 'Name']
        
        if respuesta == respuesta_correcta:
            hyperlink("¡Perfecto! Has dominado la visualización y el análisis de datos. Avanza a la siguiente sala.", "sala_final.html", "success")
        else:
            text("Revisa bien... parece que no sumaste correctamente o elegiste mal el Pokémon.", "warning")


if __name__ == "__main__":
    verificar(None, None, None)
    verificar("Attack", "Defense", "Dragon")
    verificar("Attack", "Defense", "Fire")
    verificar("Attack", "Defense", "Water")
