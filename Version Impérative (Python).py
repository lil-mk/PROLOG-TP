# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

mon_dictionnaire = {
    "Pizza": "Farine,Eau,Sel,Levure,Tomate,Fromage",
    "Salade": "Laitue,Tomate,Concombre,Vinaigre,Huile",
    "PâtesnCarbonara": "Pâtes,Crème,Lardons,Fromage,Sel,Poivre",
    "Omelette": "Œufs,Sel,Poivre,Fromage,Herbes (optionnel)",
    "Sandwich Jambon-Beurre" : "Pain,Beurre,Jambon,Salade (optionnel)",

}

print(mon_dictionnaire)


# Press the green button in the gutter to run the script.
def print_hi(recette):
    pass


def recettes_realizables(ingredients_disponibles):
    # Base de données des recettes avec les ingrédients nécessaires
    recettes = {
        "Salade composée": ["tomate", "concombre", "salade", "huile d'olive"],
        "Omelette": ["oeufs", "sel", "poivre", "beurre"],
        "Spaghetti à la tomate": ["spaghetti", "tomate", "ail", "huile d'olive"],
        "Soupe de légumes": ["carotte", "poireau", "pomme de terre", "eau", "sel"],
        "Pancakes": ["farine", "lait", "oeufs", "sucre", "beurre"]
    }

    # Liste pour stocker les recettes réalisables
    recettes_realizables = []

    # Vérification des recettes réalisables
    for recette, ingredients in recettes.items():
        # Vérifier si tous les ingrédients nécessaires sont dans les ingrédients disponibles
        if all(ingredient in ingredients_disponibles for ingredient in ingredients):
            recettes_realizables.append(recette)

    return recettes_realizables


# Exemple d'utilisation
ingredients_disponibles = ["oeufs", "sel", "poivre", "beurre", "carotte", "tomate", "spaghetti"]
recettes = recettes_realizables(ingredients_disponibles)

print("Recettes réalisables :", recettes)

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
