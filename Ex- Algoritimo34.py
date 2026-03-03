Ex- Algoritimo34
def fatorial(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * fatorial(n - 1) 

num = int(input("Digite um número: "))
print("Fatorial:", fatorial(num))
