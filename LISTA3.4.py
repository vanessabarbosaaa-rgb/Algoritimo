LISTA3
def busca_string(lista, alvo):

    alvo_lower = alvo.lower()  

    for i, nome in enumerate(lista):
        if nome.lower() == alvo_lower:
            return i  
    return -1 


nomes = ["Alice", "Bruno", "Carla", "bruno"]
resultado = busca_string(nomes, "BRUNO")
print(resultado)  