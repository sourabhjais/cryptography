import numpy as np
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' '

def parsing(matrix):
    tup=np.shape(matrix)
    string=""
    for i in range(tup[1]):
        for j in range(tup[0]):
            string+=chr(matrix[j][i]+97)
    return string

def cipher_text(key):
    key_list=sorted(list(key))
    order=[key_list.index(i)+1 for i in key]
    secret_key=np.zeros((len(key),len(key)),dtype="int")
    for i in range(len(order)):
        secret_key[order[i]-1][i]=1
    return secret_key
    
def reshaping(string,key):
    list1=list(string)
    list2=[ord(list1[i])-97 for i in range(len(list1))]
    return np.array(list2).reshape(int(len(list1)/len(key)),len(key))
    
def string_modify(string,key):
    strings=""
    for ch in string:
        if ch not in punctuations:
            strings+=ch
    k=len(strings)%len(key)       
    if k!=0:
        for i in range(len(key)-k):
            strings+='z'
    return strings

def encryption(string,key):
    string=string_modify(string,key)
    matrix=reshaping(string,key)
    key_matrix=cipher_text(key)
    transposition=matrix.dot(key_matrix)
    middle_text=parsing(transposition)
    print(middle_text)
    
file=open("3.txt",'r')
string=file.read().lower()
key="SWINDON"
encryption(string,key)
