import os

# Cache Dosyasını bulmak için yapmanız gerekenler:
# Windows arama yerine %appdata% yazın.
# Discord dosyasını açın.
# İçinde bulunan cache dosyasının konumunu kopyalayın

print("\u001b[35;1mDiscord Cache Decrypter")
print("\u001b[37;1mMert Kemal Atılgan tarafından kodlanmıştır.")
print("https://github.com/mertatilgan\n")
path = input("Discord'un Cache klasörünün konumunu girin: ")
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.png'))
    i = i+1
    print("\u001b[32;1m[!] İşlem başarılı. \u001b[33;1m"+path+"\u001b[32;1m konumunda bulunan dosyalar .png formatına çevrildi.\u001b[37;1m")
