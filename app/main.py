#app.py
from flask import Flask, render_template, request, redirect, url_for, session
from gym_equipment import Barbell, Gym_equipment, change_barbell_weight
import os
from collections import Counter

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_current_state():
    if 'barbell' not in session or 'gym' not in session:
        gym = Gym_equipment()
        for wt, qty in [(45, 4), (35, 2), (25, 2), (15, 2), (10, 2), (5, 2), (2.5, 2)]:
            gym.add_plates(wt, qty)
        barbell = Barbell(45)
        session['barbell'] = barbell.__dict__
        session['gym'] = gym.__dict__
    
    barbell_data = session['barbell']
    gym_data = session['gym']

    barbell = Barbell(barbell_data['weight'])
    barbell.cur_plate_order = barbell_data['cur_plate_order']

    gym = Gym_equipment()
    gym.plates = Counter({float(k): v for k, v in gym_data['plates'].items()})
    gym.last_move = gym_data['last_move']
    gym.plan = gym_data['plan']
    
    return {'barbell': barbell, 'gym': gym}

@app.route('/', methods=['GET', 'POST'])
def index():
    current_state = get_current_state()
    if request.method == 'POST':
        try:
            target_weight = float(request.form['target_weight'])
            current_barbell = current_state['barbell']
            current_gym = current_state['gym']
            change_barbell_weight(current_barbell, current_gym, target_weight)
            session['barbell'] = current_barbell.__dict__
            session['gym'] = current_gym.__dict__
        except ValueError as e:
            return render_template('index.html', error=str(e), **current_state)
        except Exception as e:
            return render_template('index.html', error="An unexpected error occurred.", **current_state)

    return render_template('index.html', **current_state)

@app.route('/add_plate/<float:plate_weight>')
def add_plate(plate_weight):
    current_state = get_current_state()
    barbell = current_state['barbell']
    gym = current_state['gym']
    if gym.plates[plate_weight] > 0:
        barbell.add_plate(plate_weight)
        gym.remove_plates(plate_weight, 2)
        session['barbell'] = barbell.__dict__
        session['gym'] = gym.__dict__
    return redirect(url_for('index'))

@app.route('/remove_plate/<float:plate_weight>')
def remove_plate(plate_weight):
    current_state = get_current_state()
    barbell = current_state['barbell']
    gym = current_state['gym']
    if barbell.cur_plate_order and barbell.cur_plate_order[-1] == plate_weight:
        barbell.remove_plate(plate_weight)
        gym.add_plates(plate_weight, 2)
        session['barbell'] = barbell.__dict__
        session['gym'] = gym.__dict__
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')