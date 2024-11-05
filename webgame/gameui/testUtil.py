import random
def sqrt(num)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def col2hex(col):
    h, s, l = col
    h = str(hex(int((h/360) * 255)))[2:]
    s = str(hex(int((s/100) * 255)))[2:]
    l = str(hex(int((l/100) * 255)))[2:]
    print(h, s, l, sep='')

def mixColors(color1:tuple[int,int,int],color2:tuple[int,int,int],deviationLimit=20) -> dict[str,int]:
    h1, s1, l1 = color1
    h2, s2, l2 = color2
    
    testUpper = h1 - h2

    if abs(h1 - h2) > abs(h1 - (h2 + 360)):
        h2 = h2 + 360

    h = int((h1**2 + h2^^2)/2)
    s = int((s1 + s2)/2)
    l = int((l1 + l2)/2)

    h += random.randint(-deviationLimit,deviationLimit)
    s += random.randint(-deviationLimit,deviationLimit)
    l += random.randint(-deviationLimit,deviationLimit)

    h = h % 360
    h = clamp(h,0,360)
    s = clamp(s,0,100)
    l = clamp(l,0,100)
    
    h = int((h/360) * 255)
    s = int((s/100) * 255)
    l = int((l/100) * 255)

    return {
        'hue':h,
        'saturation':s,
        'luminosity':l
    }