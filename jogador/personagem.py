atributos = {
    "Força": 0,
    "Agilidade": 0,
    "Intelecto": 0,
    "Presença": 0,
    "Vigor": 0
}

def criarAtributos(forca,agilidade,intelecto,presenca,vigor):
    return {
        "Força": forca,
        "Agilidade": agilidade,
        "Intelecto": intelecto,
        "Presença": presenca,
        "Vigor": vigor
    }

def validarAtributos(atributos):
    total = sum(atributos.values())

    if total > 10:
        return False
    else:
        return True