# Szymon Fica 337307
# list 3 task 1

import collections

def f(s): 
    de, mlen = collections.deque(), 0
    for i in range(0, len(s)):
        p, q = i, i
        while p-1 >= 0 and q+1 < len(s) and s[p-1] == s[q+1]:
            p -= 1
            q += 1
        if q - p > 1 and q - p + 1 >= mlen:
            if q - p + 1 == mlen:
                de.append((p, q-p+1))
            else:
                de.clear()
                mlen = q-p+1
                de.append((p, q-p+1))
        if i+1 < len(s) and s[i] == s[i+1]:
            p, q = i, i+1
            while p-1 >= 0 and q+1 < len(s) and s[p-1] == s[q+1]:
                p -= 1
                q += 1
            if q - p > 1 and q - p + 1 >= mlen:
                if q - p + 1 == mlen:
                    de.append((p, q-p+1))
                else:
                    de.clear()
                    mlen = q-p+1
                    de.append((p, q-p+1))
    return list(de)

tekst = "acabab"
print(f(tekst))

