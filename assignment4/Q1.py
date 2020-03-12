import numpy as np

def reshaping(list1,key):
    return np.array(list1).reshape(int(len(list1)/5),len(key))

def create_key(string):
    list1=[]
    for ch in string:
        list1.append(ord(ch)-97)
    return list1

def parsing(matrix):
    tup=np.shape(matrix)
    string=""
    for i in range(tup[1]):
        for j in range(tup[0]):
            string+=chr(matrix[j][i]+97)
    return string
    
def string_modify(str1):
    string=""
    for ch in str1:
        if ch!=" ":
            string+=ch
    rem=len(string)%5      
    if rem!=0:
        for i in range(5-rem):
            string+='z'
    return create_key(string)    

def cipher_text(plain_text,key):
    secret_key=np.zeros((len(key),len(key)),dtype="int")
    for i in range(len(key)):
        secret_key[int(key[i])-1][i]=1
    first_transposition=plain_text.dot(secret_key)
    middle_text=parsing(first_transposition)
    print("After first transposition:",middle_text)
    list1=create_key(middle_text)
    middle_plain_text=reshaping(list1,key)
    second_transposition=middle_plain_text.dot(secret_key)
    cipher_text=parsing(second_transposition)
    print("After second transposition:",cipher_text)
     

    
key="31452"
plain_text=[]
file=open("q1.txt",'r')
string=file.read().lower()
list1=string_modify(string)
plain_text=reshaping(list1,key)
cipher_text(plain_text,key)
