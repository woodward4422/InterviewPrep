# Question: Given a list of Restaurants that have a name and rating, find the business with the median rating

class Business:
    def __init__(self,name,rating):
        self.name = name
        self.rating = rating
    
def median_rating_business(businesses):
    businesses.sort(key = lambda b: b.rating)
    


    
if __name__ == "__main__":
    businesses = [Business("Burger King", 3),Business("Barnes and Nobles", 4),Business("Subway", 2), Business("Home Depot", 5), Business("Marshalls", 3), Business("MacD",1), Business("Home Goods", 2)]
    print(median_rating_business(businesses))

