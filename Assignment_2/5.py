def statistical_attack(cipher_text):
    all_freq = {}  
    for i in cipher_text: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    list1=list(all_freq.keys())
    list2=list(all_freq.values())
    ch=list1[list2.index(max(list2))]
    if ch.isupper():
        k=ord(ch)-65
    else:   
        k=ord(ch)-97 
    if k<4:
        key=26-k
    else:
        key=k-4
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

f=open("file6.txt",'r')
cipher_text=f.read() 
print("PLAIN TEXT:",statistical_attack(cipher_text))
