def longest_common_subsequence(name1, name2):
    m = len(name1)
    n = len(name2)

    lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if name1[i - 1] == name2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

    lcs = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if name1[i - 1] == name2[j - 1]:
            lcs = name1[i - 1] + lcs
            i -= 1
            j -= 1
        elif lcs_matrix[i - 1][j] > lcs_matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


name1 = input()
name2 = input()

lcs = longest_common_subsequence(name1, name2)

print(lcs)
