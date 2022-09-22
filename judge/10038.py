# -*- coding: utf-8 -*-

while True:
    try:
        input_ = [int(x) for x in input().split()]
        n = input_[0]
    except:
        break
    
    values = input_.copy()[1:] + ["0"]
    compare_values = []

    for i, v in enumerate(values):
        if values[i + 1] == "0":
            break
        
        abs_value = abs(v - values[i + 1])
        
        compare_values.append(abs_value)
    
    is_jolly = all([compare_values.count(x) == 1 for x in range(1, n)])

    print("Jolly" if is_jolly else "Not jolly")
