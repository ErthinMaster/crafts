import json, random
from utils import load_json, write_json, load_txt


def generate_ingredients_for_potions(potions, ingredients):
    for potion in potions.values():
        nb_ingredients = random.randint(2, 2+potion['level'])
        potion["ingredients"] = {val : random.randint(2, 2*potion['level']) for val in random.choices(ingredients, k=nb_ingredients)}


if __name__ == '__main__':
    potions = load_json("./potions.json")
    ingredients = load_txt("./ingredients.txt")
    generate_ingredients_for_potions(potions, ingredients)
    write_json(".potions_new.json", potions)
    
