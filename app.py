from gym_equipment import Gym_equipment, load_barbell, unload_barbell

gym = Gym_equipment()
for wt, qty in [(45, 6), (35, 2), (25, 2), (10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)

bar_weight = 45
current_load = [45]  # per side

# Load to 165
plan_load = load_barbell(165, bar_weight, current_load, gym)
print("Load plan:", plan_load)

# Unload from [45, 25, 10] to 135
current_load = [45, 25, 10]
plan_unload = unload_barbell(135, bar_weight, current_load)
print("Unload plan:", plan_unload)
