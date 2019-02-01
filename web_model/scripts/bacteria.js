class Bacteria extends Animal {

	setMaxSpeed(maxspeed = random(10)) {
		this.maxspeed = maxspeed
	}
	setNutritionValues(values = []) {
		this.nutritionValues = values
	}
	setDnaLen(dnaLen = 0) {
		this.dnaLen = dnaLen;
	}
	setMaxForce(maxforce = 0.5) {
		this.maxforce = maxforce
	}

	setHealthDrop(hD = 0) {
		this.healthDrop = hD
	}
	behavior(groupsToEat, groupsToAvoid) {}

	display() {
		// Draw a worm

		var theta = this.velocity.heading() + PI / 2;
		push();
		translate(this.position.x, this.position.y);
		colorMode(HSB);
		fill(this.clr, 95, 95);
		noStroke();
		ellipse(0, 0, 20);
		pop();
	}
}