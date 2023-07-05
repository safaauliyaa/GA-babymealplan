from flask import Flask, render_template, request, redirect,url_for,jsonify
from GAmodel import *

app = Flask(__name__)

@app.route('/')
def index():
    # Mengembalikan halaman HTML menggunakan fungsi render_template
    return render_template('home.html')


@app.route("/mealplan",methods =["GET", "POST"])
def meal_plan():
    if (request.method == "POST"):
        mealplans,listNutritionTarget=final(int(request.form['usia']),float(request.form['berat_badan']),float(request.form['tinggi_badan']), request.form['gender'])
        labelMenu=["Pagi", "Siang", "Malam"]
        labelNutrisi=["karbohidrat","lemak","protein","fiber"]
        imageNutrisi=["karbo.jpg","fat.jpg","prot.jpg","fiber.jpg"]
        image=["https://images.unsplash.com/photo-1593100164369-e90cdff9678a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1167&q=80","https://images.unsplash.com/photo-1471938537155-7de0bd123d0c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80","https://images.unsplash.com/photo-1629822937307-ce27f951e385?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80",]
        totCaloriesMealPlan=[round(mealplans[0]['Energi (kal)'].sum(),1), round(mealplans[1]['Energi (kal)'].sum(),1),round(mealplans[2]['Energi (kal)'].sum(),1)]
        return render_template('mealplan.html', listMealPlan=mealplans, labelMenu=labelMenu, imageList=image, listNutritionTarget=listNutritionTarget,labelNutrisi=labelNutrisi,imageNutrisi=imageNutrisi,totCaloriesMealPlan=totCaloriesMealPlan)


if __name__ == '__main__':
    app.run(debug=True) 