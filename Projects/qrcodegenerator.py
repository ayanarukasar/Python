from turtle import back
import qrcode
import image

qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://www.linkedin.com/in/ayana-rukasar-28a9851a3/?lipi=urn%3Ali%3Apage%3Ad_flagship3_resumebuilder%3BOCDAAve3RASz7PNxX%2FgKlw%3D%3D"

qr.add_data(data)
qr.make(fit=True)

image=qr.make_image(fill="black",back_color="white")
image.save("test.png")