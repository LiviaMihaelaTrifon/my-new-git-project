from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(recipe, ingredients):
    pdf_path = f"{recipe.name}_ingredientele.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)

    c.drawString(100, 750, f"Rețeta: {recipe.name}")
    c.drawString(100, 730, "Ingrediente necesare:")

    y_position = 710
    for ingredient_name, details in ingredients.items():
        c.drawString(100, y_position, f"{ingredient_name}: {details['quantity']} {details['unit']}")
        y_position -= 20
    
    c.save()
