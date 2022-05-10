animals = ["Bird", "Fox", "Cat", "Rat", "Alligator"]

animals.append("Giraffe")

moreAnimals = ["monkey", "ant eater", "red panda"]

animals.extend(moreAnimals)

animals.insert(4, "snake")

animals.pop(3)  #removes stuff idk

animals.remove("snake")

del animals[2]


for counter in animals:
    print(counter)

