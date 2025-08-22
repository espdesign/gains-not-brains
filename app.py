class Gym:
    def __init__(self):
        self.plates = []
        self.barbells = []

    def add_equipment(self, equipment:list):
        for item in equipment:
            if isinstance(item, Plate):
                print(f'Adding Plate: {item.weight} lbs')
                self.plates.append(item)

            elif isinstance(item, Barbell):
                print(f'Adding Barbell: {item.weight} lbs')
                self.barbells.append(item)
            else:
                raise TypeError(f"Cannot add equipment of unknown type {type(item)}")
            
    def remove_equipment(self, equipment:list):
        for item in equipment:
            if isinstance(item, Plate):
                print(f'Removing Plate: {item.weight} lbs')
                copy_plates = self.plates[:]
                i = 0
                while i < len(copy_plates):
                    if isinstance(copy_plates[i], Plate):
                        if copy_plates[i].weight == item.weight:
                            print(f"removing {i=}")
                            copy_plates.pop(i)

                            self.plates = copy_plates[:]
                            break
                        i += 1

            elif isinstance(item, Barbell):
                print(f'Removing Barbell: {item.weight} lbs')
                copy_barbell = self.barbells[:]
                i = 0
                while i < len(copy_barbell):
                    if isinstance(copy_barbell[i], Barbell):
                        if copy_barbell[i].weight == item.weight:
                            copy_barbell.pop(i)
                            self.barbells = copy_barbell[:]
                            break
                        i += 1
            else:
                raise TypeError(f"Cannot remove equipment of unknown type {type(item)}")


class Plate:
    def __init__(self, weight:int):
        self.weight = weight
    def __repr__(self):
        return f'<Plate {self.weight} >'

class Barbell:
    def __init__(self, weight):
        self.weight = weight
    def __repr__(self):
        return f'<Barbell {self.weight}>'

# Test Usage
gym = Gym()
plate_45 = "Plate(45)"

gym.add_equipment([Plate(45), Plate(45), Plate(10), Plate(15)])
gym.add_equipment([Barbell(45), Barbell(15)])
print(gym.barbells, gym.plates)
gym.remove_equipment([Plate(45), Barbell(15), Plate(45), Plate(15), Plate(10), Plate(10), Plate(15), Barbell(20), Barbell(45)])
gym.add_equipment([Barbell(45), Plate(45)])

print(gym.barbells, gym.plates)


print(Barbell(45))