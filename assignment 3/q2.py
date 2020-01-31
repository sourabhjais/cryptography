import numpy as np
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' '

def search(ch,secret_key):
    tup=np.where(secret_key==ch)
    k=list(zip(tup[0],tup[1]))
    return k

def string_modify(string):
    for i in range(0,len(string)-1):
        if string[i]==string[i+1]:
            if string[i]!='x':
                string=string[:i+1]+'x'+string[i+1:]
            else:
                string=string[:i+1]+'y'+string[i+1:]
    string1=""                
    for i in range(0,len(string)):
        if string[i] not in punctuations: 
               string1=string1+string[i]              
    if len(string1)%2!=0:
        string1+='x'
        
    return string1  

def playfair_cipher(secret_key,string):
    string_list = [(string[i:i+2]) for i in range(0, len(string), 2)] 
    print(string_list)
    new_string=""
    for ch in string_list:
        if ch[0]=='j':
            ch[0]='i'
        if ch[1]=='j':
            ch[1]='i'
        tup1=search(ch[0],secret_key)
        x1,y1=tup1[0][0],tup1[0][1]
        tup2=search(ch[1],secret_key)
        x2,y2=tup2[0][0],tup2[0][1]
        if y1==y2:
            new_string+=secret_key[(x1+1)%5][y1]+secret_key[(x2+1)%5][y2]            
        elif x1==x2:
            new_string+=secret_key[x1][(y1+1)%5]+secret_key[x2][(y2+1)%5]
        else:
            new_string+=secret_key[x1][y2]+secret_key[x2][y1]
    return new_string

def create_key(string):
    secret_key=['l','g','d','b','a','q','m','h','e','c','u','r','n','i','f','x','v','s','o','k','z','y','w','t','p']
    update_key=[string[0]]
    for ch in string[1:]:
        if ch not in update_key:
            update_key.append(ch)
    for ch in secret_key:
        if ch not in update_key:
            update_key.append(ch)
    return update_key

key="commonlounge"
secret_key=create_key(key)
secret_key=np.array(secret_key).reshape(5,5)
file=open("file2.txt",'r')
string=file.read().lower()
string=string_modify(string)
print(string)
print("CIPHER TEXT:",playfair_cipher(secret_key,string))
