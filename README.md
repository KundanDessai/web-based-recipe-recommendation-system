# Web-based Recipe Recommendation System

An intelligent **web-based recipe recommendation system** built using **Python**, **Flask**, and **Bootstrap**. This app suggests the top 3 matching recipes based on ingredients and preferences like **food type**, **cuisine**, **course**, **flavor**, and **prep time**.

---

## Features

- Recommends top 3 recipes based on your **input ingredients**
- Choose between **Vegetarian** and **Non-Vegetarian** options
- Filter by **Cuisine**, **Course**, **Flavor**, and **Prep Time**
- Calculates **ingredient match score** for ranking
- Displays recipe name, ingredients, instructions, prep time, type, and image
- Built with a clean **Bootstrap-based UI** using a glassmorphism effect

---

## Tech Stack

- **Frontend:** HTML, CSS, Bootstrap 5  
- **Backend:** Python (Flask)  
- **Data Source:** CSV recipe dataset  
- **Filtering Logic:** Rule-based ingredient matching

---

## How to Run

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/KundanDessai/web-based-recipe-recommendation-system.git
    cd web-based-recipe-recommendation-system
    ```

2. **Create a Virtual Environment (recommended)**  
    ```bash
    python -m venv venv
    source venv/bin/activate        # Mac/Linux
    venv\Scripts\activate           # Windows
    ```

3. **Install Dependencies**  
    ```bash
    pip install flask pandas
    ```

4. **Ensure Dataset is Present**  
    - Make sure `AITRAINX_DATASET_with_flavour.csv` is in the root directory.

5. **Run the Flask Server**  
    ```bash
    python app.py
    ```

6. **Access the Application**  
    - Open your browser and go to:  
    ```
    http://localhost:5000
    ```

---

## Future Improvements

- Add screenshot gallery of results  
- Improve ingredient matching with NLP models    
- Deploy on Render or Replit  
- User login & favorite recipes  
- Voice input or image-based ingredient detection


