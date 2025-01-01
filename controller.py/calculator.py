class Calculator:
    def calculate_ingredients(self, recipe, portions):
        required_ingredients = {}
        for ingredient in recipe.ingredients:
            required_ingredients[ingredient.name] = {
                "unit": ingredient.unit,
                "quantity": ingredient.quantity * portions
            }
        return required_ingredients
