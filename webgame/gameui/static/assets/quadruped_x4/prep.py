from PIL import Image, ImageFilter
import os

def prep(target:str):
    if not target:
        while not os.path.isfile((target := os.path.curdir+ '/' + input('File Name: '))):
            ...
    with Image.open(target, 'r') as f:
        if f.mode == 'RGB':
            f.close()
            exit(0)
        pixels = []
        for row in range(f.height):
            pxRow = []
            for column in range(f.width):
                col = f.getpixel((column,row))
                wob = 255 if col[3] == 0 else 0
                if wob:
                    newColor = (wob, wob, wob, col[3])
                else:
                    newColor = (col[0], col[1], col[2], col[3])

                if len(newColor) > 4:
                    newColor = (newColor[0], newColor[1], newColor[2], newColor[4])
                pxRow.append(newColor)
            pixels += pxRow
        new = Image.new('RGBA', (f.width,f.height))
        new.putdata(pixels)
        new.save(target)
    if __name__ == '__main__':
        exit(0)


if __name__ == '__main__':
    prep('')
    input()