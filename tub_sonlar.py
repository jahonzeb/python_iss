a=int(input('Son kirit:'))
for b in range(a):
    s=0
    for x in range(1,b+1):
        if b%x==0:
            s=s+1
    if s==2:
       print(b)
