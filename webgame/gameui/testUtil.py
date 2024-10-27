def parseColors(genes:str):
    def parseHex(rgb_values:str):
        rgb = tuple(int(rgb_values[i:i+2], 16) for i in (0, 2, 4))
        parsed_rgb = {
            'red': rgb[0],
            'green': rgb[1],
            'blue': rgb[2],
        }
        return parsed_rgb
    primary_color = parseHex(genes[11:17])
    secondary_color = parseHex(genes[17:23])
    highlights = parseHex(genes[23:29])
    return primary_color, secondary_color, highlights

print(parseColors('ffffffffb12c50bff8873e1215abc'))