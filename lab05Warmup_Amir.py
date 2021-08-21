from PIL import Image

bear = Image.open( "bear.png" )
bear.show()
#bear.size
#600 pixels wide, 800 pixels long

#pixel = bear.getpixel( ( 100, 200) )
#RGB: (166,201,239)

#for i in range(100):
    #bear.putpixel( (i, 200) , (0, 0, 0) )
#turns the pixel at (100,200) to black

def invert( im ):

    ''' Invert the colors in the input image, im '''

    

    # Find the dimensions of the image

    (width, height) = im.size



    # Loop over the entire image

    for x in range( width ):

        for y in range( height ):

            (red, green, blue) = im.getpixel((x, y))
            im.putpixel((x,y),(255-red,255-green,255-blue))
            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them

            # in the image using putpixel()

def invert_block(im):
  (width, height) = im.size
  #iterates through (300,600) for width
  for x in range(width//2,width):
    #iterates through (0,400)
    for y in range(height//2):
        (red, green, blue) = im.getpixel((x, y))
        im.putpixel((x,y),(255-red,255-green,255-blue))


bear.save("tmp_Amir.png")
