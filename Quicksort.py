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
