import colorama
from colorama import Fore, Style, Back
import os
import psutil
import platform
import datetime
import socket
import shutil
import webbrowser

users_name = os.getlogin()
users_pc = platform.node()

IP = socket.gethostbyname(socket.gethostname())
TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CPU = psutil.cpu_percent(interval=1)
RAM = psutil.virtual_memory().percent
DISK = psutil.disk_usage("/").percent
SYSTEM_USERS = platform.system()
BOOT_TIME_SECONDS = (datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())).total_seconds()
BOOT_TIME_STR = str(datetime.timedelta(seconds=int(BOOT_TIME_SECONDS)))

path = os.getcwd()

catfetch = (Fore.MAGENTA) + f"""
     ██████       █████                                     USER NAME: {users_name}     
    █  ██  ██    █  ██ █                                    USER PC: {users_pc}
    █ █  █   ████  █  ████                             
  ███                    ███████████████████                OS: {SYSTEM_USERS}
 ██                       ██               ██████           TIME: {TIME}
 █     ████      ████      █                    █████       CPU: {CPU}%
███         ████         ██                     ██  ██      RAM: {RAM}%
 ██                     ██                   ████    █      DISK: {DISK}%
  ██               ██████  ██     ████████████       █      HELP: cat info
   ███████████████████   ██    ███                 ██       IP: {IP}
   ██  █     █  ██    ██████████          █████████         BOOT TIME: {BOOT_TIME_STR}
    ████      ███              ████████████           
"""

print(catfetch)

while True:
    print(f"{Fore.YELLOW + f"<{path}>"}")
    input_command = input(Fore.WHITE + f"{users_name}^{SYSTEM_USERS} +> ").strip().lower()

    if input_command == "cat info":
        help_info = (Fore.CYAN) + """
        cat info - Displays information command with system details.
        cat exit - Exits the CAT terminal.
        cat clear - Clears the terminal screen.
        cat go - Changes the current directory.
        cat fc - Creates a new folder. 
        cat del - Deletes a file or folder.
        cat ls - Lists the contents of the current directory.
        cat fmf - Creates a full folder path.
        cat rf - Reads the contents of a file.
        cat rn - Renames files and folder.
        cat mv - Moves files and folder.
        cat kill - Kills id or names process.
        cat pl - Process List.
        cat goto = Find file name in current directory.
        _________________________________________
        bw - Fast Browser.
        ed - Fast Notepad.
        sd - Fast shutdown.
        run - Fast run program.
        dd - Fast Dodi repacks (Original).
        fg - Fast Fitgirl Repacks (Original).
        play - Fast play music.
        df - Fast download file in current directory. (hl df for more info)
        _________________________________________
        /s → Shutdown the computer (power off).

        /r → Restart the computer (reboot).

        /a → Abort a pending shutdown (cancel).

        /f → Force running applications to close (without warning).

        /t <seconds>
        """
        print(help_info)
    elif input_command == "cat clear":
        os.system("cls" if os.name == "nt" else "clear")
        print(catfetch)
    elif input_command == "cat exit":
        print(Fore.GREEN + "Exit...")
        exit()
    elif input_command == "cat go":
        new_path = input(Fore.YELLOW + "CAT ~ New path +> ").strip()
        
        try:
            os.chdir(new_path)
            path = new_path
            print(Fore.GREEN + f"Changed directory to: {new_path} :3")
        except Exception as e:
            print(Fore.RED + f"Error: not found {new_path} :(")
    elif input_command == "cat fc":
        folder_name = input(Fore.YELLOW + "CAT ~ Folder name +> ").strip()

        try:
            os.mkdir(folder_name)
            print(Fore.GREEN + f"Folder '{folder_name}' created successfully! :3")
        except Exception as e:
            print(Fore.RED + f"Error: could not create folder '{folder_name}' :(")
    elif input_command == "cat del":
        file_name = input(Fore.YELLOW + "CAT ~ File name +> ").strip()

        try:
            if os.path.isfile(file_name):
                os.remove(file_name)
                print(Fore.GREEN + f"File '{file_name}' deleted successfully! :3")
            elif os.path.isdir(file_name):
                shutil.rmtree(file_name)
                print(Fore.GREEN + f"Folder '{file_name}' deleted successfully! :3")
            else:
                print(Fore.RED + f"Error: '{file_name}' not found :(")
        except Exception as e:
            print(Fore.RED + f"Error: could not delete '{file_name}' :(")
    elif input_command == "cat ls":
        try:
            items_directory = os.listdir(path)
            if items_directory:
                print(Fore.GREEN + f"Contents of '{path}':")
                for item in items_directory:
                    print(Fore.CYAN + f"+ {item}")
            else:
                print(Fore.YELLOW + f"'{path}' is empty.")
        except Exception as e:
            print(Fore.RED + f"Error: could not list contents of '{path}' :(")
    elif input_command == "cat fmf":
        full_folder_name = input(Fore.YELLOW + "CAT ~ Full folder name (e.g path/folder) +> ").strip()
        try:
            os.makedirs(full_folder_name)
            print(Fore.GREEN + f"Full folder '{full_folder_name}' created successfully! :3")
        except Exception as e:
            print(Fore.RED + f"Error: could not create full folder '{full_folder_name}' :(")
    elif input_command == "cat rf":
        file_name_rf = input(Fore.YELLOW + "CAT ~ File name +> ").strip()
        try:
            with open(file_name_rf, 'r', encoding='utf-8') as file:
                content = file.read()
                print(Fore.GREEN + f"Contents in {file_name_rf}:\n{content}")
        except Exception as e:
            print(Fore.RED + f"Error: could not read file '{file_name_rf}' :(")
    elif input_command == "cat mv":
        old_path = input(Fore.YELLOW + "CAT ~ Old path +> ").strip()
        new_path = input(Fore.YELLOW + "CAT ~ New path +> ").strip()
        try:
            shutil.move(old_path, new_path)
            print(Fore.GREEN + f"Moved of {old_path} to {new_path} successfully! :3")
        except Exception as e:
            print(Fore.RED + f"Error: could not move '{old_path}' to '{new_path}' :(")
    elif input_command == "cat rn":
        old_name = input(Fore.YELLOW + "CAT ~ Old name +> ").strip()
        new_name = input(Fore.YELLOW + "CAT ~ New name +> ").strip()
        try:
            os.rename(old_name, new_name)
            print(Fore.GREEN + f"Renamed of {old_name} to {new_name} successfully! :3")
        except Exception as e:
            print(Fore.RED + f"Error: could not rename '{old_name}' to '{new_name}' :(")
    elif input_command == "ed":
        ed_input = input(Fore.YELLOW + "CAT ~ File name (in CD) and path +> ")
        try:
            print(Fore.GREEN + f"File {ed_input} opened in notepad :3")
            os.system(f"notepad {ed_input}")
        except Exception as e:
            print(Fore.RED + f"File not found {ed_input} {e} :(")
    elif input_command == "sd":
        sd_input_1 = input(Fore.YELLOW + "CAT ~ Enter one flags (e.g /r, /s, /a, /f) +> ")
        sd_input_2 = input(Fore.YELLOW + "CAT ~ Enter two flags (e.g /t) +> ")
        sd_input_3 = input(Fore.YELLOW + "CAT ~ Enter three flags +> ")
        sd_input_time = input(Fore.YELLOW + "CAT ~ Enter time (e.g seconds) +> ")
        try:
            print(Fore.GREEN + f"Shutdown {sd_input_1} {sd_input_2} successfly, TIME: {sd_input_time} :3")
            os.system(f"shutdown {sd_input_1} {sd_input_2} {sd_input_time}")
        except Exception as e:
            print(Fore.RED + f"Error shutdown: {e} :3")
    elif input_command == "bw":
        bw_input = input(Fore.YELLOW + "CAT ~ Enter URL +> ")
        try:
            print(Fore.GREEN + f"Opening URL: {bw_input} :3")
            webbrowser.open(bw_input)
        except Exception as e:
            print(Fore.RED + f"Error opening URL: {e} :(")
        if bw_input.lower() == "youtube":
            print(Fore.GREEN + f"Opening YouTube... :3")
            webbrowser.open("https://www.youtube.com")
        if bw_input.lower() == "google":
            print(Fore.GREEN + f"Opening Google... :3")
            webbrowser.open("https://www.google.com")
    elif input_command == "run":
        run_input = input(Fore.YELLOW + "CAT ~ Enter program name or path +> ")
        try:
            print(Fore.GREEN + f"Running program ~ {run_input } :3")
            os.system(f"start {run_input}")
        except Exception as e:
            print(Fore.RED + f"Error running {run_input}, {e} :(")
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                print(Fore.CYAN + f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU%: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_info'].rss / (1024 * 1024):.2f} MB")
        except Exception as e:
            print(Fore.RED + f"Error occurred while fetching process information: {e} :(")
    elif input_command == "cat kill":
        kill_input = input(Fore.YELLOW + "CAT ~ Enter PID or process name to kill +> ").strip()
        try:
            if kill_input.isdigit():
                pid = int(kill_input)
                proc = psutil.Process(pid)
                proc.terminate()
            else:
                found = False
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'].lower() == kill_input.lower():
                        proc.terminate()
                        print(Fore.GREEN + f"Process '{kill_input}' with PID {proc.info['pid']} terminated successfully! :3")
                        found = True
                if not found:
                    print(Fore.RED + f"Process '{kill_input}' not found. :(")
        except Exception as e:
            print(Fore.RED + f"Error occurred while killing process: {e} :(")
    elif input_command == "cat goto":
        goto_input = input(Fore.YELLOW + "CAT ~ Enter file/folder name +> ").strip()
        found_files = False
        try:
            for root, dirs, files in os.walk("."):
                for d in dirs:
                    if d.lower() == goto_input.lower():
                        print(Fore.GREEN + f"Found folder: {os.path.join(root, d)} :3")
                        found_files = True
                for f in files:
                    if f.lower() == goto_input.lower():
                        print(Fore.GREEN + f"Found file: {os.path.join(root, f)} :3")
                        found_files = True
                if not found_files:
                    print(Fore.RED + f"{goto_input} not found :(")
        except Exception as e:
            print(Fore.RED + f"Error occurred while searching: {e} :(")
    elif input_command == "play":
        play_input = input(Fore.YELLOW + "CAT ~ Enter music file name (current directory) +> ").strip()
        try:
            print(Fore.GREEN + f"Playing music: {play_input} :3")
            os.startfile(play_input)
        except Exception as e:
            print(Fore.RED + f"Error playing music: {e} :(")
    elif input_command == "df":
        import requests
        df_URL = input(Fore.YELLOW + "CAT ~ Enter name download file +> ").strip()
        try:
            shortcuts = {
                "blender": ("https://download.blender.org/release/Blender3.5/blender-3.5.0-windows-x64.msi", "blender-3.5.0-windows-x64.msi"),
                "steam": ("https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe", "SteamSetup.exe"),
                "discord": ("https://discord.com/api/download?platform=win", "DiscordSetup.exe"),
                "firefox": ("https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US", "FirefoxSetup.exe"),
                "winrar": ("https://www.rarlab.com/rar/winrar-x64-611.exe", "winrar-x64-611.exe"),
                "7zip": ("https://sourceforge.net/projects/sevenzip/files/7-Zip/22.01/7z2201-x64.exe/download", "7z2201-x64.exe"),
                "vsc": ("https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user", "VSCodeSetup.exe"),
                "python": ("https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe", "python-3.12.4-amd64.exe"),
                "spotify": ("https://download.scdn.co/SpotifySetup.exe", "SpotifySetup.exe")
            }

            if df_URL.lower() in shortcuts:
                url, filename = shortcuts[df_URL.lower()]
                print(Fore.GREEN + f"Downloading {df_URL.title()}... :3")
                r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, stream=True, timeout=15)
                if r.status_code == 200:
                    with open(filename, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    print(Fore.GREEN + f"{df_URL.title()} downloaded successfully! :3")
            else:
                print(Fore.GREEN + f"Downloading file from {df_URL} to {path} :3")
                r = requests.get(df_URL, headers={"User-Agent": "Mozilla/5.0"}, stream=True, timeout=15)
                if r.status_code == 200:
                    with open(path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                print(Fore.GREEN + f"File downloaded successfully! :3")

        except Exception as e:
            print(Fore.RED + f"Error downloading file: {e} :(")
    elif input_command == "hl df":
        hl_df_info = (Fore.CYAN) + """
        Fast download file in current directory.
        You can use shortcuts for popular programs:
        - blender
        - steam
        - discord
        - firefox
        - winrar
        - 7zip
        - vsc (Visual Studio Code)
        - python
        - spotify
        """
        print(hl_df_info)
    else:
        print(Fore.RED + "Unknown command. Type 'cat info' for available commands.")
