#!/usr/bin/env python
# coding: utf-8

# In[26]:


import string


def changetocipher(shift=10):
  char=" "+string.digits+string.ascii_letters+string.punctuation

  shiftedchar=char[30:]+char[:30]

  return str.maketrans(char,shiftedchar),str.maketrans(shiftedchar,char)

def encrypt(text,cipher):
  return text.translate(cipher)

def decrypt(text,decipher):
  return text.translate(decipher)

def main():
    print("<Wlcome to Encrption>")


    database={}

    while True:


        cipher,decipher=changetocipher()


        checker=input("Want to Encrypy or Decrypt(E/D):").upper()
        if checker=="E":
          text=input("Enter the Text:")
          encryptedtext=encrypt(text,cipher)
          if text=="":
            break
          if text in database:
            print(f"The Original Text:{text}")
            print(f"The Encrypted Text:{database[text]}")
          else:
            print(f"The Original Text:{text}")
            print(f"The Encrypted Text:{encryptedtext}")
            database[text]=encryptedtext
        elif checker=="D":
          text=input(f"Enter the Text You want to Decrypt:")


          print(f"The Decrypted Text:{decrypt(text,decipher)}")

        else:
          print("Invalid Input")




        print(database)
if __name__=="__main__":
     main()


