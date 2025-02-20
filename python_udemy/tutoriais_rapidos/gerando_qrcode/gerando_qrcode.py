import pyqrcode


qr = pyqrcode.create(input("Digite o site:\n"))
qr.png("qr.png", scale=6)
print("QR gerado")  
