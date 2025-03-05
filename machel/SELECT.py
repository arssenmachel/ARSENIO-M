def matches_select(word):
    """
    Verifica se a palavra fornecida corresponde a "SELECT",
    ignorando diferenças entre maiúsculas e minúsculas sem usar funções nativas.
    """
    return (
        (word[0] == 'S' or word[0] == 's') and
        (word[1] == 'E' or word[1] == 'e') and
        (word[2] == 'L' or word[2] == 'l') and
        (word[3] == 'E' or word[3] == 'e') and
        (word[4] == 'C' or word[4] == 'c') and
        (word[5] == 'T' or word[5] == 't')
    )

def contains_select(texto):
    """
    Percorre a string e verifica se há "SELECT" em qualquer mistura de maiúsculas e minúsculas.
    """
    tamanho = len(texto)
    
    for i in range(tamanho - 5):  # "SELECT" tem 6 caracteres
        segmento = texto[i:i+6]
        if matches_select(segmento):
            return True
    
    return False

if _name_ == "_main_":
    entrada = input("Digite uma palavra para verificar: ")
    if contains_select(entrada):
        print("A palavra SELECT foi encontrada.")
    else:
        print("A palavra SELECT não foi encontrada.")