from cryptography.fernet import Fernet

'''

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() 

b'hello ' & 'hello' both are different things forst one is byte string and we don't want to do that 

'''

def load_key():
    file = open("key.key", "rb") #rb read /bite
    key = file.read()
    file.close()
    return key


key = load_key()  # encode string ko leta hai and bits me convert kar deta hai 
fer = Fernet(key)






def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data =   line.rstrip() #r me next line  mode inc. hota hai toh bass usko hi strip off karnae ke liye 
            user , passw = data.split("|")
            print("User: " ,user,"| Password:" ,fer.decrypt(passw.encode()).decode())
    
    

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open("passwords.txt", 'a') as f: # with open and close apne app hi kar deta hai apko manually nahi karan padta w= write , a = append new file created and read the file and r mode reading mode 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#for encription we install a module through terminal (command = pip install cryptography )but you need to install the pythin first         



 



while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add), press Q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue