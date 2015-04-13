# your code goes here
scores = open("scores.txt")

restaurant_dict = {}

for restaurants in scores:
    restaurants = restaurants.rstrip().split(":")
    restaurant_dict[restaurants[0]] = restaurants[1]
    names = sorted(restaurant_dict)
for name in names:
    print "Restaurant: %s is rated at %s." % (name, restaurant_dict[name])

scores.close()
