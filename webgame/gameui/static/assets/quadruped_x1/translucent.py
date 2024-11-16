from PIL import Image, ImageFilter
import os
from prep import prep

def main():

    while not os.path.isfile((target := os.path.curdir+ '/' + input('File Name: '))):
        ...
    prep(target)
    with Image.open(target, 'r') as f:
        f.convert('RGB')
        pixels = []
        for row in range(f.height):
            pxRow = []
            for column in range(f.width):
                alpha = getGray(f.getpixel((column,row)))
                wob = 255 if alpha == 0 else 0
                newColor = (wob, wob, wob, alpha)
                if len(newColor) > 4:
                    newColor = (newColor[0], newColor[1], newColor[2], newColor[4])
                pxRow.append(newColor)
            pixels += pxRow
        new = Image.new('RGBA', (f.width,f.height))
        new.putdata(pixels)
        new.save(target)
    exit(0)

def getGray(rgb:tuple[int,int,int]):return 255 - (int(sum(rgb[:3])/3))


if __name__ == '__main__':
    main()
    input()