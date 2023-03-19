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
