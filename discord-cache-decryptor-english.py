import os

print("\u001b[35;1mDiscord Cache Decrypter")
print("\u001b[37;1mCoded by: Mert Kemal Atılgan")
print("https://github.com/mertatilgan\n")
path = input("Enter the location of Discord's Cache folder: ")
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.png'))
    i = i+1
    print("\u001b[32;1m[!] The operation is successful. Files in \u001b[33;1m"+path+"\u001b[32;1m location have been converted to .png format.\u001b[37;1m")
