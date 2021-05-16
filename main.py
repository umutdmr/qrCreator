import pyqrcode as qr
import os

url = input("Enter the url:\n")
qr_url = qr.create(url)
url = "_".join(url.split("https://")[1].split("/"))
os.chdir(os.getcwd() + "\created_qr_codes")
qr_url.png(url + ".png", scale=10)