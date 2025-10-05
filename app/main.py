#app.py
from flask import Flask, render_template, request, redirect, url_for
from gym_equipment import Barbell, Gym_equipment, change_barbell_weight

app = Flask(__name__)

# Initialize gym equipment and barbell once
gym = Gym_equipment()
# Set gym equipment available
for wt, qty in [(45, 4), (35, 2), (25, 2), (15, 2), (10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)
barbell = Barbell(45)

# A simple in-memory store for the current state (barbell and gym)
# In a real application, you might use a database or session management
current_state = {
    'barbell': barbell,
    'gym': gym
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            target_weight = float(request.form['target_weight'])
            current_barbell = current_state['barbell']
            current_gym = current_state['gym']
            change_barbell_weight(current_barbell, current_gym, target_weight)
        except ValueError as e:
            return render_template('index.html', error=str(e), **current_state)
        except Exception as e:
            return render_template('index.html', error="An unexpected error occurred.", **current_state)

    return render_template('index.html', **current_state)

@app.route('/add_plate/<float:plate_weight>')
def add_plate(plate_weight):
    barbell = current_state['barbell']
    gym = current_state['gym']
    if gym.plates[plate_weight] > 0:
        barbell.add_plate(plate_weight)
        gym.remove_plates(plate_weight, 2)
    return redirect(url_for('index'))

@app.route('/remove_plate/<float:plate_weight>')
def remove_plate(plate_weight):
    barbell = current_state['barbell']
    gym = current_state['gym']
    if barbell.cur_plate_order and barbell.cur_plate_order[-1] == plate_weight:
        barbell.remove_plate(plate_weight)
        gym.add_plates(plate_weight, 2)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


