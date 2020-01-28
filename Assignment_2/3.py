def brute_force(cipher_text,key):
    string="" 
    for ch in cipher_text:
        if ch !=' ':
            if (ch.isupper()):
                C=chr((ord(ch)-65-key)%26+65)
                string+=C
            else:
                C=chr((ord(ch)-97-key)%26+97)
                string+=C
        else:
            string+=ch             
    return  string         
cipher_text=input("Enter cipher text:")
for key in range(1,26):
    print("PLAIN TEXT FOR KEY ",key," is ",brute_force(cipher_text,key))
