imgw, imgh = 1000, 1000

hexagon_side = 15
noise_scale = .02

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
    
    # fill(30, 30, 30)
    
    # Bottom Left Face
    beginShape()
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) - h))
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) + h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) + h))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) - h))
    endShape()
    
    # fill(80, 80, 80)
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
    
    for i in range(map_height):
        y = i * ((.86 * hexagon_side))
        for j in range(map_width):
            if (i%2 == 0):
                x = j * (hexagon_side * 3)
            else:
                x = (hexagon_side * 1.5) + j * (hexagon_side * 3)
            
            n = int(noise((x / 4) * noise_scale, (y / 4) * noise_scale) * 130)

            fill(70, 40, noise(x * noise_scale, y * noise_scale) * 369)
            draw_hexagon(x, y, hexagon_side, n)


    
    # draw_hexagon(325, 207, 50, 0)
    # draw_hexagon(250, 164, 50, 0)

    # draw_hexagon(250, 250, 100, 6)
    
    save('Examples/blood-red-' + str(int(random(1000))) + '.png')
    
