# -*- coding: utf-8 -*-

while True:
    input_ = [int(x) for x in input().split()]

    if not input_ or input_[0] == 0:
        break
    
    n = input_[0]

    values = input_.copy()[1:] + [-1]

    compare_values = []
    qtt_values = n

    for i, v in enumerate(values):
        if values[i + 1] == -1:
            break
        
        abs_value = abs(v - values[i + 1])
        
        compare_values.append(abs_value)

    if all([compare_values.count(x) == 1 for x in range(1, n)]):
        print("Jolly")
    else:
        print("Not jolly")
