def xor(a,b):
    if a==b:
        return 0
    else:
        return 1
    
def key_stream(seed,epoch):
    string=list(seed)
    string.insert(0,str(xor(int(seed[-2]),int(seed[-1]))))
    key=""
    for i in range(epoch):
        key+=string[-1]
        for j in range(1,len(seed)+1):
            string[-j]=string[-j-1]
        string[0]=str(xor(int(string[-2]),int(string[-1])))
    return key[:2**len(seed)-1]
    

seed=['0','0','0','1']
epoch=20
print(key_stream(seed,epoch))
