// http://natureofcode.com
// Implements Craig Reynold's autonomous steering behaviors
// See: http://www.red3d.com/cwr/
let groups;
let height;
let width;

//gui
let gui;
//dynamic parameters
var mutationRate = 2;
var fertility = 0.1;
var carryingCapacity = 5000

function mousePressed() {
	mouseDragged();
}

function mouseDragged() {
	newAnimal = new Bacteria(mouseX, mouseY, null, random(360))
	groups.addAnimal(groups.animals[0], newAnimal)
}


function setup() {
	height = 0.95 * windowHeight;
	width = 0.95 * windowWidth;
	let canvas = createCanvas(width, height);
	canvas.parent('sketch-holder')

	groups = new Groups([
		[Bacteria, 1]
	]);

	gui = createGui('Parameters');
	colorMode(HSB);
	sliderRange(0, 30, 1);
	gui.addGlobals('mutationRate');
	sliderRange(0, 0.3, 0.001);
	gui.addGlobals('fertility');
	sliderRange(1, 10000, 1);
	gui.addGlobals('carryingCapacity');

	colorMode(RGB);

}

function draw() {
	background(77, 77, 77);
	groups.behave();
	groups.update();
	groups.display();

}

function windowResized() {
	width = 0.95 * windowWidth;
	height = 0.95 * windowHeight
	resizeCanvas(width, height);
}