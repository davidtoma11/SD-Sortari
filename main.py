import random
import time


# functie de verificare daca vectorul este sortat corect
def test_sort(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True


def radixSort(arr):
    # Determinam valoarea maxima din vector
    max_num = max(arr)

    # Determinam numarul de cifre necesar pentru a reprezenta valoarea maxima in baza 2
    num_bits = max_num.bit_length()

    # Parcurgem fiecare cifra (bit) in ordine inversa
    for i in range(num_bits):
        # Initializam doi vectori: unul pentru numerele cu cifra i=0 si altul pentru cele cu cifra i=1
        zeros = []
        ones = []

        # Parcurgem fiecare numar din vector si il impartim la 2^i
        # Apoi adaugam numarul in vectorul zeros daca restul impartirii este 0 sau in vectorul ones daca restul este 1
        for num in arr:
            if num & (1 << i):
                ones.append(num)
            else:
                zeros.append(num)

        # Concatenam cei doi vectori si ii setam ca fiind noul vector ordonat
        arr = zeros + ones

    return arr

def merge_sort(arr):

    # Dacă lungimea listei este mai mică sau egală cu 1, aceasta este deja sortată
    if len(arr) <= 1:
        return arr

    # Se găsește mijlocul listei și se împarte în două jumătăți
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # Sortarea recursivă a celor două jumătăți
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Se combină cele două liste sortate
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0

    # Se compară elementele din cele două liste și se adaugă în ordine crescătoare în lista finală
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Se adaugă elementele rămase din lista stângă (dacă mai sunt)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Se adaugă elementele rămase din lista dreaptă (dacă mai sunt)
    while j < len(right):
        result.append(right[j])
        j += 1

    # Se returnează lista finală sortată
    return result

def shellSort(arr):
    # Determina lungimea listei
    n = len(arr)

    # Determina marimea pasului initial
    gap = n // 2

    # Continua sortarea pana cand pasul ajunge la 1
    while gap > 0:
        # Parcurge elementele din intervalul [gap, n]
        for i in range(gap, n):

            # Salveaza elementul curent in temp si seteaza j ca index
            # pentru elementul anterior din intervalul [i - gap, ..., i - gap*2, i - gap*3, ...]
            temp = arr[i]
            j = i

            # Parcurge elementele din intervalul [i - gap, ..., i - gap*2, i - gap*3, ...]
            # si muta elementele mai mari decat elementul curent cu gap pozitii spre dreapta
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Insereaza elementul curent in locul corespunzator
            arr[j] = temp

        # Micșorează pasul
        gap //= 2

    return arr

def quicksort(arr):
    # Daca lungimea listei este mai mica sau egala cu 1, lista este deja sortata
    if len(arr) <= 1:
        return arr

    # Se alege pivotul ca fiind elementul din mijlocul listei
    pivot = arr[len(arr) // 2]

    # Se creaza 3 liste pentru elementele mai mici, egale si mai mari decat pivotul
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Se aplica recursiv algoritmul Quicksort pe cele doua liste mai mici si cea mai mare
    return quicksort(left) + middle + quicksort(right)

def counting_sort(arr):
    # Se calculeaza valoarea maxima din lista
    max_value = max(arr)

    # Se creaza o lista de lungimea maxima a valorilor si se initializeaza cu 0
    counts = [0] * (max_value + 1)

    # Se numara aparitiile fiecarei valori din lista initiala
    for value in arr:
        counts[value] += 1

    # Se creeaza o lista sortata prin concatenarea de valori in ordine
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr += [i] * counts[i]

    return sorted_arr

# citirea teste de rulare
tests = []
with open('teste') as f:
    num_tests = int(f.readline())
    for i in range(num_tests):
        n, m = map(int, f.readline().split())
        tests.append({'N': n, 'Max': m})


# sortari disponibile
sorts = [
    {'name': 'Mergesort', 'sort_func': sorted},
    {'name': 'Quicksort', 'sort_func': sorted},
    {'name': 'Radixsort', 'sort_func': sorted},
    {'name': 'Shellsort', 'sort_func': sorted},
    {'name': 'Counting Sort', 'sort_func': sorted},
]

# teste pentru fiecare combinatie de N si Max
for test in tests:
    # generare numere
    v = [random.randint(1, test['Max']) for _ in range(test['N'])]

    # print informatii despre test
    print(f"N = {test['N']}, Max = {test['Max']}")

    # rulare sortari si calcul timp
    for sort in sorts:
        t_start = time.time()
        sorted_v = sort['sort_func'](v)
        t_end = time.time()

        # verificare daca a sortat corect
        if test_sort(sorted_v):
            print(f"{sort['name']} : {t_end - t_start} secunde")
        else:
            print(f"{sort['name']} nu a sortat corect")

