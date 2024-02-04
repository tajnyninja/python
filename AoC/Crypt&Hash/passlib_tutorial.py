# passlib learn
# Kacper
# use this to install passlib: pip install passlib

from passlib.hash import sha512_crypt

password = "Tajne hasło!"   # Twpje hasełko
salt = "somesalt"  # Wybrana sól

# Wygeneruj hash hasła z liczbą cykli 5000 i ustaloną solą
hashed_password = sha512_crypt.using(rounds=5000, salt=salt).hash(password)

print(hashed_password)