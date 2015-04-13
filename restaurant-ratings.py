# your code goes here
scores = open("scores.txt")

restaurant_list = []

for restaurants in scores:
    individual_restaurants = restaurants.rstrip().split(":")
    restaurant_list.append(individual_restaurants)
    restaurant_list.sort()
for restaurants in restaurant_list:
    print "Restaurant: %s is rated at %s." % (restaurants[0], restaurants[1])