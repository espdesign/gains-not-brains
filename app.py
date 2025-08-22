from gym_equipment import Gym_equipment, load_barbell, unload_barbell
from flask import Flask, render_template, request

app = Flask(__name__)
gym = Gym_equipment()

# Preload some plates
for wt, qty in [(45, 4), (35, 2), (25, 2), (15,2),(10, 2), (5, 2), (2.5, 2)]:
    gym.add_plates(wt, qty)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    current_load = []
    target_weight = 0
    bar_weight = 45  # default bar

    if request.method == "POST":
        try:
            bar_weight = float(request.form.get("bar_weight", 45))
            target_weight = float(request.form.get("target_weight", 0))
            current_load_str = request.form.get("current_load", "")
            # Convert comma-separated input into list of floats
            current_load = [float(x.strip()) for x in current_load_str.split(",") if x.strip()]

            if target_weight > bar_weight + 2*sum(current_load):
                # Need to load
                result = load_barbell(target_weight, bar_weight, current_load, gym)
            else:
                # Need to unload
                result = unload_barbell(target_weight, bar_weight, current_load)

        except Exception as e:
            result = {"error": str(e)}

    return render_template(
        "index.html",
        plates=gym.plates,
        current_load=current_load,
        target_weight=target_weight,
        bar_weight=bar_weight,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
