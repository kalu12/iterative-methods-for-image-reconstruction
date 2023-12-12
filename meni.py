import subprocess

def run_script(script_path):
    try:
        subprocess.run(['python', script_path])
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("Menu:")
        print("1. Run Script 1")
        print("2. Run Script 2")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            run_script('mnk.py')
        elif choice == '2':
            run_script('/path/to/script2.py')
        elif choice == '3':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()