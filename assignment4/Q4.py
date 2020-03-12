def shift_left(P1,P2,modulus):
    terms=len(P1)-P1.index('1')
    result="00000000"
    reduction=0
    if(P2[0]=='1'):
            reduction=1
    for i in range(terms-1):
        P2=P2[1:]+'0'
        if reduction==1:
            P2=int(P2,2)^int(modulus,2)
            P2='{0:b}'.format(P2)
            while len(P2)!=8:
                P2='0'+ P2
            reduction=0
        print(P2)    
        if P1[-i-2]=='1':
            result=int(P2,2)^int(result,2)
            result='{0:b}'.format(result)
        if(P2[0]=='1'):
            reduction=1    
    while len(result)!=8:
        result='0'+result
    return result
P1="000100110"
P2="10011110"
modulus="100011011"
modulus=modulus[1:]
print(shift_left(P1,P2,modulus))
