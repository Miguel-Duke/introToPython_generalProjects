#This is the code for 2.15 lab:Driving Costs done with instructor!
#Remember to remove the strings from the input functions as zybooks will
#not be happy about their appearance in the answers!

#input miles/gallon
#input dollars/gallon
#output cost of 20, 75, and 500 miles

#accept input values
mPerGall = float(input('Enter the miles/gallon for the car'))
dPerGall = float(input('Enter the dollars/gallon price of gas'))

#calculate the cost for 20 miles
miles = 20
numGallons = miles / mPerGall
cost20 = dPerGall * numGallons

#calculate the cost for 75 miles
miles = 75
numGallons = miles / mPerGall
cost75 = dPerGall * numGallons

#calculate the cost for 500 miles
miles = 500
numGallons = miles / mPerGall
cost500 = dPerGall * numGallons

#print out the three costs
print('{:.2f} {:.2f} {:.2f}'.format(cost20, cost75, cost500) )

#in this print command each {} corresponds to a value listed in the .format()
#that comes after it. the .2 states that the float (decimal) should go as far
#as 2 decimal places to the right. 


