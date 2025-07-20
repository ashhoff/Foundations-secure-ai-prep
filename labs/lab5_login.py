users = {"admin":"pass123"}
username = input("Username: ")
password = input("Password: ")
if username in users and users[username] == password:
    print("Access Granted!")
else:
    print("Access Denied!")