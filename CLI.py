#Library to call bash (shell) scripts.
import subprocess

def command_line(): #Computer updates

    #User password setup
    passwd = input("Enter your provisional usr passwd: ")
    passwd = int(passwd)

    while True: #Loop

        #Control of the loop to update the computer
        print("Choose one of the commands available: \
        1. apt update \
        2. apt upgrade \
        3. exit")
        command = str(input("root@terminal_pc:~$ ")).lower()

        if command == "apt update": #First command
            print("This cmd requires sudo privileges, type sudo before it to use it: ")
            command = str(input("root@terminal_pc:~$ ")).lower()
            sudo = int(input("Enter your root password: "))

            #Conditioning the commands
            if command == "sudo apt update" and sudo == passwd:
                subprocess.call(['bash', '/home/kvelez07/Downloads/commands.sh'])
            else:
                print("Invalid root authentication.")

        elif command == "apt upgrade": #Second command
            print("This cmd requires sudo privileges, type sudo before it to use it: ")
            command = str(input("root@terminal_pc:~$ ")).lower()
            sudo = int(input("Enter your root password: "))

            #Conditioning the commands
            if command == "sudo apt upgrade" and sudo == passwd:
                subprocess.call(['bash', '/home/kvelez07/Downloads/commands2.sh'])
            else:
                print("Invalid root authentication.")

        elif command == "apt update && apt upgrade": #Complete alternative
            print("This cmd requires sudo privileges, type sudo before it to use it: ")
            command = str(input("root@terminal_pc:~$ ")).lower()
            sudo = int(input("Enter your root password: "))

            #Conditioning the commands
            if command == "sudo apt update" and sudo == passwd:
                subprocess.call(['bash', '/home/kvelez07/Downloads/commands.sh'])
                subprocess.call(['bash', '/home/kvelez07/Downloads/commands2.sh'])
            else:
                print("Invalid root authentication.")

        elif command == "exit":
            break

        else: #Error checking
            print("Invalid command")
            break

command_line() #Function calling.