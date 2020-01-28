def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def multiplicative_inverse(a, b):
    for i in range(1, a):
        if (i * b) % a == 1:
            return i
        
def brute_force(cipher_text,key1):
    key=multiplicative_inverse(26,key1)
    string=""    
    for ch in cipher_text:
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
cipher_text=input("Enter cipher text:")
z_star=[1]
for i in range(2,26):
    if gcd(26,i)==1:
        z_star.append(i)
for key in z_star:
    print("PLAIN TEXT FOR KEY ",key," is ",brute_force(cipher_text,key))
