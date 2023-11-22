for i in range(3):
    H,M,S,h,m,s = map(int,input().split())
    h-=H
    m-=M
    s-=S
    if s < 0:
        s%=60
        m-=1
    if m < 0:
        m%=60
        h-=1
    print(h,m,s)