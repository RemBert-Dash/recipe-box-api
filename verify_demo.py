from app import hash_password, verify_password

plain = "CorrectHorseBatteryStaple"
stored = hash_password(plain)
print("HASH:", stored)

print("Right password check:", verify_password(stored, "CorrectHorseBatteryStaple"))
print("Wrong password check:", verify_password(stored, "wrong-password"))