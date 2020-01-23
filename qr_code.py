from PIL import Image, ImageDraw, ImageFont
import qrcode


####################### use the function to create logo and return it as an object###################################
def qr_with_logo(message = '', logo = ''):
	#imported logo
	logo = Image.open(logo)#remove logo with the address of your file
 

	#create qrcode
	#message = 'flirty_with_pencils ' 
	image = qrcode.make(message)  #info added to qrcode


	#finding offset for logo
	bg_w, bg_h = image.size
	logo_w, logo_h = (bg_w//5, bg_h//5)
	offset = ((bg_w - logo_w) // 2, (bg_h - logo_h) // 2)


	#resizing logo
	logo.thumbnail((logo_w, logo_h), Image.ANTIALIAS)

	#creating final image
	image.paste(logo, offset)
	
	
	image.save('personalised_qr_code.jpg') #save the qrcode with the given file_name
	
	return image