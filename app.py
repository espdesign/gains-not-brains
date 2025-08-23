from gym_equipment import Barbell, Gym_equipment

gym = Gym_equipment()
# Preload some plates
for wt, qty in [(45, 4), (35, 2), (25, 2), (15,2),(10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)
print(gym, '\n')
barbell = Barbell(45)


# Example usage
target_weight = 135
try:
    print("Current:", barbell, gym)
    gym.change_weight(barbell, target_weight)
    print("After:", barbell, gym)
except ValueError as e:
    print(e)

# Example usage
target_weight = 165
try:
    print("Current:", barbell, gym)
    gym.change_weight(barbell, target_weight)
    print("After:", barbell, gym)
except ValueError as e:
    print(e)

# Example usage
target_weight = 185
try:
    print("Current:", barbell, gym)
    gym.change_weight(barbell, target_weight)
    print("After:", barbell, gym)
except ValueError as e:
    print(e)
# Example usage
target_weight = 225
try:
    print("Current:", barbell, gym)
    while True:
        if gym.change_weight(barbell, target_weight):
            break
    print("After:", barbell, gym)
except ValueError as e:
    print(e)

target_weight = 215
try:
    print("Current:", barbell, gym)
    while True:
        if gym.change_weight(barbell, target_weight):
            break
    print("After:", barbell, gym)
except ValueError as e:
    print(e)

target_weight = 135
try:
    print("Current:", barbell, gym)
    while True:
        if gym.change_weight(barbell, target_weight):
            break
    print("After:", barbell, gym)
except ValueError as e:
    print(e)