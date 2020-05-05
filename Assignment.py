print("Hello User!")
email = input("Enter your email address: ")

split = email.split('@')
print(split)

username = split[0]
domain = split[1]

print("Your username is", username, "and your domain is", domain)