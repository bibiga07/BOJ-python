while True:
    a = input()
    oct = []
    c = 0
    d = 0 
    
    if a == '#':
        break
    else:
        for i in range(len(a)):
            if a[i] == '-':
                b = 0
            elif a[i] == '\\':
                b = 1
            elif a[i] == '(':
                b = 2
            elif a[i] == '@':
                b = 3
            elif a[i] == '?':
                b = 4
            elif a[i] == '>':
                b = 5
            elif a[i] == '&':
                b = 6
            elif a[i] == '%':
                b = 7
            elif a[i] == '/':
                b = -1
            else:
                break
            oct.append(b)
        
        for q in range(len(oct)-1, -1, -1):
            if q == 0:
                c += oct[-1]
            else:
                c += oct[d] * (8 ** q)
                d += 1
        print(c)