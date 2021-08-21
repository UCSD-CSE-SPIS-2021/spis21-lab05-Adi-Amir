#print("Running lab05Warmup_Amir.py") 
#import lab05Warmup_Amir
#print("Running lab05Warmup_Adi.py") 
#import lab05Warmup_Adi
from PIL import Image

bear = Image.open("bear.png")

def grayscale(im):
  (width, height) = im.size
  
  for x in range(width):
    
    for y in range(height):
        (red, green, blue) = im.getpixel((x, y))
        lum = int(0.21*red+0.72*green+0.07*blue)
        im.putpixel((x,y),(lum,lum,lum))

def binarize(im, thresh, startx, starty, endx, endy):
  (width, height) = im.size
  
  for x in range(startx, endx):
    
    for y in range(starty,endy):
        (red, green, blue) = im.getpixel((x, y))
        lum = int(0.21*red+0.72*green+0.07*blue)
        color  = 0
        if(lum>thresh):
            color = 255
        else:
            color = 0
        im.putpixel((x,y),(color,color,color))

def mirrorVert(im):
    (width, height) = im.size
    for x in range(width):
    
        for y in range(height//2,height):
            (red,green,blue) = im.getpixel((x,height-y))
            im.putpixel((x,y),(red,green,blue))

def mirrorHoriz(im):
    (width, height) = im.size
    for x in range(width//2,width):
    
        for y in range(height):
            (red,green,blue) = im.getpixel((width-x,y))
            im.putpixel((x,y),(red,green,blue))

def flipVert(im):
    (width,height) = im.size
    
    copy = Image.open("bear.png")

    for x in range(width):
        for y in range(height):
            (red,green,blue) = im.getpixel((x,height-y-1))
            copy.putpixel((x,y),(red,green,blue))

    for x in range(width):
        for y in range(height):
            (red,green,blue) = copy.getpixel((x,y))
            im.putpixel((x,y), (red, green, blue))

def scale(im):
    (width, height) = im.size
    copy = Image.new('RGB', (width//2,height))

    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            if(x%2 == 0 and y%2 == 0):
                copy.putpixel((x//2, y//2), (red, green, blue))
            
    return copy

def blur(im):
  (width, height) = im.size
  totalRed = 0
  totalGreen = 0 
  totalBlue = 0
  copy = Image.new('RGB', (width,height))
  for x in range(width):
    for y in range(height):
      (red, green, blue) = im.getpixel((x, y))
      totalRed += red
      totalGreen += green
      totalBlue += blue
  avgRed = int(totalRed // height)
  avgGreen = int(totalGreen // height)
  avgBlue = int(totalBlue // height)
  for x in range(width):
    for y in range(height):
      im.putpixel((x,y), (avgRed,avgGreen,avgBlue))
  return copy



#grayscale(bear)
#bear.save("grayscale.png")

#binarize(bear,150,200,400,400,600)
#bear.save("binarize.png")

#mirrorVert(bear)
#bear.save("mirrorVert.png")

#mirrorHoriz(bear)
#bear.save("mirrorHoriz.png")

#flipVert(bear)
#bear.save("flipVert.png")

#bearScale = scale(bear)
#bearScale.save("scale.png")

blur(bear)
bear.save("blur.png")