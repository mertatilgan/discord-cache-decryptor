import os
from colorama import Fore, Back, Style

print(Fore.CYAN + "Discord Cache Decrypter")
print(Fore.WHITE + "Coded by: Mert Kemal Atılgan")
print("https://github.com/mertatilgan\n")

path = input("Enter the location of Discord's Cache folder: ")
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.png'))
    i = i+1
print(Fore.GREEN + "[!] The operation is successful. Files in "+path+" location have been converted to .png format.")
print(Style.RESET_ALL)
