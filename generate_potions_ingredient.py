# -*- coding: utf-8 -*-
# @Author: Axel Bento da Silva
# @Date:   2024-01-22 13:30:54
# @Last Modified by:   Axel Bento da Silva
# @Last Modified time: 2024-01-22 13:41:18
import json, random
from utils import load_json, write_json, load_txt


def generate_ingredients_for_potions(potions, ingredients):
    for potion in potions.values():
        nb_ingredients = random.randint(2, 2+potion['niveau'])
        potion["ingredients"] = {val : random.randint(2, 2*potion['niveau']) for val in random.choices(ingredients, k=nb_ingredients)}


if __name__ == '__main__':
    potions = load_json("./potions.json")
    ingredients = load_txt("./NewPlantes.txt")
    generate_ingredients_for_potions(potions, ingredients)
    write_json("potions_new.json", potions)
    
