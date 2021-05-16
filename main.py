import pyqrcode as qr
import os

operating_system = os.name
url = input("Enter the url:\n")
qr_url = qr.create(url)
url = "_".join(url.split("https://")[1].split("/"))
if operating_system == "nt":
    os.chdir(os.getcwd() + "\created_qr_codes")
elif operating_system == "posix":
    os.chdir(os.getcwd() + "/created_qr_codes")
qr_url.png(url + ".png", scale=10)