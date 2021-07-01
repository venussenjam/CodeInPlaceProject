from simpleimage import SimpleImage

def main():
    #Draw Horizontal line patterns based on mod of Y
    image2 = SimpleImage.blank(500, 500)
    for x in range(image2.width):
        for y in range(image2.height):
            pixel = image2.get_pixel (x,y)
            if y % 6 == 0:
                setPixelRed(pixel)
            elif y % 5 == 1:
                setPixelGreen(pixel)
            else:
                setPixelBlue(pixel)
    image2.show()

    #Make 9 boxes and set color based on x and y values
    image3 = SimpleImage.blank(768, 768)
    for x in range(image3.width):
        for y in range(image3.height):
            pixel2 = image3.get_pixel (x,y)
            if (x//256) == 0:
                setPixel (pixel2, 0 , y % 256 , x % 256)
            elif (x//256) == 1:
                setPixel (pixel2, y % 256 , x % 256, 0)
            else:
                setPixel (pixel2, x % 256 , 0, y % 256)
    image3.show()

    #Make a circle by setting color only for pixels at a fixed distance from center
    imageSize = 512
    image4 = SimpleImage.blank(imageSize, imageSize)
    center = imageSize//2
    radius = imageSize//3
    for x in range(image4.width):
        for y in range(image4.height):
            pixel4 = image4.get_pixel (x,y)
            if (distance(center, center, x, y) == radius):
                setPixel (pixel4, 255, 0, 255)
            else:
                setPixel (pixel4, 0 , 0, 0)
    image4.show()

def distance (x1, y1, x2, y2):
    return (round(pow(pow((x1 - x2),2) + pow((y1 - y2),2),0.5)))


def setPixel(pixel, x,y,z):
    pixel.red = x
    pixel.green = y
    pixel.blue = z

def setPixelRed(pixel):
    pixel.red = 255
    pixel.green = 0
    pixel.blue = 0 

def setPixelGreen(pixel):
    pixel.red = 0
    pixel.green = 255

    pixel.blue = 0 

def setPixelBlue(pixel):
    pixel.red = 0
    pixel.green = 0
    pixel.blue = 255

if __name__ == '__main__':
    main()