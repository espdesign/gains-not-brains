from gym_equipment import Barbell, Gym_equipment

gym = Gym_equipment()
# Preload some plates
for wt, qty in [(45, 4), (35, 2), (25, 2), (15,2),(10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)
print(gym, '\n')

barbell = Barbell(45)
print('adding Plate 45')
barbell.add_plate(45)
print(barbell)
print('adding Plate 25')
barbell.add_plate(25)
print(barbell)
print('Removing Plate 25')
barbell.remove_plate(25)
print(barbell)
barbell.add_plate(2.5)
print(barbell)
