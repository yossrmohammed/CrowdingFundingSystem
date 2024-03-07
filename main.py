import user

def main():
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                print('Register')
                user.register()
            elif choice == '2':
                print('Login')
                user.login()
            elif choice == '3':
                print('Bye Bye')
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

