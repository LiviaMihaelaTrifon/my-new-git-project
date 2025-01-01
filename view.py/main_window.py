import tkinter as tk
from tkinter import messagebox
from controller.recipe_manager import RecipeManager
from controller.calculator import Calculator
from utils.pdf_generator import generate_pdf

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Patiserie")
        
        self.recipe_manager = RecipeManager()
        self.calculator = Calculator()

        self.recipe_listbox = tk.Listbox(self.root)
        self.recipe_listbox.pack()
        
        self.add_recipe_button = tk.Button(self.root, text="Adaugă rețetă", command=self.open_add_recipe_window)
        self.add_recipe_button.pack()
        
        self.calculate_button = tk.Button(self.root, text="Calculează Ingrediente", command=self.calculate_ingredients)
        self.calculate_button.pack()
        
        self.load_recipes()

    def load_recipes(self):
        recipes = self.recipe_manager.get_recipes()
        for recipe in recipes:
            self.recipe_listbox.insert(tk.END, recipe.name)

    def open_add_recipe_window(self):
        from view.add_recipe import AddRecipeWindow
        AddRecipeWindow(self.root, self.recipe_manager)

    def calculate_ingredients(self):
        selected_recipe_name = self.recipe_listbox.get(tk.ACTIVE)
        recipes = self.recipe_manager.get_recipes()
        recipe = next(r for r in recipes if r.name == selected_recipe_name)

        portions = int(input("Introduce numărul de porții: "))  # Ar trebui înlocuit cu un formular Tkinter
        ingredients = self.calculator.calculate_ingredients(recipe, portions)
        generate_pdf(recipe, ingredients)

        messagebox.showinfo("Calcul complet", "PDF-ul cu ingredientele a fost generat.")
