from werkzeug.security import generate_password_hash, check_password_hash

password = "CorrectHorseBatteryStaple"

hashed = generate_password_hash(password)
print("HASH:", hashed)

print("Right password check:", check_password_hash(hashed, "CorrectHorseBatteryStaple"))
print("Wrong password check:", check_password_hash(hashed, "wrong-password"))