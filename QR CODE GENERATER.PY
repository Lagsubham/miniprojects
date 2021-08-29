import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr=pyqrcode.create("i m subham mandal")
qr.png("mycode.png",scale=8)

d=decode(image.open("mycode.png"))

print(d[0].data.decode("ascii"))