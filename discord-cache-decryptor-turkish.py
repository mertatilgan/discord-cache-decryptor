import os
from colorama import Fore, Back, Style

# Cache Dosyasını bulmak için yapmanız gerekenler:
# Windows arama yerine %appdata% yazın.
# Discord dosyasını açın.
# İçinde bulunan cache dosyasının konumunu kopyalayın

print(Fore.CYAN + "Discord Cache Decrypter")
print(Fore.WHITE + "Mert Kemal Atılgan tarafından kodlanmıştır.")
print("https://github.com/mertatilgan\n")

path = input("Discord'a ait olan Cache klasörünün konumunu girin: ")
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.png'))
    i = i+1
    print(Fore.GREEN + "[!] İşlem başarılı."+path+" konumunda bulunan dosyalar .png formatına çevrildi.")
    print(Style.RESET_ALL)
