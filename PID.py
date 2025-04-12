import os
import psutil
import pyperclip

def copy_app_folder(pid):
    try:
        process = psutil.Process(pid)
        exe_path = process.exe()                
        folder_path = os.path.dirname(exe_path)   
        pyperclip.copy(folder_path)             
        print(f"Masir folder barname (PID: {pid}) dar clipboard copy shod:\n{folder_path}")
    except psutil.NoSuchProcess:
        print(f"Hich process ba PID {pid} yaft nashod.")
    except Exception as e:
        print(f"Khatayi rokh dad: {e}")

if __name__ == "__main__":
    while True:
        pid_input = input("Shenase (PID) barname-ye mored nazar ra vared konid (ya 'exit' baraye khoruj): ")
        if pid_input.strip().lower() == "exit":
            print("Barname baste shod.")
            break
        try:
            pid = int(pid_input)
            copy_app_folder(pid)
        except ValueError:
            print("Voroodi motabar adadi nist. Lotfan yek shomare sahih vared konid.")
