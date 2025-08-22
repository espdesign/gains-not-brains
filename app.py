from collections import Counter

class Gym_equipment:
    def __init__(self):
        self.plates = Counter()
        self.barbells = Counter()

    def add_barbells(self, weight:int|float, quantity:int):
        """Adds a specified quantity of barbells of a certain weight."""
        if quantity > 0:
            self.barbells[weight] += quantity
            print(f"Added {quantity}, {weight} barbell(s).")
        else:
            print("Quantity to add must be positive.")

    def remove_barbells(self, weight:int|float, quantity:int):
        """Removes a specified quantity of barbells of a certain weight."""
        if quantity > 0:
            if self.barbells[weight] >= quantity:
                self.barbells[weight] -= quantity
                print(f"Removed {quantity}, {weight} barbell(s).")
            else:
                print(f"Not enough {weight} barbells to remove.")
        else:
            print("Quantity to remove must be positive.")

    def add_plates(self, weight:int|float, quantity:int):
        """Adds a specified quantity of plates of a certain weight."""
        if quantity > 0:
            self.plates[weight] += quantity
            print(f"Added {quantity}, {weight} plate(s).")
        else:
            print("Quantity to add must be positive.")

    def remove_plates(self, weight:int|float, quantity:int):
        """Removes a specified quantity of plates of a certain weight."""
        if quantity > 0:
            if self.plates[weight] >= quantity:
                self.plates[weight] -= quantity
                print(f"Removed {quantity}, {weight} plate(s).")
            else:
                print(f"Not enough {weight} plates to remove.")
        else:
            print("Quantity to remove must be positive.")
    def total_plate_weight(self):
        return sum(weight * count for weight, count in self.plates.items())

    def __repr__(self):
        return f"Gym_equipment(plates={dict(self.plates)}, barbells={dict(self.barbells)})"

def load_barbell(target: float, bar_weight: float, current: list[float]|list[int], gym: Gym_equipment):
    """
    Add plates until the target is reached (no removals).
    
    Returns:
        {"add": [plates to add per side],
         "new_state": [final plates per side]}
    or None if impossible.
    """
    current_total = bar_weight + 2 * sum(current)
    need = target - current_total

    if need < 0:
        return None  # can't unload here
    if need == 0:
        return {"add": [], "new_state": current[:]}

    plan_add = []
    new_state = current[:]

    for w in sorted(gym.plates.keys(), reverse=True):
        pair_weight = w * 2
        while need >= pair_weight and gym.plates[w] >= 2:
            plan_add.append(w)
            new_state.append(w)
            need -= pair_weight
            gym.plates[w] -= 2
        if need == 0:
            return {"add": plan_add, "new_state": new_state}

    return None  # not possible


def unload_barbell(target: float, bar_weight: float, current: list[float]|list[int]):
    """
    Remove plates until the target is reached.
    
    Returns:
        {"remove": [plates removed per side],
         "new_state": [final plates per side]}
    or None if impossible.
    """
    current_total = bar_weight + 2 * sum(current)
    diff = current_total - target

    if diff < 0:
        return None  # can't unload to go heavier
    if diff == 0:
        return {"remove": [], "new_state": current[:]}

    plan_remove = []
    new_state = current[:]

    # Work outermost first (heaviest first is a safe approximation)
    for w in sorted(current, reverse=True):
        pair_weight = w * 2
        if diff >= pair_weight and w in new_state:
            plan_remove.append(w)
            new_state.remove(w)
            diff -= pair_weight
        if diff == 0:
            return {"remove": plan_remove, "new_state": new_state}

    return None  # couldn't reach target exactly


# Example usage:
gym = Gym_equipment()
for wt, qty in [(45, 6), (35, 2), (25, 2), (10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)

bar_weight = 45
current = [25]  # per side → total = 95

print("Current total:", bar_weight + 2*sum(current))

# Case 1: load up to 200
plan = load_barbell(200, bar_weight, current[:], gym)
print("Load plan:", plan)

# Case 2: unload down to 135 (from [45,25,10] per side = 205)
current2 = [45, 25, 10]
plan2 = unload_barbell(135, bar_weight, current2)
print("Unload plan:", plan2)
