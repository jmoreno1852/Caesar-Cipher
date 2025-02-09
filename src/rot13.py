#Substitution Cypher 
#In this case I will directly implement ROT13 as its a derivative from Caesar cypher

def rot13(data):
    rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    return data.translate(rot13)
