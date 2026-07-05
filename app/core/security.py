from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

hashed_password = password_hash.hash("my_password")

print("hasss", hashed_password)

is_verified = password_hash.verify("my_password" , hashed_password);

print("Verified", is_verified)