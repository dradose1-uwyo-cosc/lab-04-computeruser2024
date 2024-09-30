#top  15 

#skirt  20
#shoes  25
#purse  10
#hat  5
# I bought eggs for $3
items = ["top", "skirt", "shoes", "purse", "hat"]
prices = ["15", "20", "25", "10", "5"]
for item in items:
    print (item)
for price in prices:
    print (price)
#for i in range(len(items)):
#print("Length of items", len(items))
#print("What is this doing?", range(len(items)))
#for index in range(len(items)):
#    print(f"Index: {index} I bought {items[index]} for ${prices[index]}')
# I spent $100 at Walmart
#prices = ["15", "20", "25", "10", "5"]
prices = [15, 20, 25, 10, 5]
print ("I spent")
print(sum(prices))





# The cheapest item was x
# The most expensive item was x
print(f"The cheapest item was {prices[-1]}")
print(f"The most expensive item was {items[2]}")