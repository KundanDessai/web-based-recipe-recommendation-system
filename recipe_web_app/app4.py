from flask import Flask, render_template, request
from model.recommender import get_top_recipes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    no_match = False
    if request.method == "POST":
        ingredients = request.form.get("ingredients", "")
        cuisine = request.form.get("cuisine", "")
        course = request.form.get("course", "")
        prep_time = request.form.get("prep_time", "")
        food_type = request.form.get("food_type", "")
        flavor = request.form.get("flavor", "")
        
        recipes = get_top_recipes(ingredients, cuisine, course, prep_time, food_type, flavor)
        if not recipes:
            no_match = True

    return render_template("index.html", recipes=recipes, no_match=no_match)

if __name__ == '__main__':
    app.run(debug=True)
