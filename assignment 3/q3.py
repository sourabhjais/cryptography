punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' ' 

def vigenere_cipher(string,secret_key):
    cipher_text=""
    for i in range(0,len(string)):
        cipher_text+=chr(((ord(string[i])-97)+(ord(secret_key[i%len(secret_key)])-97))%26+97)
    return cipher_text    

def string_modify(string):
    string1=""                
    for i in range(0,len(string)):
        if string[i] not in punctuations: 
               string1=string1+string[i]     
    return string1
                
file=open("file3.txt",'r')
string=file.read().lower()
key="pascal"
string=string_modify(string)
print(string)
print("CIPHER TEXT:",vigenere_cipher(string,key))
