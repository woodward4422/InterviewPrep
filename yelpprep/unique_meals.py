# Question: Given a list of meals that have a name and ingredients

class Meal:

    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients
# Takes in a list of meals 
def unique_meals(meals_list):
    for element in meals_list:
       frozenset(ingredients) = element.ingredients
        ingredients.sort()
        
    return len(ingredients_dict)
    
    
       # element.ingredients.sort(key = lambda s: s.ingredients)

    
if __name__ == "__main__":
    meals = [Meal("American",["lettuce","cheese","olives","tomato"]),Meal("Mexican",["lettuce","cheese","pepper","tomato"]), Meal("French",["lettuce","cheese","pepper","tomato"]),Meal("Continental",["lettuce","cheese","olives","tomato"])]
    print(unique_meals(meals))
