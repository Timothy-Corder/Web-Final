from django.db import models
from django.shortcuts import get_object_or_404
from .models import Pet, User, Egg, UserProfile
import random
from math import sqrt
import datetime

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def parseTypes(genes:str):
    typeIndex = {

    
        # Pure elements
        'nn': 'neutral',

        # Water
        'ww': 'water',
        'wf': 'steam',
        'wr': 'plant',
        'wa': 'mist',
        'wc': 'snow',
        'wl': 'reflection',
        'wm': 'rust',
        'wd': 'abyss',
        'wb': 'erosion',
        'ws': 'abrasion',
        'wp': 'pressure',

        # Fire
        'fw': 'acid',
        'ff': 'fire',
        'fr': 'coal',
        'fa': 'lightning',
        'fc': 'frostbite',
        'fl': 'radiance',
        'fd': 'umbra',
        'fm': 'forge',
        'fb': 'impact',
        'fs': 'scission',
        'fp': 'combustion',

        # Rock
        'rr': 'rock',
        'rw': 'mud',
        'rf': 'lava',
        'ra': 'dust',
        'rc': 'permafrost',
        'rl': 'gem',
        'rd': 'obsidian',
        'rm': 'ore',
        'rb': 'boulder',
        'rs': 'sharpening',
        'rp': 'geodynamics',

        # Air
        'aa': 'air',
        'aw': 'cloud',
        'af': 'inferno',
        'ar': 'sand',
        'ac': 'frost',
        'al': 'halo',
        'ad': 'miasma',
        'am': 'magnetism',
        'ab': 'gust',
        'as': 'laceration',
        'ap': 'pneumatics',

        # Cold
        'cw': 'ice',
        'cf': 'thermal',
        'cr': 'glacier',
        'ca': 'chill',
        'cc': 'cold',
        'cl': 'aurora',
        'cd': 'styx',
        'cm': 'superconductor',
        'cb': 'hailstone',
        'cs': 'shard',
        'cp': 'thermodynamics',

        # Light
        'lw': 'crystal',
        'lf': 'photosphere',
        'lr': 'prism',
        'la': 'rainbow',
        'lc': 'bioluminescence',
        'll': 'light',
        'ld': 'eclipse',
        'lm': 'reflection',
        'lb': 'flash',
        'ls': 'laser',
        'lp': 'scintillation',

        # Dark
        'dw': 'void',
        'df': 'hellfire',
        'dr': 'cave',
        'da': 'vacuum',
        'dc': 'night',
        'dl': 'twilight',
        'dd': 'dark',
        'dm': 'tenebrae',
        'db': 'null',
        'ds': 'infection',
        'dp': 'dark matter',

        # Metal
        'mw': 'mercury',
        'mf': 'fusion',
        'mr': 'alloy',
        'ma': 'conductivity',
        'mc': 'tempering',
        'ml': 'luster',
        'md': 'umbrium',
        'mm': 'metal',
        'mb': 'mace',
        'ms': 'blade',
        'mp': 'force',

        # Blunt
        'bw': 'wave',
        'bf': 'explosion',
        'br': 'landslide',
        'ba': 'shockwave',
        'bc': 'shock',
        'bl': 'flare',
        'bd': 'black hole',
        'bm': 'dent',
        'bb': 'blunt',
        'bs': 'concussion',
        'bp': 'impulse',

        # Sharp
        'sw': 'whirlpool',
        'sf': 'cauterization',
        'sr': 'shrapnel',
        'sa': 'keen',
        'sc': 'cryoscission',
        'sl': 'glint',
        'sd': 'necrosis',
        'sm': 'edge',
        'sb': 'dull',
        'ss': 'sharp',
        'sp': 'incision',

        # Physical
        'pw': 'hydraulics',
        'pf': 'pyrokinetics',
        'pr': 'kinetics',
        'pa': 'aerodynamics',
        'pc': 'cryogenics',
        'pl': 'photon',
        'pd': 'antimatter',
        'pm': 'impact',
        'pb': 'break',
        'ps': 'precision',
        'pp': 'physical',
    }


    petTypes = []
    unparsedTypes = {}


    # Loop through genes two characters at a time
    for i in range(0, len(genes[:7]), 2):
        petType = genes[i:i+2]  # Get two characters and convert to lowercase
        if petType in typeIndex:
            if typeIndex[petType] not in petTypes:
                petTypes.append(typeIndex[petType])
                unparsedTypes[typeIndex[petType]] = {'c1':genes[i],'c2':genes[i+1]}
        else:
            if 'n' in petType:
                if 'neutral' not in petTypes:
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
        hex = tuple(int(rgb_values[i:i+2], 16) for i in (0, 2, 4))
        parsed_hsl = {
            'hue': int((hex[0]/255)*360),
            'saturation': int((hex[1]/255)*100),
            'luminosity': int((hex[2]/255)*100),
        }
        return parsed_hsl

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
        'd': 'rough',
        'e': 'scales',
        'f': 'feathers',
        'g': 'shiny'
    }

    if genes[30] in coverIndex:
        skinType = f'{coverIndex[genes[30]]}'
    else:
        skinType = 'skin'

    featureIndex = {
        'a': 'spots',
        'b': 'antennae',
        'c': 'tail',
        'd': 'alt_tail',
        'e': 'sharp_ears',
        'f': 'none',
        'g': 'horns_0',
        'h': 'horns_1'
    }

    if genes[31] in featureIndex:
        traitType = f'{featureIndex[genes[31]]}'
    else:
        traitType = 'none'


    colors = {
        'spots':'Secondary',
        'antennae':'Secondary',
        'tail':'Primary',
        'alt_tail':'Primary',
        'sharp_ears':'Primary',
        'none':'Secondary',
        'horns_0':'Secondary',
        'horns_1':'Secondary'
    }

    positions = {
        'spots':6,
        'antennae':8,
        'tail':8,
        'alt_tail':8,
        'sharp_ears':8,
        'none':8,
        'horns_0':8,
        'horns_1':8
    }

    # --- Code for pre-biped/slither implementation
    if walkType not in ['quadruped', 'glide']:
        walkType = 'glide'
    # --- End
    
    traitCol = colors[traitType]

    features = {
        'walk': walkType,
        'skin': skinType,
        'trait': traitType,
        'color': traitCol,
        'position': positions[traitType]
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
    def generate():
        uuid = ''
        for _ in range(length):
            uuid += random.choice(alpha)
        return uuid
    while True:
        uuid = generate()
        try:
            Pet.objects.get(letterId=uuid)
        except Pet.DoesNotExist:
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

    pet = Pet(genes=genome,master=master,age=0.0,gender=random.choice([True, False]),name='Generated Pet',letterId=generateUUID(64))
    return pet

def mixColors(color1: tuple[int, int, int], color2: tuple[int, int, int], deviationLimit=20) -> dict[str, int]:
    h1, s1, l1 = color1
    h2, s2, l2 = color2

    # Adjust hue for circular distance
    directDiff = abs(h1 - h2)
    if directDiff <= 180:
        h = (h1 + h2) / 2
    else:
        # Wrap around the 360 boundary
        if h1 < h2:
            h1 += 360
        else:
            h2 += 360
        h = (h1 + h2) / 2 % 360  # Wrap back to 0-360 after averaging

    # Calculate averages of saturation and luminosity
    s = (s1 + s2) / 2
    l = (l1 + l2) / 2

    # Apply random deviation within the limit
    h += random.randint(-deviationLimit, deviationLimit)
    s += random.randint(-deviationLimit, deviationLimit)
    l += random.randint(-deviationLimit, deviationLimit)

    # Clamp values within their ranges
    h = h % 360  # Keep hue in 0-360 range
    s = clamp(s, 0, 100)
    l = clamp(l, 0, 100)

    # Convert to 0-255 scale
    h = int((h / 360) * 255)
    s = int((s / 100) * 255)
    l = int((l / 100) * 255)

    return {
        'hue': h,
        'saturation': s,
        'luminosity': l
}

def combinePets(pet1:Pet,pet2:Pet,mutationChance:float=0.05):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rarityIndex = {
        'n': 8,
        'w': 10,
        'f': 10,
        'r': 10,
        'a': 10,
        'c': 7,
        'l': 5,
        'd': 5,
        'm': 6,
        'b': 4,
        's': 4,
        'p': 2,
    }
    
    genome1 = pet1.genes
    genome2 = pet2.genes
    childGenome = ''

    for i in range(8):
        if random.random() > mutationChance:
            roll = random.random()
            totalChance = (cutoff := rarityIndex[genome1[i]]) + rarityIndex[genome2[i]]
            if (roll * totalChance) < cutoff:
                childGenome += genome1[i]
            else:
                childGenome += genome2[i]
        else:
            roll = random.random()
            keys = list(rarityIndex.keys())
            for j in range(len(keys)):
                currentKeys = keys[:j]
                currVal = 0
                for key in currentKeys:
                    currVal += rarityIndex[key]
                if (roll * sum(list(rarityIndex.values()))) < currVal:
                    print(childGenome)
                    childGenome += keys[j]
                    print(childGenome)
                    break
    for i in range(8,11):
        if random.random() > mutationChance:
            if random.choice([True,False]):
                childGenome += genome1[i]
            else:
                childGenome += genome2[i]
        else:
            roll = random.choice(alpha[:17])
            childGenome += roll
        
    
    primary_color_1, secondary_color_1, highlights_1 = parseColors(genome1)
    primary_color_2, secondary_color_2, highlights_2 = parseColors(genome2)

    childPrimary = mixColors(tuple(primary_color_1.values()),tuple(primary_color_2.values()))
    childSecondary = mixColors(tuple(secondary_color_1.values()),tuple(secondary_color_2.values()))
    childHighlights = mixColors(tuple(highlights_1.values()),tuple(highlights_2.values()))
    for var in [childPrimary,childSecondary,childHighlights]:
        for col in ['hue','saturation','luminosity']:
            childGenome += (format(var[col], '02x'))
            
            
    if random.random() > mutationChance:
        if random.choice([True, False]):
            childGenome += genome1[len(childGenome)]
        else:
            childGenome += genome2[len(childGenome)]
    else:
        childGenome += random.choice(alpha[0:4])
    print(childGenome)
    print(len(childGenome))
    
    if random.random() > mutationChance:
        if random.choice([True, False]):
            childGenome += genome1[len(childGenome)]
        else:
            childGenome += genome2[len(childGenome)]
    else:
        childGenome += random.choice(alpha[0:6])
    print(childGenome)
    print(len(childGenome))
            
    if random.random() > mutationChance:
        if random.choice([True, False]):
            childGenome += genome1[len(childGenome)]
        else:
            childGenome += genome2[len(childGenome)]
    else:
        childGenome += random.choice(alpha[0:8])
    print(childGenome)
    print(len(childGenome))

    return childGenome
    # 
    # child.save()

def hatch(egg:Egg, name:str, gender:bool):
    newGenome = combinePets(egg.mother,egg.father,)

    hatchling = Pet(genes=newGenome, master=egg.master, name=name, age = 0.0, gender=gender, letterId=generateUUID(64))

    egg.delete()
    return hatchling

def starterPets(master:User):
    genome1 = 'wwwwwwwwcno8cd6ad8cd6e58cd667bec'
    genome2 = 'ffffffffeip15ff9915ff6600ff7fbeh'
    genome3 = 'rrrrrrrrbop57c13e3ec16699c13ebeb'
    genome4 = 'aaaaaaaaagmf6f6f681aadd5f86a0beg'

    pet1 = Pet(genes=genome1,master=master,age=100.0,gender=False,name='Aqua',letterId=generateUUID(64))
    pet2 = Pet(genes=genome2,master=master,age=100.0,gender=True,name='Ignis',letterId=generateUUID(64))
    pet3 = Pet(genes=genome3,master=master,age=100.0,gender=False,name='Gaia',letterId=generateUUID(64))
    pet4 = Pet(genes=genome4,master=master,age=100.0,gender=True,name='Aero',letterId=generateUUID(64))
    return pet1, pet2, pet3, pet4

def get_settings(user:User):
    qualityMap = ['_x1','_x4','_x8']
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(quality=0,user=user)
        profile.save()
    settings = {}
    settings['quality'] = qualityMap[profile.quality]
    
    return settings

def set_settings(user:User,**settings):
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(quality=0,user=user)
        profile.save()

    for setting, value in settings.items():
        print(setting,value)
        setattr(profile, setting, value)
    profile.save()
    
    
def getPalestColor(primary, secondary, highlights):
    # Compare luminosity (the 'l' value) to get the palest color
    colors = [primary, secondary, highlights]
    palest_color = min(colors, key=lambda c: c['luminosity'])
    return palest_color

def getMostSaturatedColor(primary, secondary, highlights):
    # Compare saturation (the 's' value) to get the most saturated color
    colors = [primary, secondary, highlights]
    most_saturated_color = max(colors, key=lambda c: c['saturation'])
    return most_saturated_color

def makeEgg(pet1_id:int, pet2_id:int, master:User):
    pet1 = get_object_or_404(Pet, id=pet1_id)
    pet2 = get_object_or_404(Pet, id=pet2_id)

    # Ensure the selected pets belong to the user and are of opposite genders
    if pet1.master == master and pet2.master == master and pet1.gender != pet2.gender:
        # Generate the child's genome using combinePets
        child_genome = combinePets(pet1, pet2)
        
        # Parse colors for parent1 and parent2
        primary_color_1, secondary_color_1, highlights_1 = parseColors(pet1.genes)
        primary_color_2, secondary_color_2, highlights_2 = parseColors(pet2.genes)

        # Get the palest color from parent1
        palest_color = getPalestColor(primary_color_1, secondary_color_1, highlights_1)
        # Get the most saturated color from parent2
        most_saturated_color = getMostSaturatedColor(primary_color_2, secondary_color_2, highlights_2)

        # Create a new egg with the determined colors
        new_egg = Egg(
            color1=''.join(format(palest_color[c], '02x') for c in ['hue', 'saturation', 'luminosity']),
            color2=''.join(format(most_saturated_color[c], '02x') for c in ['hue', 'saturation', 'luminosity']),
            mother=pet1 if not pet1.gender else pet2,
            father=pet1 if pet1.gender else pet2,
            master=master,
            hatchDate=datetime.datetime.now() + datetime.timedelta(days=3)
        )
        
        return new_egg