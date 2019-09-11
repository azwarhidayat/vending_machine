print ("Vending Machine By Azwar")
print ("Selamat datang yu dipilih yang haus")

print ("air = 2000")
print ("cola = 4000")
print ("Es Teh = 6000") 

money = int(input("Tolong Masukkan Uang Anda "))

if money >= 2000 and money < 4000 :
    print ("kamu memilih air")
    
elif money >= 4000 and money < 6000 :
    print ("Kamu Memilih Cola")

elif money >= 6000:
    print ("Kamu Memilih Es Teh")

else:
    print ("Maaf uang anda kurang. Coba Lagi")
