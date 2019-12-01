##############################
# Created by Eric Davidson
# https://github.com/erdavids
##############################

# Width/Height of the image
imgw, imgh = 2000, 2000


#############
# Change the tile style
#############
hexagon_size = 10
outline_width = 1
outline_color = (0, 0, 0)
custom_stroke = True

#############
# Noise Variables
#############
noise_loc_mod = 4
noise_scale = .02
noise_max = 120
max_distance = 0.55 * min(imgw, imgh)

#############
# Map Variables
#############
flat_map = False
flat_water = True
ranges =   [0,            10,      20,     25,      40,           60,      70,      noise_max]
features = ["dark_water", "water", "sand", "grass", "dark_grass", "rocky", "snowy", "dark_water"]
#############
# Colors
#############
# Using a dictionary allows easily adding new colors.
colors = {'dark_water': (120, 120, 225),
         'water': (150, 150, 255),
         'sand': (237, 201, 175),
         'grass': (207, 241, 135),
         'dark_grass': (167, 201, 135),
         'rocky': (170, 170, 170),
         'snowy': (255, 255, 255)
         }

# Set this to false when doing a raised map for best results
draw_everything = False

def draw_hexagon(x, y, side, h):
    
    # Top Face
    beginShape()
    vertex((x + side * sin(PI/2), y + side * cos(PI/2) - h))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6) - h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) - h))
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) - h))
    vertex((x + side * sin(7 * PI/6), y + side * cos(7 * PI/6) - h))
    vertex((x + side * sin(5 * PI/6), y + side * cos(5 * PI/6) - h))
    endShape(CLOSE)

    # Bottom Left Face
    beginShape()
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) - h))
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) + h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) + h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) - h))
    endShape()

    # Bottom Front Face
    beginShape()
    vertex((x + side * sin(PI/6), y + side * cos(PI/6) - h))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6) + h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) + h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) - h))
    endShape()

    # Bottom Right Face
    beginShape()
    vertex((x + side * sin(PI/2), y + side * cos(PI/2) - h))
    vertex((x + side * sin(PI/2), y + side * cos(PI/2) + h))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6) + h))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6) - h))
    endShape()
    
def in_range(n, r):
    return n >= r[0] and n < r[1]

# Set tile types based on noise height
def get_tile_type(n): 
    for i in range(len(ranges)):
        # For instance, if n is 5:
        # The first test fails, since 0 < 5
        # The second test passes, since 10 > 5 - this means 
        # our number is between 0 and 10, and so it is dark water.
        # (and we should return index 0)
        if ranges[i] >= n:
            return features[i-1]
    # Default case.
    return features[-1]

# Returns the distance between tiles
def get_distance(tile_one_x, tile_one_y, tile_two_x, tile_two_y):
    return sqrt(pow((tile_one_x - tile_two_x), 2) + pow((tile_one_y - tile_two_y), 2))
    
    
def setup():
    
    # Create the canvas
    size(imgw, imgh)
    background(120, 120, 225)
    
    # Adjust the settings for the noise function
    # noiseDetail(5)
    
    # Take advantage of resolution
    pixelDensity(2)
    
    # Set the border for the hexagon tiles
    if outline_width > 0:
        stroke(outline_color[0], outline_color[1], outline_color[2])
        strokeWeight(outline_width)
    else:
        noStroke()

    
    # Create the empty map for hex tiles
    map_height = int(1.5 * imgh / (.86 * hexagon_size))
    map_width =  int(1.5 * imgw / (hexagon_size * 3))
    
    hex_map = []
    for mh in range(map_height):
        hex_map.append([])
    
    # Assign each tile's position, height, and type
    for i in range(map_height):
        y = i * (.86 * hexagon_size)
        for j in range(map_width):
            if i%2 == 0:
                x = j * (hexagon_size * 3)
            else:
                x = (hexagon_size * 1.5) + j * (hexagon_size * 3)
            
            n = noise((x / noise_loc_mod) * noise_scale, (y / noise_loc_mod) * noise_scale)
 
            # Make custom alterations to the map
            map_center = (imgw/2, imgh/2)

            distance_from_center = get_distance(x, y, map_center[0], map_center[1])

            gradient_perc = distance_from_center/max_distance

            n -= pow(gradient_perc, 3)
            n = max(n, 0)
            
            n *= noise_max
            
            hex_map[i].append((x, y, n, get_tile_type(n)))
            

    # Draw the map based on tile type
    for r in hex_map:
        for c in r:
            noise_height = c[2]
            hex_color = colors[c[3]]
            fill(hex_color[0], hex_color[1], hex_color[2])
            if draw_everything or noise_height > 0:
                if flat_map:
                    noise_height = 0
                    
                if custom_stroke:
                    # Adding strokes based on the base color looks very nice, and less blocky.
                    dark_stroke = [min(255, int(x * 0.5)) for x in hex_color]
                    stroke(dark_stroke[0], dark_stroke[1], dark_stroke[2])

                if flat_water:
                    noise_height = max(20, noise_height)
      
                draw_hexagon(c[0], c[1], hexagon_size, noise_height)

    seed = int(random(10000))
    
    save('Examples/Best/%s.png' % seed)
