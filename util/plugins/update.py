# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import *

def search_for_updates():
    clear()
    setTitle("Hazard Nuker Checking For Updates. . .")
    r = requests.get("https://github.com/Rdimo/Hazard-Nuker/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        soup = BeautifulSoup(requests.get("https://github.com/Rdimo/Hazard-Nuker/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        new_version = requests.get(update_url)
        setTitle("Hazard Nuker New Update Found!")
        print(f'''{Fore.YELLOW}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.RED}Looks like this Hazard Nuker {THIS_VERSION} is outdated '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.RED}'))

        if choice.upper() == 'Y':
            print(f"{Fore.WHITE}\nUpdating. . .")
            setTitle(f'Hazard Nuker Updating...')
            #if they are running hazard.exe
            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("HazardNuker.zip", 'wb')as zipfile:
                    zipfile.write(new_version.content)
                with ZipFile("HazardNuker.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("HazardNuker.zip")
                try:
                    cwd = os.getcwd()+'\\HazardNuker\\'
                    shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'HazardNuker.exe')
                    shutil.copyfile(cwd+'README.md', 'README.md')                   
                    shutil.rmtree('HazardNuker')
                    setTitle('Hazard Nuker Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!")
                    sleep(1)
                    os.startfile("HazardNuker.exe")
                    sys.exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.RED}\nHazard Nuker-{THIS_VERSION} doesn't have enough permission to update\ntry re-running again as admin or turn off anti-virus otherwise try and download it manually here {update_url}\n\n\"{err}\"")
                    sleep(10)
            #if they are running hazard source code
            else:
                new_version_soure = requests.get("https://github.com/Rdimo/Hazard-Nuker/archive/refs/heads/master.zip")
                with open("Hazard-Nuker-master.zip", 'wb')as zipfile:
                    zipfile.write(new_version_soure.content)
                with ZipFile("Hazard-Nuker-master.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Hazard-Nuker-master.zip")
                try:
                    cwd = os.getcwd()+'\\Hazard-Nuker-master'
                    shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                    shutil.rmtree(cwd)
                    setTitle('Hazard Nuker Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!")
                    sleep(1)
                    os.startfile("run.bat")
                    sys.exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.RED}\nHazard Nuker-{THIS_VERSION} doesn't have enough permission to update\ntry re-running again as admin or turn off anti-virus otherwise try and download it manually here {update_url}\n\n\"{err}\"")
                    sleep(10)

        else:
            input
            return