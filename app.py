from gym_equipment import Barbell, Gym_equipment, change_barbell_weight

gym = Gym_equipment()
# Set gym equipment available
for wt, qty in [(45, 4), (35, 2), (25, 2), (15, 2), (10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)
print(gym, "\n")
barbell = Barbell(45)


# Example usage
for target in [135, 165, 185, 225, 215, 135]:
    print(f"{barbell}")
    print(f"{target=}")
    change_barbell_weight(barbell, gym, target)
    print(f"{gym.plan}")
    print(f"{barbell}")
    print("\n")
