class Groups {
	constructor(dataAboutGroups = [
		[bacteria, 10]
	]) {
		//dataAboutGroups - array where each element is [name, qty]
		this.animals = []
		this.dataAboutGroups = dataAboutGroups
		this.dataAboutGroups.forEach((name_qty, index) => {
			this.animals[index] = []
			for (let i = 0; i < name_qty[1]; i++) {
				let clr = map(i, 0, name_qty[1], 0, 355)
				this.addNewAnimal(this.animals[index], name_qty[0], clr)
			}
			this.birthProb = fertility;
		})
	}
	getDeathProb() {
		return 1 - (carryingCapacity - this.animals[0].length + 1) / carryingCapacity
	}
	addNewAnimal(group, name, clr, x = random(width), y = random(height)) {
		group.push(new name(x, y, null, clr));
	}

	addAnimal(group, animal) {
		group.push(animal)
	}

	behave() {
		this.animals[0].forEach((bacteria) => {
			bacteria.behavior([], [])
		});
	}
	update() {
		this.birthProb = fertility;
		this.animals.forEach((animals, i) => {
			this.children = []
			let deathPrb = this.getDeathProb('')
			animals.forEach((animal, j) => {
				animal.update();
				if (deathPrb > random()) {
					// food.addNewApple(animal.position.x + random(-10,10), animal.position.y + random(-10,10))
					animals.splice(j, 1);
				}

				if (this.birthProb > random()) {
					let child = animal.getChild()
					this.children.unshift(child)
				}
			})
			if (this.children.length > 0) {
				this.children.forEach((child) => {
					this.addAnimal(animals, child)
				})
			}
		})

	}

	display() {
		this.animals.forEach((animals, index) => {
			this.animals[index].forEach((animal, index) => {
				animal.display()
			})
		})
	}
}