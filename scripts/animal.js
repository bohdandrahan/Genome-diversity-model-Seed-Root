// http://natureofcode.com
// The "Animal" class

class Animal {
  constructor(x, y, dna = null, clr = 355) {
    this.acceleration = createVector(0, 0);
    this.position = createVector(x, y);
    this.r = 6;
    this.setMaxSpeed();
    this.velocity = createVector(random(-this.maxspeed, this.maxspeed), random(-this.maxspeed, this.maxspeed));
    this.setMaxForce();
    this.setDnaLen();
    this.setDnaCeiling();
    this.setNutritionValues();
    this.setDna(dna);
    this.health = 1;
    this.setMutationRate();
    this.setHealthDrop();
    this.setDirection();
    this.clr = clr
  }
  setNutritionValues(){
    this.nutritionValues = [0.1, -0.1]
  }
  setMaxSpeed(maxspeed = 2){
    this.maxspeed = maxspeed 
  }

  setMaxForce(maxforce = 0.1) {
    this.maxforce = maxforce
  }
  setDnaLen(dnaLen = 2){
    this.dnaLen = dnaLen
  }
  setDnaCeiling(){
    this.dnaCeiling = 2;
    this.dnaCeilingVision = 100
  }
  setDna(dna = null){
    if (!dna){
      this.dna = [];
      for (let i = 0; i < this.dnaLen; i++){
        this.dna.push(random(-this.dnaCeiling, this.dnaCeiling));
      }

      this.dna_vision = [];
      for (let i = 0; i < this.dnaLen; i++){
        this.dna_vision.push(random(0, this.dnaCeilingVision));
      }
    } else{
      this.dna = dna[0]
      this.dna_vision = dna[1]}
  }
  setMutationRate(){
    this.mutationRate = [0.5, 10]
  }
  setHealthDrop(hD = 0.005){
    this.healthDrop = hD
  }
  setDirection(){
    //abstract method, used is CigaretteButt
  }

  // Method to update location
  update() {  
    // Update velocity
    this.velocity.add(this.acceleration);
    // Limit speed
    this.velocity.limit(this.maxspeed);
    this.position.add(this.velocity);
    // Reset accelerationelertion to 0 each cycle
    this.acceleration.mult(0);

    this.health -= this.healthDrop
    this.boundaries()
  }

  applyForce(force) {
    // We could add mass here if we want A = F / M
    this.acceleration.add(force);
  }

  // A method that calculates a steering force towards a target
  // STEER = DESIRED MINUS VELOCITY

  behavior(groupsToEat, groupsToAvoid){
    var steers = []
    groupsToEat.forEach((group, index) =>{
      steers[index] = this.hunt(group, this.nutritionValues[index], this.dna_vision[index])
    })
    groupsToAvoid.forEach((group, index) =>{
      let steer = this.avoid(group, this.dna_vision[index])
      steers.push(steer)
    })
    steers.forEach((steer, index) =>{
      steer.mult(this.dna[index]);
      this.applyForce(steer);
    })
  }
  getChild(){
    let dna = this.getMutatedDna()
    let x = this.position.x
    let y = this.position.y
    let clr = this.clr +random(-3, 3)
    let child = new this.constructor(x, y, dna, clr )
    return child
  }
  getMutatedDna(){
    let mutatedDna = []
    let mutatedDnaVision = []
    this.dna.forEach((dna_, index) => {
      let newDna = dna_ + random(-this.mutationRate[0], this.mutationRate[0]);
      if (newDna < -this.dnaCeiling || newDna > this.dnaCeiling){
        newDna = dna_
      }
      mutatedDna[index] = newDna;
    });
    this.dna_vision.forEach((dna_v, index) =>{
      let newDna_v = dna_v + random(-this.mutationRate[1], this.mutationRate[1]);
      if (newDna_v < 0 || newDna_v > this.dnaCeilingVision){
        newDna_v = dna_v;
      }
      mutatedDnaVision[index] = newDna_v;
    });
    return [mutatedDna, mutatedDnaVision]
  }

  hunt(preys, nutrition, vision){
    let nearest = this.findNearest(preys)
    if (nearest){
      if(this.distanceTo(nearest) < max(this.maxspeed, 7)){
        this.eat(preys, nearest, nutrition)
        return createVector(0,0);
      }else  if (this.distanceTo(nearest) < vision){
        return this.seek(nearest.position);
      }
      else {
        this.boundaries();
        return createVector(0,0);
      }
    }else {
      this.boundaries();
      return createVector(0,0);
    }
  }
  eat(preys, prey, nutrition){
    preys.splice(preys.indexOf(prey), 1);
    this.health += nutrition
  }

  avoid(group, vision){
    let nearest = this.findNearest(group)
    if (nearest){
      if (this.distanceTo(nearest) < vision){
        return this.seek(nearest.position);
      } else{
        return createVector(0,0);
      }
    } else{
      return createVector(0,0);
    }
  }

  findNearest(preys) {
    let record = Infinity;
    let nearest = null;
    for (var i = 0; i < preys.length; i++) {
      let d = this.distanceTo(preys[i]);
      if (d < record){
        record = d;
        nearest = preys[i];
      }
    }
    return nearest;
  }

  isDead(){
    return (this.health < 0)
  }

  distanceTo(object) {
    return this.position.dist(object.position);
  }

  seek(target) {

    var desired = p5.Vector.sub(target, this.position); // A vector pointing from the location to the target

    // Scale to maximum speed
    desired.setMag(this.maxspeed);

    // Steering = Desired minus velocity
    var steer = p5.Vector.sub(desired, this.velocity);
    steer.limit(this.maxforce); // Limit to maximum steering force

    return steer;
  }

  boundaries() {
    let d = 25;

    let desired = null;

    if (this.position.x < d) {
      desired = createVector(this.maxspeed, this.velocity.y);
    } else if (this.position.x > width - d) {
      desired = createVector(-this.maxspeed, this.velocity.y);
    }

    if (this.position.y < d) {
      desired = createVector(this.velocity.x, this.maxspeed);
    } else if (this.position.y > height - d) {
      desired = createVector(this.velocity.x, -this.maxspeed);
    }

    if (desired !== null) {
      desired.normalize();
      desired.mult(this.maxspeed);
      let steer = p5.Vector.sub(desired, this.velocity);
      steer.limit(this.maxforce);
      this.applyForce(steer);
    }
  }

  getHealthColor(){
    return lerpColor(color(255,0,0),color(0,255,0),this.health)
  }


  display() {
    // Draw a triangle rotated in the direction of velocity
    var theta = this.velocity.heading() + PI / 2;
    fill();
    stroke(200);
    strokeWeight(1);
    push();
    translate(this.position.x, this.position.y);
    rotate(theta);
    beginShape();
    vertex(0, -this.r * 2);
    vertex(-this.r, this.r * 2);
    vertex(this.r, this.r * 2);
    endShape(CLOSE);
    pop();
  }

}