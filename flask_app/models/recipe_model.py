from msilib.schema import ControlEvent
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import database

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.under_thirty = data['under_thirty']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, created_at, under_thirty, user_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(created_at)s, %(under_thirty)s, %(user_id)s);"

        return connectToMySQL(database).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        
        result = connectToMySQL(database).query_db(query)
        recipes = []

        if len(result) > 0:
            for recipe in result:
                recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        
        result = connectToMySQL(database).query_db(query, data)

        if len(result) > 0:
            return cls(result[0])
        else:
            return None
    
    @classmethod
    def delete_one(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        return connectToMySQL(database).query_db(query, data)

    @classmethod
    def update_one(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, user_id = %(user_id)s, under_thirty = %(under_thirty)s, created_at = %(created_at)s WHERE id = %(id)s;'

        return connectToMySQL(database).query_db(query, data)