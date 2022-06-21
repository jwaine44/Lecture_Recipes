from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/display/recipe')
def display_recipe():
    if User.validate_session():
        return render_template("recipe.html")
    else:
        return redirect('/')

@app.route('/recipe/new', methods=['POST'])
def create_recipe():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'created_at': request.form['created_at'],
        'under_thirty': request.form['under_thirty'],
        'user_id': session['user_id']
    }

    Recipe.create(data)

    return redirect('/dashboard')

@app.route('/dashboard')
def get_recipes():
    if User.validate_session():
        recipes = Recipe.get_all()
        return render_template('dashboard.html', recipes = recipes)
    else:
        return redirect('/')

@app.route('/recipe/<int:id>')
def get_recipe(id):
    if User.validate_session():
        data = {
            "id": id
        }
        recipe = Recipe.get_one(data)
        return render_template('displayRecipe.html', recipe = recipe)
    else:
        return redirect('/')

@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    data = {
        'id': id
    }
    Recipe.delete_one(data)
    return redirect('/dashboard')

@app.route('/recipe/edit/<int:id>')
def display_recipe_edit(id):
    if User.validate_session():
        data = {
            'id': id
        }
        recipe = Recipe.get_one(data)
        return render_template('displayEditRecipe.html', recipe = recipe)
    else:
        return redirect('/')

# This is for update through the form, id is not updateable on the form so it's set as itself here
@app.route('/recipe/edit/<int:id>', methods=['POST'])
def update_recipe(id):
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_thirty': request.form['under_thirty'],
        'user_id': session['user_id'],
        'created_at': request.form['created_at']
    }

    Recipe.update_one(data)

    return redirect('/dashboard')