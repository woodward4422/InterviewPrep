# Question: Given a list of meals that have a name and ingredients

class Meal:

    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients
# Takes in a list of meals and will use a dictionary with keys being ingredients to find unique meals
ingredients_dict = {}
def unique_meals(meals_list):
    if len(meals_list == 0):
        return 0

    for element in meals_list:
        ingredients = element.ingredients
        ingredients.sort()
        keys = frozenset(ingredients)
        ingredients_dict[keys] = element.name
    return len(ingredients_dict)
    
    

    
if __name__ == "__main__":
    meals = [Meal("American",["lettuce","cheese","olives","tomato"]),Meal("Mexican",["lettuce","cheese","pepper","tomato"]), Meal("French",["lettuce","cheese","pepper","tomato"]),Meal("Continental",["lettuce","cheese","olives","tomato"])]
    print(unique_meals(meals))
