import os

def shutdown_system():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /s /t 1')
    elif os.name == 'posix':  # For Linux/Unix/Mac
        os.system('shutdown now')
    else:
        print("Unsupported operating system")
shutdown_system()
