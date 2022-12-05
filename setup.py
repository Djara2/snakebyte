import file_tools as ft
import os_tools as ot
import os

OPERATING_SYSTEM = ot.get_os()
path = ft.get_path()
files = ft.get_directory_files(path)
ot.clear()
if "config.txt" in files:
    print("You already have a config.txt file in your SnakeByte folder.")
    print("Do you wish to create a new default config.txt file?")
    print("━" * len("Do you wish to create a new default config.txt file?"))
    action = input("Create new default config.txt? [y/n]: ")
    if action in ["y", "Y", "yes", "Yes", "YES"]:
        print("SnakeByte needs to know where your music is")
        print("━" * len("SnakeByte needs to know where your music is"))
        location = input("Where is your music? ")
        lines = [
            f"music = {location}"
        ]
        config_file = open("config.txt", "w")
        config_file.writelines('\n'.join(lines))
        config_file.close()
    else:
        print()
        print("SnakeByte needs the pip to work.")
        print("Do you want to try to install pip to your system?")
        print("If you already have pip, entering \"y\" is OK.")
        action = input("Install pip? [y/n]: ")
        
        if action in ["y", "Y", "yes", "Yes", "YES"]:
           os.system("python3 -m install pip")
        else:
            print("If pip is already installed, you are OK")
            print("Otherwise, the setup process going forward will crash")
            print("━" * len("Otherwise, the setup process going forward will crash"))
            input("Press ENTER to acknowledge ")

        print("\nSnakeByte needs the Rich library to work.")
        print("Do you want to try to install Rich to your system?")
        print("If you already have Rich, entering \"y\" is OK.")
        print("━" * len("Do you want to try to install Rich to your system?"))
        action = input("Install Rich? [y/n]: ")
        
        if action in ["y", "Y", "yes", "Yes", "YES"]:
            os.system("python3 -m pip install rich")
        else:
            print("If Rich is already installed, you are OK")
            print("Otherwise, the setup process going forward will crash")
            print("━" * len("Otherwise, the setup process going forward will crash"))
            input("Press ENTER to acknowledge ")
        
        print("\nSnakeByte needs the mpv application to work.")
        print("Do you want to try to install mpv to your system?")
        print("If you already have mpv, entering \"y\" is OK.")
        print("━" * len("Do you want to try to install mpv to your system?"))
        action = input("Install mpv? [y/n]: ")
        
        # Installing mpv
        if action in ["y", "Y", "yes", "Yes", "YES"]:
            # installing mpv for Windows
            if OPERATING_SYSTEM == "Windows":
                print("The best way to automatically install mpv is to use Chocolatey")
                print("━" * len("The best way to automatically install mpv is to use Chocolatey"))
                action = input("Do you have Chocolatey on your system?")
                # if Chocolatey is already installed
                if action in ["y", "Y", "yes", "Yes", "YES"]:
                    os.system("runas /user:Administrator \"cmd.exe /C choco install mpv\"")
                # if Chocolatey is not installed
                else:
                    print("This setup script can install Chocolatey for you automatically.")
                    print("━" * len("This setup script can install Chocolatey for you automatically."))
                    action = input("Install Chocolatey? [y/n]: ")
                    
                    # installing Chocolatey
                    if action in ["y", "Y", "yes", "Yes", "YES"]:
                        ot.administrative_powershell_command("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))")
                        os.system("runas /user:Administrator \"cmd.exe /C choco install mpv\"")
                        
            # installing mpv for Linux
            elif OPERATING_SYSTEM == "Linux":
                distro = ot.get_linux_distribution()
                if distro in ["Ubuntu", "Linux Mint", "Debian"]:
                    os.system("sudo apt install mpv")
                
                if distro == "Arch":
                    os.system("pacman -S mpv")
                                    
        else:
            print("If mpv is already installed, you are OK")
            print("Otherwise, the setup process going forward will crash")
            print("━" * len("Otherwise, the setup process going forward will crash"))
            input("Press ENTER to acknowledge ")
        
        print("If you installed everything, you should be good to go.")
        print("If the program doesn't run, try to run through this setup script again.")
        print("━" * len("If the program doesn't run, try to run through this setup script again."))
        input("Press ENTER to conclude ")
           
else:
    print("You do not have a config.txt file in your SnakeByte folder. Do you wish to create a new default one?")
    print("━" * len("You do not have a config.txt file in your SnakeByte folder. Do you wish to create a new default one?"))
    action = input("Create new config file? [y/n]: ")
    
    if action in ["y", "Y", "yes", "Yes", "YES"]:
        print("SnakeByte needs to know where your music is")
        print("━" * len("SnakeByte needs to know where your music is"))
        location = input("Where is your music? ")
        lines = [
            f"music = {location}"
        ]
        config_file = open("config.txt", "w")
        config_file.writelines('\n'.join(lines))
        config_file.close()
        
    else:
        print("\nYou need a config.txt file in order for SnakeByte to run.")
        print("If you do not wish to automatically create a new one, you can create one manually in the root of the SnakeByte folder.")
        print("━" * len("If you do not wish to automatically create a new one, you can create one manually in the root of the SnakeByte folder."))
        input("Press ENTER to conclude ")