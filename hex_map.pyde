w, h = 1000, 1000

hexagon_side = 25
noise_scale = .02

line_width = 1


def draw_hexagon(x, y, side, h):
    point(x, y)
    beginShape()
    vertex((x + side * sin(PI/2), y + side * cos(PI/2)))
    vertex((x + side * sin(PI/6), y + side * cos(PI/6)))
    vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6)))
    vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2)))
    vertex((x + side * sin(7 * PI/6), y + side * cos(7 * PI/6)))
    vertex((x + side * sin(5 * PI/6), y + side * cos(5 * PI/6)))
    endShape(CLOSE)
    


    
    # for v in range(len(verts) - 1):
    #     line(verts[v][0], verts[v][1], verts[v+1][0], verts[v+1][1])
    
    # line(verts[len(verts) - 1][0], verts[len(verts) - 1][1], verts[0][0], verts[0][1])

def setup():
    size(w, h)
    strokeWeight(line_width)
    
    stroke(0, 0, 0)
   
    colorMode(HSB, 360, 40, 40);
         
    for i in range(25):
        y = i * ((.86 * hexagon_side))
        for j in range(10):
            if (i%2 == 0):
                x = j * (hexagon_side * 3)
            else:
                x = (hexagon_side * 1.5) + j * (hexagon_side * 3)
            
            n = int(noise(x * noise_scale, y * noise_scale) * 100 / 2)
            print(n)
            for l in range(n):
                fill(noise(x * noise_scale, y * noise_scale) * 360, 70, 70)
                draw_hexagon(x, y - l, hexagon_side, 0)


    
    # for i in range(100):
    #     start_x = 0
    #     start_y = i * ((.86 * hexagon_side) * 2) - 600
        
    #     for j in range(100):
    #         for h in range(int(random(2))):
    #             draw_hexagon(start_x + j * (hexagon_side * 1.5), start_y + j * (.86 * hexagon_side) - h, hexagon_side, 0)

    # start_x = 0
    # start_y = (.86 * hexagon_side) * 2
    
    # for i in range(10):
    #     draw_hexagon(start_x + i * (hexagon_side * 1.5), start_y + i * (.86 * hexagon_side), hexagon_side, 0)
    
    
    
    # draw_hexagon(325, 207, 50, 0)
    # draw_hexagon(250, 164, 50, 0)

    # draw_hexagon(250, 250, 50, 0)
    
