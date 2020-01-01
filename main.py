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

#this is the latest output from either encyrpting or decrypting 
latestText = " "

def main():
    options()
  
#the command line arguments options
def options():
    
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
   
   #if there are no option given
    if(len(sys.argv) == 1):
        print("There needs to be an inline command\n -e for encrypt\n -d to decrypt\n -k followed by a number to select a specific key")

    userOptions = []

    for options in sys.argv[1:]:
        userOptions.append(options)
        
    if("-k" in userOptions):
        #getting position
        x = userOptions.index('-k')
        #getting the next value
        x += 1
        
        #if the choice is greater than the keys.txt line count
        if(int(userOptions[x]) >= linesCount()):
            print("the number you have selected has no line in text file, going to default")
            choice = 1
        else: #storing the choice to then get the key
            choice = userOptions[x]
    else:
        choice = 1

    #using the value to get the key from the textfile
    key = keys(int(choice))
    #removing undeccasery spaces and case's
    key = key.replace(" ","".lower())

    if("-e" in userOptions):
        txt = input("type in the sentence that you want to encrypt:\n").lower()
        #producing the encrypted text
        encrypt(txt,key,alphabet)

    if("-d" in userOptions):
        #decrypting text
        enc = input("Type in the sentence you want to decrypt:\n").lower()
        decrypt(enc, key,alphabet)

    if("-i" in userOptions):
        #getting position of the file name
        x = userOptions.index('-i')
        x += 1
        #storing the text from the file into txt
        txt = ReadFile(userOptions[x])

        #encrypting the text
        encrypt(txt,key,alphabet)

    if("-id" in userOptions):
        #getting psoition of the file name
        x = userOptions.index('-id')
        x += 1
        #storing the text from the file into txt
        txt = ReadFile(userOptions[x])

        #decrypt the text
        decrypt(txt,key,alphabet)

    if("-o" in userOptions):
        #getting position of the file name
        x = userOptions.index('-o')
        x += 1
        if(latestText != " "):
            SaveToFile(latestText,userOptions[x])
        else:
            print("Nothing to save into the file\n Aborting process")


    


def encrypt(text,key, alph=[]):
    #so i can store the final result
    global latestText

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
                
    latestText = encryptText
    print("The encrypted text: ",encryptText)

#etext - encrypted text
#key - the key to encrypt and decrypt
#alph -the english alphabet
def decrypt(etext, key, alph=[]):
    #so i can store the final result 
    global latestText

    #storing the distance of plain char from A
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

    latestText = decryptedText 
    print("Decrypted Text: ", decryptedText)

#counts how many lines are in keys.txt and returns them
def linesCount():
    cnt = 1
    with open('keys.txt') as fp:
        for line in fp:
            cnt += 1
    return(cnt)
    
#reads the keys file and returns a specific key string based on choice
def keys(choice):
    filepath = 'keys.txt'
    cnt = 1
    #opening file
    with open(filepath) as fp:
        #reading each line
        for line in fp:
            #returning the specific key that the user choice
            if(cnt == choice):
                return(line.strip())
            cnt += 1
            
        
#function to read and return a string of the file contents
def ReadFile(filename):
    #the text in the file
    file_text = ""

    with open(filename) as fp:
        #read each line
        for line in fp:
            file_text += line
    print("This is the content: ",file_text)
    #return the content
    return(file_text)

#saving the encrypted text to a specified text file
def SaveToFile(content, filename):
    #opening file
    savefile = open(filename, 'w')

    #saving the encrypted text to file
    savefile.write(content)
    savefile.close()

main()
