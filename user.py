import json
import hashlib
import validations
import os.path
import projects


class User:
    def __init__(self, firstName, lastName, email, Password, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = Password
        self.phone = phone


def hashPassword(pwd):
    """Hash a password using SHA-256 algorithm"""
    pwd_bytes = pwd.encode("utf-8")
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd


def register():
    fname = input("Enter your first name : ")
    if not validations.validateStrings(fname):
        print("Invalid frist name")
        return
    lname = input("Enter your last name : ")
    if not validations.validateStrings(lname):
        print("Invalid last name")
        return
    email = input("Enter your email : ")
    if not validations.validateEmail(email):
        print("Invalid email")
        return
    if validations.userExist(email):
        print("Email already exists. Please choose a different email.")
        return
    phone = input("Enter your phone : ")
    if not validations.validatePhone(phone):
        print("Invalid phone number")
        return
    password = input("Enter your pawssword : ")
    validation, mess = validations.validatePassword(password)
    if not validation:
        print(mess)
        return
    confirmPassword = input("Enter your confirm pawssword : ")
    if password != confirmPassword:
        print("password not equal confirm password")
        return
    hashedPassword = hashPassword(password)
    newUser = User(fname, lname, email, hashedPassword, phone)
    userData = {
        "firstName": newUser.firstName,
        "lastName": newUser.lastName,
        "email": newUser.email,
        "password": newUser.password,
        "phone": newUser.phone,
    }
    file_path = "userData.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = {"userData": []}

    data["userData"].append(userData)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("User registered successfully!")


def login():
    flag = 0
    email = input("Enter email: ")
    password = input("Enter password: ")
    auth = password.encode()
    authHash = hashlib.sha256(auth).hexdigest()
    with open("userData.json", "r") as f:
        data = json.load(f)
    for user in data["userData"]:
        if user["email"] == email and user["password"] == authHash:
            flag = 1
            break
    if flag != 1:
        print("Login failed!")
        return
    while True:
        print(
            " 1. See all projects \n 2. Add project \n 3. Edit project \n 4. Delete project \n 5. Exit"
        )
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                print("all Projects")
                projects.getAll()

            elif choice == "2":
                print("Add projects")
                projects.addProject(email)
            elif choice == "3":
                print("Edit project ")
                projects.editProject(email)
            elif choice == "4":
                print("Delete project ")
                projects.deleteProject(email)
            elif choice == "5":
                print("Bye Bye ")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")
