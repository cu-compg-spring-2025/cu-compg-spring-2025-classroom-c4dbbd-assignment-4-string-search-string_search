def naive_search(T, P):
    occurrences = []
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if T[i + j] != P[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences
