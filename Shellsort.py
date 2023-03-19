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
