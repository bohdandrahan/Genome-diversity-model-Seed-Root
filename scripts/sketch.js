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
	sliderRange(0, 10, 1);
	gui.addGlobals('mutationRate');
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