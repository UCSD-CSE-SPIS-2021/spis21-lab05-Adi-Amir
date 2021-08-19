from PIL import Image
bear = Image.open("bear.png")
bear.show()
pixel = bear.getpixel( ( 100, 200) )
print(pixel)
bear.putpixel( (100, 200), (0, 0, 0) )
#for i in range(100):
    #bear.putpixel( (i, 200) , (0, 0, 0) )


def invert(im):
    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
          if(x < 300):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel((x,y),(255-red,255-green,255-blue))

            # Complete this function by adding your lines of code here.
            
            # You need to calculate the new pixel values and then to change them

            # in the image using putpixel()
#def invert_block(im):
 # (width, height) = im.size
  #for x in range(width):
   # for y in range(height):
    #  (red, green, blue) = im.getpixel((x, y))
     # if(x > 300 & y < 400):
      #  im.putpixel((x,y),(255-red,255-green,255-blue))
def invert_block(im):
  (width, height) = im.size
  for x in range(width):
    for y in range(height):
      if(x >= 300 and y <= 400):
        (red, green, blue) = im.getpixel((x, y))
        im.putpixel((x,y),(255-red,255-green,255-blue))


invert_block(bear)
bear.save("tmp_Adi.png") 

