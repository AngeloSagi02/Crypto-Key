from cryptography.fernet import Fernet

def encrypto():                                         #Encrypting of the file
    fname = input("File name + Extension: ")
    #fname + "encrypted"                                #If you comment on this statement, it overwrites the file (ADD "+ encrypted" LINE 14)
    fkey = input("Please input your key: ")
    cipher = Fernet(fkey)

    with open(fname,'rb')as f:
        e_file = f.read()                               #Read the file

    encrypted_file = cipher.encrypt(e_file)             #Encrypting of the file

    with open(fname,'wb') as ef:          
        ef.write(encrypted_file)                        #Writing

def decrypto ():                                        #Decrypting of the file
    fname = input("File name + Extension: ")
    #fname + "decrypted"                                #If you comment on this statement, it overwrites the file  (ADD "+ decrypted" LINE 29)                      
    fkey = input("Enter your key: ")
    cipher = Fernet(fkey)

    with open(fname,'rb') as df:    
        encrypted_data = df.read()                      #Read the file


    decrypted_file = cipher.decrypt(encrypted_data)     #Decrypting

    with open(fname,'wb') as df:
        df.write(decrypted_file)                        #Writing

def gen_key():
    key = Fernet.generate_key()
    print("Key Generetion (copy all without \"   b''    \"): \n\n", key, "\n")

print("\n\nHi, welcome to the en/de crypting program.\nWhat do you want to do?\n")

c = None
while c != 0:
    c = input("0 - Exit \n1 - Encrypting \n2 - Decrypting\n3 - Generation Key\n\n")

    if c == "1":
        encrypto()
    elif c == "2":
        decrypto()
    elif c == "3":
        gen_key()
    elif c == "0":
        break
    else:
        print("Invalide choice")
    
