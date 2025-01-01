import pymongo
from pymongo import MongoClient

parola=None
with open("parola_mongo.txt", "r") as file:
    parola=file.read

class Database:
    def __init__(self, uri=f"mongodb+srv://mariustrifon:{parola}@cluster0.2nwkg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", db_name="patiserie"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_recipes(self):
        return list(self.db.recipes.find())

    def add_recipe(self, recipe):
        self.db.recipes.insert_one(recipe)

    def get_ingredient(self, ingredient_name):
        return self.db.ingredients.find_one({"name": ingredient_name})


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://mariustrifon:Mariusikklivia94@cluster0.2nwkg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)