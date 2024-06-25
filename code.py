import qrcode
import os

# Path to stock QR Code
path = "data/"

if (os.path.isdir(path) == False):
    os.mkdir(path)

data = str(input("Data to store inside the QR Code\n"))
img_name = str(input("Name of the output (.png format)\n"))

img = qrcode.make(data)
img.save(path+img_name+".png")
