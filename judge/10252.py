# -*- coding: utf-8 -*-

temp = []

while True:
    s1 = list(input())
    s2 = list(input())
    
    if not s1 and not s2:
        break
    
    s1.sort()
    s2.sort()
    
    unique_letters = []
    
    [unique_letters.append(c) for c in s1 if c not in unique_letters]
    
    pos_count_uq_letters = [(i, s2.count(c)) for i, c in enumerate(unique_letters)]
    
    if len(pos_count_uq_letters) == 0:
        print()
        continue
    
    max_ = max(pos_count_uq_letters, key=lambda k: k[1])[1]
    
    sorted_max_uq_letter = sorted(
        [c for c in pos_count_uq_letters if c[1] == max_],
        key=lambda k: k[1]
    )

    resp = "".join([unique_letters[x[0]] for x in sorted_max_uq_letter])

    # print(resp)
    temp.append(resp)

print("\n".join(temp))
