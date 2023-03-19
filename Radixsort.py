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
