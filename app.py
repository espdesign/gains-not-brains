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

def load_barbell(target: float, bar_weight: float, current: list[float|int], gym: Gym_equipment):
    """
    target: desired total weight (bar + plates)
    bar_weight: empty barbell weight
    current: list of plate weights already loaded on ONE SIDE
    gym: Gym_equipment object
    
    Returns: list of plates to add (per side) in order, or None if impossible.
    """
    current_total = bar_weight + 2 * sum(current)
    need = target - current_total

    if need < 0:
        return None  # can't unload plates
    if need == 0:
        return []    # already at target

    plan = []
    # work in descending order
    for w in sorted(gym.plates.keys(), reverse=True):
        pair_weight = w * 2
        while need >= pair_weight and gym.plates[w] >= 2:
            plan.append(w)
            need -= pair_weight
            gym.plates[w] -= 2  # use up a pair
        if need == 0:
            return plan

    return None  # not possible

# Example usage:
gym = Gym_equipment()
# Add plates to inventory
for wt, qty in [(45, 4), (35, 2), (25, 2), (15, 2), (10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)

print("Inventory:", gym)

bar_weight = 45
current = [45, 15]  # one 45 per side already on bar (so total=95)

target = 185
plan = load_barbell(target, bar_weight, current, gym)

if plan:
    print(f"To reach {target} lbs, add (per side): {plan}")
else:
    print("Target not achievable with available plates, or no changes needed.")