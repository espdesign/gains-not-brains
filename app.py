from gym_equipment import Barbell, Gym_equipment

gym = Gym_equipment()
# Preload some plates
for wt, qty in [(45, 4), (35, 2), (25, 2), (15,2),(10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)
print(gym, '\n')
barbell = Barbell(45)


def attempt_weight_change(barbell, gym, target_weight):
    try:
        print("Current:", barbell, gym,)
        print("Target:", target_weight)
        while not gym.change_weight(barbell, target_weight):
            #print(gym.last_move)
            gym.plan.append(gym.last_move)
            gym.last_move = []
            pass
        #print(gym.last_move)
        gym.plan.append(gym.last_move)
        print("After:", barbell, gym)
        print('PLAN:', gym.plan)
        
    except ValueError as e:
        print(e)


# Example usage
for target in [135, 165, 185, 225, 215, 135]:
    attempt_weight_change(barbell, gym, target)
    gym.last_move = []
    gym.plan = []
    print('\n')

