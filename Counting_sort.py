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
