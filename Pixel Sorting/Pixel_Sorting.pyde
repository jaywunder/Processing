"""What I'm doing is getting the 16 pixels above and below and averageing them
together to get some kind the averaging the y axis pixels then averageing those
two numbers and that's the new pixel color"""
from random import randint
from time import sleep

img = loadImage("/Users/JacobWunder/Desktop/wave.jpg")
width = img.width
height = img.height
    
def setup():
    size(width,height)
    image(img, 0, 0)
    #averagePixels()
    
def draw():
    if mousePressed:
        differentColors(0,height)
        #glitchRows(0,height)
    
    
def getLoc(_x, _y):
    return _x+(_y*(img.width-1))
    
def average(lst):
    if len(lst) != 0:
        #avg = total / (len(lst))
        avg = int(sum(lst))/int(len(lst))
        #print "lst:",lst
        #print "sum:",int(sum(lst))
        #print "len:",int(len(lst))  
        return int(avg)
    
def _draw():
    """Rename to 'draw' to use"""
    loadPixels()
    pixCopy = pixels
    for pix in range(len(pixels)-int(img.width/8)):
        pixels[pix] = pixCopy[pix+randint(0, int(img.width/8))]
    updatePixels()
    saveFrame("output-##")
    
def glitchWholePicture():
    """Blurs the whole picture"""
    loadPixels()
    divnum = 16
    for x in range(img.width):
        for y in range(img.width):
            #get location
            loc = x+(y*(img.width-1))
            #get chance
            rand0 = randint(0,5)
            rand1 = randint(0,5)
            if rand0 == rand1:
                #new coord
                newX = randint(x, ((img.width/divnum)+x))
                newLoc = newX+(y*(img.width-1))
                if newLoc < len(pixels)-img.width/divnum and loc < len(pixels)-img.width/divnum:  
                    for n in range(randint(0, img.width/divnum)):
                        pixels[loc+n] = pixels[newLoc]
    updatePixels()
    saveFrame("output-##")

def glitchRows(yMin,yMax):
    """Glitches specific rows between yMin and yMax"""
    loadPixels()
    divnum = 16
    for y in range(yMin,yMax):
        for x in range(img.width):
            loc = x+(y*(img.width-1))
            rand0 = randint(0,5)
            rand1 = randint(0,5)
            if rand0 == rand1:
                newX = randint(x, ((img.width/divnum)+x))
                newLoc = newX+(y*(img.width-1))
                if newLoc < len(pixels)-img.width/divnum and loc < len(pixels)-img.width/divnum:  
                    for n in range(randint(0, img.width/divnum)):
                        pixels[loc+n] = pixels[newLoc]
    updatePixels()
    saveFrame("output-##")
            
def blurImage():
    loadPixels()
    print("starting")
    n = 0
    divnum = 16
    pixList = []
    #for x in range(width-1):
        #for y in range(height-1)
    while n < len(pixels):
        for p in range(1, randint(2,int(width/divnum))):
            if n + p < len(pixels):
                pixList.append(pixels[n + p])
            else:
                break
            pixels[n] = average(pixList)
            pixList = []
        n += 1
    updatePixels()
    saveFrame("output-##")
    print("ending")
    
def differentColors(minY,maxY,mode,threshold):
    loadPixels()
    print("starting")
    threshDict = {.25:-2500000,
                  .5: -5000000,
                  1: -10000000,
                  2: -20000000,
                  3: -30000000,
                  4: -40000000,
                  5: -50000000,
                  6: -60000000,
                  7: -70000000,
                  8, -80000000,
                  9, -90000000,
                  10, -100000000}
                  
    for y in range(minY,maxY):
        for x in range(1,width):
            prevPix = pixels[(x-1)+(y*(img.width-1))]
            #print(y, x, pixels[x+(y*(img.width-1))] - prevPix)
            if pixels[x+(y*(img.width-1))] - prevPix < threshDict[threshold]: #-10000000
                if mode == 0:
                    pixels[x+(y*(img.width-1))] = prevPix
                elif mode == 1:
                    pixels[x+(y*(img.width-1))] = average((prevPix,pixels[x+(y*(img.width-1))]))
                
    print('ending')
    updatePixels()
    saveFrame("output-##")
                
