def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def additive_cipher(plain_text,key):
    string=""
    if key>25:
        return 
    for ch in plain_text:
        if ch !=' ':
            if (ch.isupper()):
                C=chr((ord(ch)-65+key)%26+65)
                string+=C
            else:
                C=chr((ord(ch)-97+key)%26+97)
                string+=C
        else:
            string+=ch             
    return  string 

def multiplicative_cipher(plain_text,key):
    string=""
    if key>25 or (gcd(26,key))!=1:
        print("key is not in Z*")
        return 
    for ch in plain_text:
        if ch !=' ':
            if (ch.isupper()):
                C=chr(((ord(ch)-65)*key)%26+65)
                string+=C
            else:
                C=chr(((ord(ch)-97)*key)%26+97)
                string+=C
        else:
            string+=ch             
    return  string 

def affine_cipher(plain_text,key1,key2):
    string=""
    if key2>25 or (gcd(26,key2))!=1:
        print("second key is not in Z*")
        return 
    for ch in plain_text:
        if ch !=' ':
            if (ch.isupper()):
                T=((ord(ch)-65)*key2)%26
                C=chr((T+key1)%26+65)
                string+=C
            else:
                T=((ord(ch)-97)*key2)%26
                C=chr((T+key1)%26+97)
                string+=C
        else:
            string+=ch             
    return  string 

f=open("file1.txt",'r')
plain_text=f.read()
key1=int(input("Enter key: "))
key2=int(input("Enter key: "))
print("CIPHER TEXT IN ADDITIVE: ",additive_cipher(plain_text,key1))
print("CIPHER TEXT IN MULTIPLICATIVE: ",multiplicative_cipher(plain_text,key2))
print("CIPHER TEXT IN AFFINE: ",affine_cipher(plain_text,key1,key2))
