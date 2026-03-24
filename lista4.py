def soma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)
print(f"Soma dos dígitos de 123: {soma_digitos(123)}")


def conta_digitos(n):
   
    if n < 10:
        return 1
    return 1 + conta_digitos(n // 10)
print(f"Dígitos de 9876: {conta_digitos(9876)}") 


def inverte_string(s):
 
    if len(s) <= 1:
        return s
    return s[-1] + inverte_string(s[:-1])
print(f"Inverso de 'recursao': {inverte_string('recursao')}")


def eh_palindromo(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    return eh_palindromo(s[1:-1])
print(f"'arara' é palíndromo? {eh_palindromo('arara')}")

def produto(a, b):
  
    if b == 0:
        return 0
    if b == 1:
        return a
    return a + produto(a, b - 1)
print(f"Produto de 3 e 4: {produto(3, 4)}")


def maior_elemento(lista):
   
    if len(lista) == 1:
        return lista[0]
    
    maior_do_resto = maior_elemento(lista[1:])
    if lista[0] > maior_do_resto:
        return lista[0]
    else:
        return maior_do_resto
print(f"Maior de [1, 5, 3, 9, 2]: {maior_elemento([1, 5, 3, 9, 2])}")


def mdc(a, b):
    
    if b == 0:
        return a
    return mdc(b, a % b)
print(f"MDC de 48 e 18: {mdc(48, 18)}") 



def conta_ocorrencias(lista, elemento):

    if not lista:
        return 0

    contagem_atual = 1 if lista[0] == elemento else 0
    return contagem_atual + conta_ocorrencias(lista[1:], elemento)
print(f"Ocorrências de 2 em [1, 2, 3, 2, 2]: {conta_ocorrencias([1, 2, 3, 2, 2], 2)}") 


def soma_lista(lista):
    
    
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])
print(f"Soma de [10, 20, 30]: {soma_lista([10, 20, 30])}") 



def ehh_primo(n, divisor=2):

    if n <= 1:
        return False
    if divisor == n:
        return True
    if n % divisor == 0:
        return False
    return ehh_primo(n, divisor + 1)

print(f"7 é primo? {ehh_primo(7)}") 
print(f"10 é primo? {ehh_primo(10)}") 