from collections import Counter
from typing import Union
from itertools import combinations

PlateNumber = Union[int, float]


class Barbell:
    def __init__(self, weight: PlateNumber) -> None:
        self.weight = weight
        self.cur_plate_order = []

    def __repr__(self):
        x = ""
        for i in self.cur_plate_order:
            x += f"[{i}]"
        return f"Barbell:{self.weight + sum(self.cur_plate_order) * 2} lbs | ==={x} |"

    def add_plate(self, plate: PlateNumber):
        if plate > 0:
            self.cur_plate_order.append(plate)
            return True
        else:
            return False

    def pop_plate(self):
        try:
            self.cur_plate_order.pop(-1)
            return True
        except IndexError:
            return False

    def remove_plate(self, plate: int | float):
        try:
            if self.cur_plate_order[-1] == plate:
                self.cur_plate_order.pop(-1)
                return True
            else:
                return False
        except IndexError:
            return False

    def current_load(self):
        return self.weight + sum(self.cur_plate_order) * 2


class Gym_equipment:
    def __init__(self):
        self.plates: Counter[PlateNumber] = Counter()
        self.last_move = []
        self.plan = []

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

    def change_weight(self, barbell: "Barbell", target: PlateNumber):
        # calculate the diffrence of the current barbell weight and the target weight
        diff_half = (
            target - barbell.current_load()
        ) / 2  # the total weight we need to add to each side to reach target weight

        if diff_half > 0:
            # add weights to reach target weight
            # first check for simple add solution
            if diff_half in self.plates:
                barbell.add_plate(diff_half)
                self.plates.subtract(Counter({diff_half: 2}))
                self.plates = self.plates + Counter()  # remove plates that are at 0
                self.last_move = [("ADD", [diff_half])]
                return True
            else:
                # we must look for combinations of available plates that we can add to get to the total weight
                plan = sorted(
                    find_symmetric_plate_combination(self.plates, diff_half),
                    reverse=True,
                )
                # print(plan)
                if plan:
                    # print("Solution Found")
                    for plate in plan:
                        barbell.add_plate(plate)
                        self.plates.subtract(Counter({plate: 2}))
                        self.plates = (
                            self.plates + Counter()
                        )  # remove plates that are at 0
                        self.last_move.append(("ADD", [plate]))

                    return True
                else:
                    # print("Solution not found")
                    # remove outer plates and return false
                    # print(barbell.cur_plate_order)
                    x = barbell.cur_plate_order[-1]  # make note of plate on end
                    self.plates = self.plates + Counter(
                        [barbell.cur_plate_order[-1]] * 2
                    )
                    if barbell.pop_plate():
                        self.last_move = [
                            ("REMOVE", [x])
                        ]  # add removed plate to last_move
                        # print("Removed outer plate, trying again")
                        # print(barbell)
                        return False
                    else:
                        raise ValueError(
                            "No more plates to remove, cannot reach target weight"
                        )

        elif diff_half < 0:
            # remove weights to reach target weight
            # print('Removing Plate to reach target weight')
            # if the last weight added to our barbell is the target diffrence remove plate and return true
            if abs(diff_half) == barbell.cur_plate_order[-1]:
                self.last_move = [
                    ("REMOVE", [barbell.cur_plate_order[-1]])
                ]  # add move to last move
                self.plates = self.plates + Counter(
                    [barbell.cur_plate_order[-1]] * 2
                )  # add plate back to gym supply
                barbell.pop_plate()
                # print('removed last added plate for simple solution')
                return True
            else:
                self.last_move = [
                    ("REMOVE", [barbell.cur_plate_order[-1]])
                ]  # add move to last move
                self.plates = self.plates + Counter(
                    [barbell.cur_plate_order[-1]] * 2
                )  # add plate back to gym supply
                barbell.pop_plate()
                return False

        else:
            raise ValueError("Already at target weight")

        print(f"{diff_half=}")

    def __repr__(self) -> str:
        return f"Gym_equipment(plates={dict(self.plates)})"


def find_symmetric_plate_combination(plates, target):
    # brute force look through combinations of available plates to add.
    # print('Looking for symmetric_combo')
    i = 2
    while True:
        for item in list(combinations(plates, i)):
            if sum(item) == target:
                return list(item)
        i += 1
        if i > 50:
            return list()


def change_barbell_weight(barbell, gym, target_weight):
    gym.plan = []
    try:
        # print("Current:", barbell, gym,)
        # print("Target:", target_weight)
        while not gym.change_weight(barbell, target_weight):
            # print(gym.last_move)
            gym.plan.append(gym.last_move)
            gym.last_move = []
            pass
        # print(gym.last_move)
        gym.plan.append(gym.last_move)
        # print("After:", barbell, gym)
        # print('PLAN:', gym.plan)

    except ValueError as e:
        print(e)
