imgw, imgh = 1000, 1000

hexagon_side = 20
noise_scale = .05

line_width = 1


def draw_hexagon(x, y, side, h):
    point(x, y)
    
    # Top Face
    beginShape()
    vertex((x + side * sin(PI/2), y + side * cos(PI/2) - h))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6) - h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) - h))
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) - h))
    vertex((x + side * sin(7 * PI/6), y + side * cos(7 * PI/6) - h))
    vertex((x + side * sin(5 * PI/6), y + side * cos(5 * PI/6) - h))
    endShape(CLOSE)
    
    fill(0, 0, 0)
    
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
    


    
    # for v in range(len(verts) - 1):
    #     line(verts[v][0], verts[v][1], verts[v+1][0], verts[v+1][1])
    
    # line(verts[len(verts) - 1][0], verts[len(verts) - 1][1], verts[0][0], verts[0][1])

def setup():
    size(imgw, imgh)
    strokeWeight(line_width)
    pixelDensity(2)
    
    
    stroke(0, 0, 0)

    fill(200, 60, 60)
    
    map_height = int(1.5 * imgh / (.86 * hexagon_side))
    map_width =  int(1.5 * imgw / (hexagon_side * 3))
    
    hex_map = []
    for mh in range(map_height):
        hex_map.append([])
    
    for i in range(map_height):
        y = i * ((.86 * hexagon_side))
        for j in range(map_width):
            if (i%2 == 0):
                x = j * (hexagon_side * 3)
            else:
                x = (hexagon_side * 1.5) + j * (hexagon_side * 3)
            
            hex_map[i].append((j, i, x, y))

    for r in hex_map:
        for c in r:
            n = int(noise(c[0] * noise_scale, c[1] * noise_scale) * 150)
            print(n)

            fill(70, 40, noise(c[0] * noise_scale, c[1] * noise_scale) * 369)
            draw_hexagon(c[2], c[3], hexagon_side, n)
    
    # draw_hexagon(325, 207, 50, 0)
    # draw_hexagon(250, 164, 50, 0)

    # draw_hexagon(250, 250, 100, 6)
    
    save('Examples/smooth-blue-' + str(int(random(1000))) + '.png')
    
