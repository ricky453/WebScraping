a=1
b=1
c=1
while a<5:
    print('a= '+ str(a))
    b=1
    while b<5:
        print('b= '+ str(b))
        c=1
        while c<5:
            print('c= '+ str(c))
            if(c==2):
                print('break')
                break
            c+=1
        b+=1
    a+=1

        