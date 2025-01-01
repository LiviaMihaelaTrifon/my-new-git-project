from model.database import Database
from model.recipe import Recipe
from model.ingredient import Ingredient

class RecipeManager:
    def __init__(self):
        self.db = Database()

    def get_recipes(self):
        recipes_data = self.db.get_recipes()
        recipes = []
        for recipe_data in recipes_data:
            ingredients = [Ingredient(i['name'], i['unit'], i['quantity']) for i in recipe_data['ingredients']]
            recipes.append(Recipe(recipe_data['name'], ingredients, recipe_data['instructions']))
        return recipes

    def add_recipe(self, name, ingredients, instructions):
        ingredients_objects = [Ingredient(i['name'], i['unit'], i['quantity']) for i in ingredients]
        recipe = Recipe(name, ingredients_objects, instructions)
        self.db.add_recipe({
            "name": name,
            "ingredients": [{"name": i.name, "unit": i.unit, "quantity": i.quantity} for i in ingredients_objects],
            "instructions": instructions
        })
