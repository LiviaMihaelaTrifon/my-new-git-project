import pymongo
from pymongo import MongoClient

class Database:
    def __init__(self, uri="mariustrifon", db_name="patiserie"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_recipes(self):
        return list(self.db.recipes.find())

    def add_recipe(self, recipe):
        self.db.recipes.insert_one(recipe)

    def get_ingredient(self, ingredient_name):
        return self.db.ingredients.find_one({"name": ingredient_name})


