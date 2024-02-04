import hashlib

# możliwe algorytmy haszujące
#print (hashlib.algorithms_available)

# nowa zmienna hash z ustawieniem algorytmu
#ownHash = hashlib.new("sha512")

# przekazanie tekstu do zahashowania
#ownHash.update(b"nwcPadme!")

# wypisanie w formie bajt po bajcie
#print(ownHash.digest())

# wypisanie w formie szesnastkowej
#print(ownHash.hexdigest())

plainText_password = "Moje tajne hasło"
shadow = hashlib.new("sha512")
shadow.update(plainText_password.encode())

password_hash = shadow.hexdigest()

user_input = "Moje tajne hasło"
input_hash = hashlib.new("sha512")
input_hash.update(user_input.encode())
input_hash = input_hash.hexdigest()

print(password_hash)
print(input_hash)
