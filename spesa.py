lista_della_spesa = []
def aggiungi():
    lista_della_spesa.append(valore)

def visualizza():
    for i in range(len(lista_della_spesa)):
    print(f"{i + 1}. { lista_della_spesa[i]}")

def rimuovi():
    lista_della_spesa.pop(valore)