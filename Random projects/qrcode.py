import qrcode

data = "Rutger houd van mannen en Rense schijnbaar ook!"

img = qrcode.make(data)

img.save('C:/Users/Gebruiker/Pictures/Qrcodepyproj')

