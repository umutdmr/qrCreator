import pyqrcode as qr

url = input("Enter the url:\n")
qr_url = qr.create(url)
qr_url.png("result.png", scale=10)