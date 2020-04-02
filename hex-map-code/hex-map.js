p5.disableFriendlyErrors = true;

const opts = {
  // Generation Details
  height: 1200,
  tile_size: 10,
  outline: true,
  outline_width: 1,
  noise_mod: 1,
  noise_scale: .01,
  noise_max: 120,
  island_size: .62,
  
  // Initial Colors
  dark_water: [120, 120, 225], // RGB array
  light_water: [150, 150, 255],
  sand: [237, 201, 175],
  grass: [207, 241, 135],
  forest: [167, 201, 135],
  rocks: [170, 170, 170],
  snow: [255, 255, 255],
  outline_color: '#918585',
  
  // Initial Height Ranges
  snow_height: .9,
  rocks_height:.6,
  forest_height:.49,
  grass_height: .36, 
  sand_height: .26,
  light_water_height: .23,
  dark_water_height: .13,
  
  // Additional Functions
  randomize: () => randomize(),
  save: () => save()
};

window.onload = function() {
  var gui = new dat.GUI({width:300});
  // gui.remember(opts)
  var general = gui.addFolder('Generation Details')
  general.open()
  general.add(opts, 'height', 500, 2000).onChange(setup);
  general.add(opts, 'tile_size', 2, 20).onChange(setup);
  
  general.add(opts, 'outline_width', 1, 5).onChange(setup);
  
  general.add(opts, 'island_size', 0, 2).onChange(setup);
  general.add(opts, 'noise_scale', 0, .04).onChange(setup);
  general.add(opts, 'noise_mod', 1, 3).onChange(setup);
  general.addColor(opts, 'outline_color').onChange(setup);
  general.add(opts, 'outline').onChange(setup);
  
  var colors = gui.addFolder('Biome Colors');
  colors.open()
  colors.addColor(opts, 'snow').onChange(setup)
  colors.addColor(opts, 'rocks').onChange(setup)
  colors.addColor(opts, 'forest').onChange(setup)
  colors.addColor(opts, 'grass').onChange(setup)
  colors.addColor(opts, 'sand').onChange(setup)
  colors.addColor(opts, 'light_water').onChange(setup)
  colors.addColor(opts, 'dark_water').onChange(setup)
 

  var heights = gui.addFolder('Height Ranges');
  heights.open()
  heights.add(opts, 'snow_height', 0, 1).onChange(setup)
  heights.add(opts, 'rocks_height', 0, 1).onChange(setup)
  heights.add(opts, 'forest_height', 0, 1).onChange(setup)
  heights.add(opts, 'grass_height', 0, 1).onChange(setup)
  heights.add(opts, 'sand_height', 0, 1).onChange(setup)
  heights.add(opts, 'light_water_height', 0, 1).onChange(setup)
  heights.add(opts, 'dark_water_height', 0, 1).onChange(setup)

  gui.add(opts, "randomize").name("Randomize");
  gui.add(opts, "save").name("Save");

 
};

function randomize() {
  noiseSeed()
  setup()
}

function save() {
  save('photo.png');
}

function setup()
{
  var canvasDiv = document.getElementById('sketchdiv');
  var width = canvasDiv.offsetWidth;
  var height = opts.height;

  pixelDensity(2);
  
  var cnv = createCanvas(width, height);
  cnv.parent('sketchdiv');
  
  background(255)
  strokeWeight(1);
  stroke(0);
  
  draw_hexagon(30, 30, 30, 3);
  
  var hexagon_size = opts.tile_size
  
  // var map_height = 8
  // var map_width = 7
  var map_height = int(1.5 * height / (.86 * hexagon_size))
  var map_width =  int(1.5 * width / (hexagon_size * 3))
  
  var hex_map = []
  for(i = 0; i < map_height ; i++) { 
    hex_map.push([])
  }
  
  var y = 0
  var x = 0

  for (i = 0; i < map_height; i++) {
    y = i * (.86 * hexagon_size)
    for (j = 0; j < map_width; j++) {
      if (i%2 == 0) {
        x = j * (hexagon_size * 3)
      } else {
        x = (hexagon_size * 1.5) + j * (hexagon_size * 3)
      }
      
      // Calculate initial noise value
      let noiseVal = noise((x / opts.noise_mod)*opts.noise_scale, (y / opts.noise_mod)*opts.noise_scale);
      
      
      // Adjust for distance if desired
      let dist = sqrt(pow((x - width/2), 2) + pow((y - height/2), 2))
      let grad = dist / (opts.island_size * min(width, height))
      
      noiseVal -= pow(grad, 3)
      noiseVal = max(noiseVal, 0)
      
      hex_map[i].push([x, y, noiseVal])
    }
  }
  
  for (r = 0; r < hex_map.length; r++) {
    for (c = 0; c < hex_map[r].length; c++) {
      var t = hex_map[r][c]
      draw_hexagon(t[0], t[1], hexagon_size, t[2], 0)
    }
  }
  
}


function draw_hexagon(x, y, side, n, h) {
    let v = int(n * 255.0)
    let c;
    if (v < opts.dark_water_height * 255) {
      c = opts.dark_water;
    } else if(v < opts.light_water_height * 255) {
      c = opts.light_water;
    } else if (v < opts.sand_height * 255) {
      c = opts.sand;
    } else if (v < opts.grass_height * 255) {
      c = opts.grass
    } else if (v < opts.forest_height * 255) {
      c = opts.forest;
    } else if (v < opts.rocks_height * 255) {
      c = opts.rocks;
    } else {
      c = opts.snow;
    }
  
    fill(c)
    
    strokeWeight(opts.outline_width);
    if (opts.outline) {
      stroke(opts.outline_color);
    } else {
      stroke(c)
    }
    
    beginShape()
    vertex(x + side * sin(PI/2), y + side * cos(PI/2) - h)
    vertex(x + side * sin(PI/6), y + side * cos(PI/6) - h)
    vertex(x + side * sin(11 * PI/6), y + side * cos(11 * PI/6) - h)
    vertex(x + side * sin(3 * PI/2), y + side * cos(3 * PI/2) - h)
    vertex(x + side * sin(7 * PI/6), y + side * cos(7 * PI/6) - h)
    vertex(x + side * sin(5 * PI/6), y + side * cos(5 * PI/6) - h)
    endShape(CLOSE)
  
}