import random
import time
import copy
import sys



sys.setrecursionlimit(200000)

# ==========================================
# A TURMA DOS LENTOS: ALGORITMOS O(N²)
# ==========================================

def selection_sort(arr):
    n = len(arr)
    #  o 'i' é a posição atual que a gente quer preencher com o menor número
    for i in range(n):
        min_idx = i # índice 'i' já é o menor de todos
        
        # Agora a gente olha pro resto da lista (de i+1 até o final) pra ver se tem alguém menor
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j #aqui acharemos alguém menor, atualize o índice

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

def bubble_sort(arr):
    n = len(arr)
    # Vai passar a lista inteira 'n' vezes
    for i in range(n):
        # Essa variável é nosso "botão de pânico". Se a gente passar pela lista toda
        # e não trocar nada de lugar, é porque a lista JÁ TÁ ORDENADA.
        swapped = False 
        
        # O pulo do gato: a cada rodada, o maior número sempre "borbulha" pro final.
        # Então a gente não precisa ir até o final da lista todas as vezes, só até 'n - i - 1'.
        for j in range(0, n - i - 1):
            # Se o cara atual for maior que o vizinho da direita, inverte eles
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
            
    return arr

def insertion_sort(arr):
    # Pense nisso como se você estivesse com cartas de baralho na mão. 
    # Começamos da segunda carta (índice 1) assumindo que a primeira carta (índice 0) já tá organizada.
    for i in range(1, len(arr)):
        key = arr[i] # Essa é a carta que a gente pegou na mão agora pra tentar encaixar
        j = i - 1    # Esse é o índice da carta imediatamente anterior a ela
        
        # Enquanto a gente não esbarrar no começo da lista (j >= 0) 
        # E a nossa carta 'key' for menor que as cartas que a gente tá olhando...
        while j >= 0 and key < arr[j]:
            # ...a gente vai empurrando as cartas grandes pra direita pra abrir espaço
            arr[j + 1] = arr[j]
            j -= 1 # Dá um passo pra trás pra olhar a próxima carta
            
        # Achamos o lugar perfeito! Coloca a carta lá.
        arr[j + 1] = key
        
    return arr


# ==========================================
# A GALERA DE PESO: ALGORITMOS RÁPIDOS O(N LOG N)
# ==========================================

def merge_sort(arr):
    # O Merge Sort é o rei do "Dividir para Conquistar". Ele só para de se dividir quando sobra 1 elemento.
    if len(arr) > 1:
        mid = len(arr) // 2 # divide no meio
        
        # Pega a metade esquerda (L) e a metade direita (R)
        L = arr[:mid]
        R = arr[mid:]

        # a  função chama a si mesma pra continuar cortando as metades
        merge_sort(L)
        merge_sort(R)

        # Três apontadores. 'i' vai rastrear a esquerda, 'j' a direita e 'k' a lista principal (arr)
        i = j = k = 0
        

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Esse laço varre as sobras da esquerda...
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # ...e esse aqui varre as sobras da direita.
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr

def quick_sort(arr):
    # Se a lista tiver 1 ou nenhum item, ela já tá ordenada, vida que segue.
    if len(arr) <= 1:
        return arr
        
    # Escolhemos o cara do meio pra ser o "Pivô" da balança.
    pivot = arr[len(arr) // 2]
    
    # Aqui a gente usa um recurso do Python chamado List Comprehension.
    # Em vez de fazer um monte de 'for' e 'if', a gente cria três listas novas de uma vez:
    left = [x for x in arr if x < pivot]    # A galera menor que o pivô vai pra esquerda
    middle = [x for x in arr if x == pivot] # Quem é igual ao pivô fica no meio
    right = [x for x in arr if x > pivot]   # E os grandalhões vão pra direita
    
    # Agora a gente junta as três partes. Note que chamamos o quick_sort de novo pra esquerda e direita.
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    # Função auxiliar do Heap. Basicamente ela olha pra um nó da árvore (i) e garante 
    # que ele seja maior que seus dois filhos.
    largest = i          
    l = 2 * i + 1        
    r = 2 * i + 2       

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

   
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # ...e chama a função de novo pro novo nó pra garantir que não quebrou nada lá pra baixo
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Primeiro a gente bagunça a lista de um jeito estruturado, criando o Max-Heap.
    # Pense nisso como uma pirâmide onde o maior número sempre fica no topo (índice 0).
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # Agora a gente vai arrancando os números grandes do topo, um por um.
    for i in range(n - 1, 0, -1):
        # Tira o rei do topo (arr[0]) e joga ele pro final da lista (que é o lugar dele na ordem crescente)
        arr[i], arr[0] = arr[0], arr[i]
        # Como colocamos um plebeu lá no topo, a gente chama o heapify pra árvore se reorganizar e eleger o novo rei
        heapify(arr, i, 0)
        
    return arr


# ==========================================
# OS FORA DA CURVA: ALGORITMOS LINEARES O(N)
# ==========================================

def counting_sort(arr):

    if not arr: return arr
    max_val = max(arr) # Precisamos saber quem é o maior cara da lista
    
    # Criamos um array de contadores gigante, com o tamanho do maior número da lista
    count = [0] * (max_val + 1) 
    output = [0] * len(arr)     
    
    # Conta os números. Se o número "5" aparecer 3 vezes, count[5] vai valer 3.
    for num in arr:
        count[num] += 1
        
    # Soma cumulativa. Isso aqui serve pra gente saber a posição EXATA em que cada número vai ficar no final.
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Monta a lista final lendo de trás pra frente. Isso é importante pra manter a "estabilidade" 
    # (ou seja, se tinham dois números '5' repetidos, eles mantêm a ordem de chegada).
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        
    # Devolve tudo pra lista original
    for i in range(len(arr)):
        arr[i] = output[i]
        
    return arr

def counting_sort_for_radix(arr, exp):
  
    n = len(arr)
    output = [0] * n
    count = [0] * 10 # Só vai de 0 a 9 porque a gente tá lidando com base 10 (os dígitos decimais)

    # A  matemática aqui '(arr[i] // exp) % 10' serve pra pescar só um dígito específico.
    # se o número for 456 e o exp for 10 (casa da dezena), essa fórmula extrai o "5".
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr) 
    exp = 1 # Começamos olhando pras unidades
    
    # O Radix ordena os números rodada por rodada: primeiro as unidades, depois as dezenas, centenas...
    # Ele para quando a divisão inteira do maior número der 0.
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
        
    return arr

def bucket_sort(arr):
    # Como o nome diz, a gente vai jogar os dados em baldes.
    if len(arr) == 0: return arr
    min_val, max_val = min(arr), max(arr)
    
    # Quantos baldes eu preciso? Uma boa regra é pegar o tamanho da lista e dividir por 10.
    bucket_count = max(1, len(arr) // 10)
    buckets = [[] for _ in range(bucket_count)] # Cria um monte de listas vazias
    
    # Hora de distribuir a galera. Números pequenos vão pros primeiros baldes, números grandes vão pros últimos.
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1) * bucket_count)
        if index == bucket_count: 
            index -= 1 # Pra não dar erro no balde do último índice
        buckets[index].append(num)
        
    arr.clear()
    
    # Agora que todo mundo tá no seu balde, a gente ordena CADA BALDE separadamente.
    for bucket in buckets:
        # Aqui eu usei a função de ordenar nativa do Python pra facilitar a vida,
        # mas daria pra chamar o nosso insertion_sort() aqui dentro por exemplo.
        arr.extend(sorted(bucket)) 
        
    return arr


# ==========================================
# TESTANDO A BRINCADEIRA TODA
# ==========================================

def testar_algoritmo(nome, func, lista_base):
    # A gente precisa clonar a lista com deepcopy! 
    # Se passássemos a lista original, o primeiro algoritmo iria deixá-la ordenadinha. 
    # Aí o segundo algoritmo iria testar uma lista que já estava arrumada, roubando no tempo de teste.
    lista_teste = copy.deepcopy(lista_base)
    
    print(f"Bora testar o {nome}...")
    inicio = time.time() # Solta o cronômetro
    
    # Como nosso Quick Sort retorna uma lista nova (e não altera ela direto na memória), tem esse IF.
    if nome == "Quick Sort":
        lista_teste = func(lista_teste)
    else:
        func(lista_teste)
        
    fim = time.time() # Trava o cronômetro
    print(f"[{nome}] finalizou em {fim - inicio:.5f} segundos.\n")

if __name__ == "__main__":
    print("="*50)
    print("GERANDO DADOS DE TESTE...")
    # Criando um monstrinho de 100 mil números entre 1 e 1 milhão.
    lista_100k = [random.randint(1, 1000000) for _ in range(100000)]
    print("Pronto, 100.000 itens na lista!")
    print("="*50 + "\n")
    
    print("--- VAMOS COMEÇAR PELOS BONS (Os algoritmos rápidos) ---")
    # Esses aqui dão conta do recado rapidinho.
    testar_algoritmo("Merge Sort", merge_sort, lista_100k)
    testar_algoritmo("Quick Sort", quick_sort, lista_100k)
    testar_algoritmo("Heap Sort", heap_sort, lista_100k)
    testar_algoritmo("Counting Sort", counting_sort, lista_100k)
    testar_algoritmo("Radix Sort", radix_sort, lista_100k)
    testar_algoritmo("Bucket Sort", bucket_sort, lista_100k)
    
    print("="*50)
    print("--- AGORA OS LENTOS (O(N²)) ---")
    print("Atenção: AQUI SÃO OS 100K, vai demorar mds")
    print("Os próximos algoritmos podem levar BASTANTE tempo (até horas dependendo do PC).")
    print("Já tô fazendo um café, o terminal vai ficar 'pensando'...")
    print("="*50 + "\n")
    
    # Agora sim, forçando os algoritmos lentos a processarem toda a lista de 100K!
    testar_algoritmo("Selection Sort", selection_sort, lista_100k)
    testar_algoritmo("Bubble Sort", bubble_sort, lista_100k)
    testar_algoritmo("Insertion Sort", insertion_sort, lista_100k)
