fruitprices={'apple':55.6, 'banana':10.4, 'grape':44}

def buyFruit(fruit, numOfpounds):
	if fruit not in fruitprices :
		print "sorry, we don't have %s" % (fruit)
	else :
	    cost = fruitprices[fruit]*numOfpounds
	    print "That'll be %f please" % (cost)


# Main Function
if __name__ == '__main__' :
	buyFruit('apple', 5)
	buyFruit('coconut', 3)