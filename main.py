#This is project vigenere, started on monday july 29th 2019.
#this program is an encryption program that uses the vigenere square to encrypt
#and decrypt the text, also using a key phrase by sokrates. 
#"true wisdom comes to each of us when we realise how little we understand about life, ourselves and the wold around us"

# encryption: (x) = plaintext char, (y) = key char
# A to (x) = n, e.g A to the letter P is 16 spaces therefore n = 16
# encrypted char = (y) + n therefore T which is the first letter of the key + 16 = I
# encrypted char = I


# decryption: n = count from (y) to encrypted char e.g from T to I is 16 
# n = 16
# decrypted char = A + n therefore A + 16 = P

import sys

def main():
    key = """true wisdom comes to each of us when we realise how little we understand about life ourselves and the world around us"""

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    key = key.replace(" ","".lower())
   
   #if there are no args given
    if(len(sys.argv) == 1):
        print("There needs to be an inline command -e for encrypt or -d to decrypt")
    elif(sys.argv[1] == "-e"):
        txt = input("type in the sentence that you want to encrypt:\n").lower()
        #producing the encrypted text
        encrypt(txt,key,alphabet)
    elif(sys.argv[1] == "-d"):
        #decrypting text
        enc = input("Type in the sentence you want to decrypt:\n").lower()
        decrypt(enc, key,alphabet)
def encrypt(text,key, alph=[]):
    #storing the distance of plain char from A 
    position = 0
    encryptText = ""
    keypos = 0 #this is to keep  track just incase plain text length > key text length

    #checking that text is less than key
    if(True):
            #looping through plain char
            for i in range(len(text)):
                #making sure that the encryption only happens to letters
                if(text[i] != " "):
                    #finding the distance between a and plain char
                    for n in range(len(alph)):
                        if(text[i] == alph[n]):
                            position = n

                    #getting key char and adding position to it
                    #to get encrypted char
                    for n in range(len(alph)):
                        if(key[keypos] == alph[n]):
                            #print("n before position: ", n);
                            #this is the key char position + distance between A to plain char
                            n += position
                            #print("this is n: ", n)
                            #if reaching out of range in the alphabet, reset to the beginning
                            if(n >= 26):
                                n = n - 26
                                encryptText = encryptText + alph[n]
                            else:
                                encryptText = encryptText + alph[n]
    
                    #looping through the key if we reach the end of it
                    if(keypos < len(key)-1):
                        keypos += 1
                    else:
                        keypos = 0
                #adding space to the text        
                else:
                    encryptText = encryptText + " "
                
    
    print("The encrypted text: ",encryptText)

#etext - encrypted text
#key - the key to encrypt and decrypt
#alph -the english alphabet
def decrypt(etext, key, alph=[]):
    keypos = 0 #storing the key position 
    decryptedText = "" #storing the combined text 
    distance = 0 #the distance between key char and encrypted char

    #loop through encrypted text
    for i in range(len(etext)):
        if(etext[i] != " "):
            #looping through alphabet
            for n in range(len(alph)):
                #getting the key position and alphabet position 
                if(key[keypos] == alph[n]):
                    #looping from key position to encrypted letter position
                    while(alph[n] != etext[i]):
                        #print(alph[n], etext[i])
                        distance += 1
                        n +=1
                        #when reaching the end of the alphabet
                        if(n == 26):
                            n = 0
                    #adding decrypted letter to string
                    decryptedText += alph[distance];
                    #resetting distance
                    distance = 0
             
            #looping through the key if we reach the end of it
            if(keypos < len(key)-1):
                keypos += 1
            else:
                keypos = 0
        else:
            decryptedText = decryptedText + " "

    print("Decrypted Text: ", decryptedText)
    

main()
