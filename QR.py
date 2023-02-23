import qrcode as qr

val = input("Enter your link: ")
img = qr.make("val")


img.save("YsP_LinkedIn.png")
