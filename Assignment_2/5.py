def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def multiplicative_inverse(a, b):
    for i in range(1, a):
        if (i * b) % a == 1:
            return i
        
def affine_cipher(cipher_text,str1,str2):
    z_star=[1]
    for i in range(2,26):
        if gcd(26,i)==1:
            z_star.append(i)
    list1=[]            
    for key1 in range(1,26):
        for key2 in z_star:
            if str1[0].isupper():
                T1=((ord(str1[0])-65)*key2)%26
                C1=(T1+key1)%26
                T2=((ord(str1[1])-65)*key2)%26
                C2=(T2+key1)%26
                if ((ord(str2[0])-65)==C1) and ((ord(str2[1])-65)==C2):
                    list1=[key1,key2]
            else:
                T1=((ord(str1[0])-97)*key2)%26
                C1=(T1+key1)%26
                T2=((ord(str1[1])-97)*key2)%26
                C2=(T2+key1)%26
                if ((ord(str2[0])-97))==C1 and ((ord(str2[1])-97)==C2):
                    list1=[key1,key2]
    print(list1) 
    key2_inverse=multiplicative_inverse(26, list1[1])
    print(key2_inverse)
    string=""    
    for ch in cipher_text:
        if ch !=' ':
            if (ch.isupper()):
                T=((ord(ch)-65)-list1[0])%26
                C=chr((T*key2_inverse)%26+65)
                string+=C
            else:
                T=((ord(ch)-97)-list1[0])%26
                C=chr((T*key2_inverse)%26+97)
                string+=C
        else:
            string+=ch             
    return  string 
f=open("file5.txt",'r')    
cipher_text=f.read()
print("PLAIN TEXT: ",affine_cipher(cipher_text,"ab","gl"))
