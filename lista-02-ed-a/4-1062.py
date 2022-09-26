# -*- coding: utf-8 -*-


while True:
    n_vagoes = int(input())
    
    if n_vagoes == 0:
        break
    
    while True:
        trem = [int(x) for x in input().split()]
        
        if trem[0] == 0:
            break
        
        b = []
        e = []
        
        v = trem.pop()
        
        b.insert(0, v)
        
        if v == n_vagoes:
            while len(trem) > 0:
                max_ = max(trem)
                
                v = trem.pop()
                
                try:
                    if e[0] == b[0] - 1:
                        b.insert(0, e.pop())
                except:
                    pass
                
                if v == max_:
                    b.insert(0, v)
                else:
                    e.insert(0, v)
            
            if b == [x for x in range(1, n_vagoes + 1)]:
                print("Yes")
            else:
                print("No")
                
        elif v == 1:
            while len(trem) > 0:
                min_ = min(trem)
                
                v = trem.pop()
                
                try:
                    if e[0] == b[0] + 1:
                        b.insert(0, e.pop())
                except:
                    pass
                
                if v == min_:
                    b.insert(0, v)
                else:
                    e.insert(0, v)
            
            if b == [x for x in range(n_vagoes, 0, -1)]:
                print("Yes")
            else:
                print("No")
            
        else:
            print("No")
        
    print()
