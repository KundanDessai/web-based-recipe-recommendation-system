import pandas as pd

# Load dataset
df = pd.read_csv("AITRAINX_DATASET_with_flavour.csv")

# Create 'food_type' column if not present
if 'food_type' not in df.columns:
    non_veg_keywords = ["chicken", "mutton", "fish", "egg", "prawn", "shrimp", "meat", "beef"]
    def classify_food_type(ingredients):
        ingredients = str(ingredients).lower()
        return 'nonveg' if any(word in ingredients for word in non_veg_keywords) else 'veg'
    df['food_type'] = df['ingredients_name'].apply(classify_food_type)

# Preprocessing
df["ingredients_name"] = df["ingredients_name"].fillna("").str.lower()
df["cuisine"] = df["cuisine"].fillna("").str.lower()
df["course"] = df["course"].fillna("").str.lower()
df["food_type"] = df["food_type"].fillna("").str.lower()
df["flavor"] = df["flavor"].fillna("").str.lower()

# Main function
def get_top_recipes(user_ingredients, user_cuisine="", user_course="", max_prep_time=None, food_type="", flavor=""):
    user_ingredients = [ing.strip().lower() for ing in user_ingredients.split(",") if ing.strip()]
    if not user_ingredients:
        return []

    filtered_df = df.copy()

    if user_cuisine:
        filtered_df = filtered_df[filtered_df["cuisine"].str.contains(user_cuisine.strip().lower(), na=False)]
    if user_course:
        filtered_df = filtered_df[filtered_df["course"].str.contains(user_course.strip().lower(), na=False)]
    if max_prep_time:
        try:
            max_prep_time = int(max_prep_time)
            filtered_df = filtered_df[filtered_df["prep_time"] <= max_prep_time]
        except ValueError:
            pass
    if food_type:
        filtered_df = filtered_df[filtered_df["food_type"] == food_type.strip().lower()]
    if flavor:
        filtered_df = filtered_df[filtered_df["flavor"] == flavor.strip().lower()]

    def calculate_match_score(recipe_ingredients):
        recipe_ingredients = [ri.strip().lower() for ri in recipe_ingredients.split(",")]
        common = set(user_ingredients).intersection(recipe_ingredients)
        return len(common) / len(user_ingredients)

    filtered_df["match_score"] = filtered_df["ingredients_name"].apply(calculate_match_score)
    result_df = filtered_df[filtered_df["match_score"] > 0]
    top_recipes = result_df.sort_values(by="match_score", ascending=False).head(3)

    return top_recipes.to_dict(orient="records")
