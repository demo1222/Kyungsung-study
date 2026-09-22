
import os, platform
def show_menu():
    print("\n--- My OS Tool ---") 
    print("1. Show OS info")
    print("2. List files here")
    print("3. Create a file")
    print("4. Show my process ID")
    print("5. Quit")
    while True:
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            print("OS:", platform.system(), platform.release()) 
            print("Machine:", platform.node())
        elif choice == "2":
            print("Files:", os.listdir("."))
        elif choice == "3":
            name = input("File name: ").strip()
            with open(name, "w") as f:
                f.write("created\n")
            print("Created:", name)
        elif choice == "4":
            print("My PID: ", os.getpid())
        elif choice == "5":
            print("Zarylbek is done with this experiment!")
            break
        else:
            print("Invalid choice.")

show_menu()