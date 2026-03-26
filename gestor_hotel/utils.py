

from datetime import datetime

contador_cliente = 1
contador_hotel = 1

def gerar_id_cliente():
    global contador_cliente
    novo_id = f"C{contador_cliente:03d}"
    contador_cliente += 1
    return novo_id

def gerar_id_hotel():
    global contador_hotel
    novo_id = f"H{contador_hotel:03d}"
    contador_hotel += 1
    return novo_id

def validar_data_nascimento(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False












































