from collections import Counter
from typing import Sequence, Union, Optional

Number = Union[int, float]

class Gym_equipment:
    def __init__(self):
        self.plates: Counter[Number] = Counter()
        self.barbells: Counter[Number] = Counter()

    def add_plates(self, plate_type: Number, quantity: int):
        if quantity > 0:
            self.plates[plate_type] += quantity
        else:
            raise ValueError("Quantity to add must be positive.")

    def remove_plates(self, plate_type: Number, quantity: int):
        if quantity > 0:
            if self.plates[plate_type] >= quantity:
                self.plates[plate_type] -= quantity
            else:
                raise ValueError(f"Not enough {plate_type} plates to remove.")
        else:
            raise ValueError("Quantity to remove must be positive.")

    def total_plate_weight(self) -> Number:
        return sum(weight * count for weight, count in self.plates.items())

    def __repr__(self) -> str:
        return f"Gym_equipment(plates={dict(self.plates)}, barbells={dict(self.barbells)})"


def load_barbell(
    target: Number,
    bar_weight: Number,
    current: Sequence[Number],
    gym: Gym_equipment
) -> Optional[dict[str, Sequence[Number]]]:
    """
    Add plates until target is reached (no removals).

    Returns a dict with:
        "add": plates added per side
        "new_state": final plates per side
    or None if impossible.
    """
    current_total = bar_weight + 2 * sum(current)
    need = target - current_total

    if need < 0:
        return None
    if need == 0:
        return {"add": [], "new_state": list(current)}

    plan_add: list[Number] = []
    new_state: list[Number] = list(current)

    for w in sorted(gym.plates.keys(), reverse=True):
        pair_weight = w * 2
        while need >= pair_weight and gym.plates[w] >= 2:
            plan_add.append(w)
            new_state.append(w)
            need -= pair_weight
            gym.plates[w] -= 2
        if need == 0:
            return {"add": plan_add, "new_state": new_state}

    return None


def unload_barbell(
    target: Number,
    bar_weight: Number,
    current: Sequence[Number]
) -> Optional[dict[str, Sequence[Number]]]:
    """
    Remove plates until target is reached.

    Returns a dict with:
        "remove": plates removed per side
        "new_state": final plates per side
    or None if impossible.
    """
    current_total = bar_weight + 2 * sum(current)
    diff = current_total - target

    if diff < 0:
        return None
    if diff == 0:
        return {"remove": [], "new_state": list(current)}

    plan_remove: list[Number] = []
    new_state: list[Number] = list(current)

    # Remove outermost/heaviest plates first
    for w in sorted(current, reverse=True):
        pair_weight = w * 2
        if diff >= pair_weight and w in new_state:
            plan_remove.append(w)
            new_state.remove(w)
            diff -= pair_weight
        if diff == 0:
            return {"remove": plan_remove, "new_state": new_state}

    return None
