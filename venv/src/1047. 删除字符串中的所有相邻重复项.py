def removeDuplicates(S):
    i = 0
    while i < len(S) - 1:
        if S[i] == S[i + 1]:
            S = S[:i] + S[i + 2:]
            if i > 0: i -= 1
        else:
            i += 1
    return S

print(removeDuplicates("abbaca"))