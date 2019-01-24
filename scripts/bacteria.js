class Bacteria extends Animal{

  setMaxSpeed(maxspeed = random(2)){
    this.maxspeed = maxspeed 
  }
  setNutritionValues(values = []){
    this.nutritionValues = values 
  }
  setDnaLen(dnaLen = 0){
    this.dnaLen = dnaLen;
  }
  setHealthDrop(hD = 0){
    this.healthDrop = hD
  }
  behavior(groupsToEat, groupsToAvoid){
  }

  display() {
    // Draw a worm

    var theta = this.velocity.heading() + PI / 2;
    push();
    translate(this.position.x, this.position.y);
    colorMode(HSB);
    fill(this.clr%355, 95, 95);
    noStroke();
    ellipse(0,0, 20);
    pop();
  }
}