# Importing library
import qrcode
import easygui

# Data to be encoded
myvar = easygui.enterbox("Please add a website link")

# Encoding data using make() function
img = qrcode.make(myvar)

# Saving as an image file
img.save('MyQRCode1.png')
