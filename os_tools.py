import platform
import os

def clear():
    user_os = platform.system()
    if user_os == "Windows":
        os.system("cls")
    elif user_os in ["Linux", "Darwin"]:
        os.system("clear")
    else:
        print("OS TOOLS: User OS is unrecognized. Clear operation cannot procede.")

def get_os():
    return platform.system()

def restart_windows_explorer():
    if platform.system() == "Windows":
        os.system("taskkill /F /IM explorer.exe & start explorer")

def get_windows_version():
    return f"Windows {platform.release()}"

def powershell_command(argument):
    os.system(f"%SystemRoot%\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell.exe \"{argument}\"")

def administrative_powershell_command(argument):
    os.system(f"runas /user:Administrator \"%SystemRoot%\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell.exe \"{argument}\"\"")

def get_linux_distribution():
    distro_name = open('/etc/lsb-release').readline().strip().split('=')[-1]
    return distro_name

def terminal_install(package_name, package_manager = None):
    user_os = platform.system()
    if package_manager == None:
        
        if user_os == "Windows":
            os.system(f"winget install {package_name}")
        
        elif user_os == "Linux":
            distro = get_linux_distribution()
            distro_package_manager_map = {
                    "LinuxMint": "sudo apt install",
                    "Ubuntu": "sudo apt install",
                    "Fedora": "sudo dnf install",
                    "Termux": "pkg install",
                    "Alpine": "apk add",
                    "Manjaro": "pacman -S",
                    "Arch": "pacman -S",
                    "ArchLinux": "pacman -S"
                    
                    }
            os.system(f"{distro_package_manager_map[distro]} {package_name}")
        
        elif user_os == "Darwin":
            os.system("brew install {package_name}")
        
        else:
            print("OS TOOLS: Due to your OS not being recognized, you please specify a package manager in order to use this method")
    else:
        package_manager_map = {
                "choco": "choco install",
                "chocolatey": "choco install",
                "scoop": "scoop install",
                "wget": "wget",
                "curl": "curl",
                }
        os.system(f"{package_manager_map[package_manager]} {package_name}")
