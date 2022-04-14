email_to_name = {}
email = input("Email: ")
while email != "":
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    answer = input(f"Is your name {name}? (Y/n) ")
    if answer.upper() != "Y" and answer != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} ({email})")