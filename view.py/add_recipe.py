import tkinter as tk
from tkinter import messagebox

class AddRecipeWindow:
    def __init__(self, root, recipe_manager):
        self.root = root
        self.recipe_manager = recipe_manager
        
        self.window = tk.Toplevel(self.root)
        self.window.title("Adaugă Rețetă")

        self.name_label = tk.Label(self.window, text="Nume Rețetă")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.ingredient_label = tk.Label(self.window, text="Ingrediente (nume, unitate, cantitate)")
        self.ingredient_label.pack()
        
        self.ingredients_entry = tk.Entry(self.window)
        self.ingredients_entry.pack()

        self.instructions_label = tk.Label(self.window, text="Instrucțiuni")
        self.instructions_label.pack()

        self.instructions_entry = tk.Entry(self.window)
        self.instructions_entry.pack()

        self.add_button = tk.Button(self.window, text="Adaugă", command=self.add_recipe)
        self.add_button.pack()

    def add_recipe(self):
        name = self.name_entry.get()
        ingredients_data = self.ingredients_entry.get().split(",")
        ingredients = [{"name": i[0], "unit": i[1], "quantity": float(i[2])} for i in ingredients_data]
        instructions = self.instructions_entry.get()
        
        self.recipe_manager.add_recipe(name, ingredients, instructions)
        messagebox.showinfo("Succes", "Rețeta a fost adăugată.")
        self.window.destroy()
