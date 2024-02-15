import random
print("Hola mundo")


password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int( input("Escribe la longitud de la contraseña:") )

generada = ""

for i in range(long):
    generada += random.choice(password)

print(generada)

   

#for i in range(long):
#   x = random.randint(0, len(password)-1)
#   generada += password[x]
