import os

file = input("Fayl nomini kiriting: ")

if os.path.exists(file) :
    print("Fayl mavjud!")
    
else : 
    print("Fayl topilmadi!")