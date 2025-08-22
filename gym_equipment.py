from collections import Counter
from typing import Union

PlateNumber = Union[int, float]

class Barbell:
    def __init__(self, weight: PlateNumber) -> None:
        self.weight = weight
        self.cur_plate_order = []

    def __repr__(self):
        return f"Barbell:{self.weight + sum(self.cur_plate_order)*2} lbs | {list(reversed(self.cur_plate_order))}------{self.cur_plate_order}"  
      
    def add_plate(self, plate: PlateNumber):
        if plate > 0:
            self.cur_plate_order.append(plate)
            return True
        else:
            return False

    def remove_plate(self, plate:int|float):
        try:
            if self.cur_plate_order[-1] == plate:
                self.cur_plate_order.pop(-1)
                return True
            else:
                return False
        except IndexError:
            return False
            
        
class Gym_equipment:
    def __init__(self):
        self.plates: Counter[PlateNumber] = Counter()

    def add_plates(self, plate_type: PlateNumber, quantity: int):
        if quantity > 0:
            self.plates[plate_type] += quantity
        else:
            raise ValueError("Quantity to add must be positive.")

    def remove_plates(self, plate_type: PlateNumber, quantity: int):
        if quantity > 0:
            if self.plates[plate_type] >= quantity:
                self.plates[plate_type] -= quantity
            else:
                raise ValueError(f"Not enough {plate_type} plates to remove.")
        else:
            raise ValueError("Quantity to remove must be positive.")

    def total_plate_weight(self) -> PlateNumber:
        return sum(weight * count for weight, count in self.plates.items())

    def __repr__(self) -> str:
        return f"Gym_equipment(plates={dict(self.plates)})"

