from django.db import models
from .models import Pet, User
import random

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def parseTypes(genes:str):
    petTypes = []
    unparsedTypes = {}
    typeIndex = {
        # Pure elements
        'ww': 'water',
        'ff': 'fire',
        'rr': 'rock',
        'aa': 'air',
        'cc': 'cold',
        'll': 'light',
        'dd': 'dark',
        'mm': 'metal',
        'bb': 'blunt',
        'ss': 'sharp',
        'pp': 'physical',
        'nn': 'neutral',

        # Water
        'wf': 'steam',
        'fw': 'acid',
        'rw': 'mud',
        'wr': 'plant',
        'aw': 'cloud',
        'wa': 'mist',
        'wc': 'snow',
        'cw': 'ice',
        'wl': 'reflection',
        'lw': 'crystal',
        'wm': 'rust',
        'mw': 'mercury',
        'wd': 'abyss',
        'dw': 'void',
        'wb': 'erosion',
        'bw': 'wave',
        'ws': 'abrasion',
        'sw': 'whirlpool',
        'wp': 'pressure',
        'pw': 'hydraulics',

        # Fire
        'af': 'inferno',
        'fa': 'lightning',
        'fc': 'frostbite',
        'cf': 'thermal',
        'fl': 'radiance',
        'lf': 'photosphere',
        'fd': 'umbra',
        'df': 'hellfire',
        'fm': 'forge',
        'mf': 'fusion',
        'fb': 'impact',
        'bf': 'explosion',
        'fs': 'scission',
        'sf': 'cauterization',
        'fp': 'combustion',
        'pf': 'pyrokinetics',

        # Rock
        'rf': 'lava',
        'fr': 'coal',
        'ar': 'sand',
        'ra': 'dust',
        'rc': 'permafrost',
        'cr': 'glacier',
        'rl': 'gem',
        'lr': 'prism',
        'rd': 'obsidian',
        'dr': 'cave',
        'rm': 'ore',
        'mr': 'alloy',
        'rb': 'boulder',
        'br': 'landslide',
        'rs': 'sharpening',
        'sr': 'shrapnel',
        'rp': 'geodynamics',
        'pr': 'kinetics',

        # Air
        'ac': 'frost',
        'ca': 'chill',
        'al': 'halo',
        'la': 'rainbow',
        'ad': 'miasma',
        'da': 'vacuum',
        'am': 'magnetism',
        'ma': 'conductivity',
        'ab': 'gust',
        'ba': 'shockwave',
        'as': 'laceration',
        'sa': 'keen',
        'ap': 'pneumatics',
        'pa': 'aerodynamics',

        # Cold
        'cl': 'aurora',
        'lc': 'bioluminescence',
        'cd': 'styx',
        'dc': 'night',
        'cm': 'superconductor',
        'mc': 'tempering',
        'cb': 'hailstone',
        'bc': 'shock',
        'cs': 'shard',
        'sc': 'cryoscission',
        'cp': 'thermodynamics',
        'pc': 'cryogenics',

        # Light
        'ld': 'eclipse',
        'dl': 'twilight',
        'lm': 'reflection',
        'ml': 'luster',
        'lb': 'flash',
        'bl': 'flare',
        'ls': 'laser',
        'sl': 'glint',
        'lp': 'scintillation',
        'pl': 'photon',

        # Dark
        'dm': 'tenebrae',
        'md': 'umbrium',
        'db': 'null',
        'bd': 'black hole',
        'ds': 'infection',
        'sd': 'necrosis',
        'dp': 'dark matter',
        'pd': 'antimatter',

        # Metal
        'mb': 'mace',
        'bm': 'dent',
        'ms': 'blade',
        'sm': 'edge',
        'mp': 'force',
        'pm': 'impact',

        # Blunt
        'bs': 'concussion',
        'sb': 'dull',
        'bp': 'impulse',
        'pb': 'break',

        # Sharp
        'sp': 'incision',
        'ps': 'precision',
    }

    # Loop through genes two characters at a time
    for i in range(0, len(genes[:7]), 2):
        petType = genes[i:i+2]  # Get two characters and convert to lowercase
        if petType in typeIndex:
            if typeIndex[petType] not in petTypes:
                petTypes.append(typeIndex[petType])
                unparsedTypes[typeIndex[petType]] = {'c1':genes[i],'c2':genes[i+1]}
        else:
            if 'n' in petType and 'neutral' not in petTypes:
                petTypes.append('neutral')
                unparsedTypes['neutral'] = {'c1':genes[i],'c2':genes[i+1]}
            else:
                petTypes.append('unknown')  # Handle case where gene type is not in the index
                unparsedTypes['unknown'] = {'c1':genes[i],'c2':genes[i+1]}
    
    return petTypes, unparsedTypes

def parsePersonality(genes:str):
    personality = []
    trait_index = {
        'a': 'curious',
        'b': 'loyal',
        'c': 'playful',
        'd': 'careful',
        'e': 'brave',
        'f': 'clever', 
        'g': 'observant',
        'h': 'nurturing',
        'i': 'competitive',
        'j': 'musical',
        'k': 'creative',
        'l': 'dignified',
        'm': 'gentle',
        'n': 'adventurous',
        'o': 'patient',
        'p': 'determined'
    }
    personality_genes = genes[8:11]
    for gene in personality_genes:
        if gene in trait_index:
            if trait_index[gene] not in personality:
                personality.append(trait_index[gene])
    return personality

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

def parseFeatures(genes:str):

    walkIndex = {
        'a': 'biped',
        'b': 'quadruped',
        'c': 'slither',
        'd': 'glide'
    }
    if genes[29] in walkIndex:
        walkType = walkIndex[genes[29]]
    else:
        walkType = 'slither'

    coverIndex = {
        'a': 'skin',
        'b': 'fur',
        'c': 'carapace',
        'd': 'leather',
        'e': 'scales',
        'f': 'feathers'
    }

    if genes[30] in coverIndex:
        skinType = f'{coverIndex[genes[30]]}.png'
    else:
        skinType = 'skin.png'

    featureIndex = {
        'a': 'spots',
        'b': 'antennae',
        'c': 'tail',
        'd': 'alt_tail',
        'e': 'sharp_ears',
        'f': 'none',
        'g': 'horns',
        'h': 'alt_horns'
    }

    if genes[31] in featureIndex:
        traitType = f'{featureIndex[genes[31]]}.png'
    else:
        traitType = 'none.png'


    colors = {
        'spots':'Secondary',
        'antennae':'Secondary',
        'tail':'Primary',
        'alt_tail':'Primary',
        'sharp_ears':'Primary',
        'none':'Secondary',
        'horns':'Secondary',
        'alt_horns':'Secondary'
    }

    
    traitCol = colors[traitType[:-4]]

    features = {
        'walk': f'assets/{walkType}/',
        'skin': skinType,
        'trait': traitType,
        'color': traitCol
    }


    return features

def parsePet(pet:Pet):
    parsedPet = {}
    genes = pet.genes.lower()
    petTypes, unparsedTypes = parseTypes(genes)
    personality = parsePersonality(genes)
    primary_color, secondary_color, highlights = parseColors(genes)

    parsedPet['types'] = petTypes
    parsedPet['unparsedTypes'] = unparsedTypes

    parsedPet['personality'] = personality
    
    parsedPet['primary'] = primary_color
    parsedPet['secondary'] = secondary_color
    parsedPet['highlights'] = highlights

    parsedPet['features'] = parseFeatures(genes)
    
    parsedPet['gender'] = pet.gender
    parsedPet['name'] = pet.name
    parsedPet['age'] = int(pet.age)

    parsedPet['uuid'] = pet.letterId

    return parsedPet

def generateUUID(length:int):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    uuid = ''
    for _ in range(length):
        uuid += random.choice(alpha)
    return uuid

def randomPet(master):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    genome = ''
    
    types = ['w', 'f', 'r', 'a', 'c', 'l', 'd', 'm', 'b', 's', 'p', 'n']
    for _ in range(8):
        genome += random.choice(types)
    
    for _ in range(3):
        genome += random.choice(alpha[:16])
    
    for _ in range(9):
        genome += str(format(random.randint(0,255), '02x'))

    genome += random.choice(alpha[0:4])
    genome += random.choice(alpha[0:6])
    genome += random.choice(alpha[0:8])
    
    print(genome)

    pet = Pet(genes=genome,master=master,age=0.0,gender=random.choice([True, False]),name='Generated Pet',letterId=generateUUID(64))
    return pet

def mixColors(color1:tuple[int,int,int],color2:tuple[int,int,int],deviationLimit=20) -> dict[str,int]:
    r = int((color1[0] + color2[0])/2)
    g = int((color1[1] + color2[1])/2)
    b = int((color1[2] + color2[2])/2)

    r += random.randint(-deviationLimit,deviationLimit)
    g += random.randint(-deviationLimit,deviationLimit)
    b += random.randint(-deviationLimit,deviationLimit)

    r = clamp(r,0,255)
    g = clamp(g,0,255)
    b = clamp(b,0,255)
    
    return {
        'red':r,
        'green':g,
        'blue':b
    }

def combinePets(pet1:Pet,pet2:Pet,master:User,mutationChance:float=0.05):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    types = ['w', 'f', 'r', 'a', 'c', 'l', 'd', 'm', 'b', 's', 'p', 'n']
    
    genome1 = pet1.genes
    genome2 = pet2.genes
    childGenome = ''

    for i in range(11):
        if random.random() > mutationChance:
            if random.choice([True, False]):
                childGenome += genome1[i]
            else:
                childGenome += genome2[i]
        else:
            childGenome += random.choice(types)
    
    primary_color_1, secondary_color_1, highlights_1 = parseColors(genome1)
    primary_color_2, secondary_color_2, highlights_2 = parseColors(genome2)

    childPrimary = mixColors(tuple(primary_color_1.values()),tuple(primary_color_2.values()))
    childSecondary = mixColors(tuple(secondary_color_1.values()),tuple(secondary_color_2.values()))
    childHighlights = mixColors(tuple(highlights_1.values()),tuple(highlights_2.values()))
    print((childPrimary,childSecondary,childHighlights))
    for var in [childPrimary,childSecondary,childHighlights]:
        for col in ['red','green','blue']:
            childGenome += (format(var[col], '02x'))
            
    if random.random() > mutationChance:
        if random.choice([True, False]):
            childGenome += genome1[i]
        else:
            childGenome += genome2[i]
    else:
        childGenome += random.choice(alpha[0:4])
    
    if random.random() > mutationChance:
        if random.choice([True, False]):
            childGenome += genome1[i]
        else:
            childGenome += genome2[i]
    else:
        childGenome += random.choice(alpha[0:6])
            
    if random.random() > mutationChance:
        if random.choice([True, False]):
            childGenome += genome1[i]
        else:
            childGenome += genome2[i]
    else:
        childGenome += random.choice(alpha[0:8])
    print(childGenome)

    child = Pet(genes=childGenome,master=master,age=0.0,name='Combined Pet',gender=random.choice([True, False]),letterId=generateUUID(64))
    child.save()

def starterPets(master:User):
    genome1 = 'wwwwwwwwcno2b4ad4602bd42b9fd4bec'
    genome2 = 'ffffffffeipff5900ffd800ff0027beh'
    genome3 = 'rrrrrrrrbop57c13e3ec16699c13ebeb'
    genome4 = 'aaaaaaaaagmf6f6f6dcdddd5f86a0beg'

    pet1 = Pet(genes=genome1,master=master,age=100.0,gender=False,name='Aqua',letterId=generateUUID(64))
    pet2 = Pet(genes=genome2,master=master,age=100.0,gender=True,name='Ignis',letterId=generateUUID(64))
    pet3 = Pet(genes=genome3,master=master,age=100.0,gender=False,name='Gaia',letterId=generateUUID(64))
    pet4 = Pet(genes=genome4,master=master,age=100.0,gender=True,name='Aero',letterId=generateUUID(64))
    return pet1, pet2, pet3, pet4