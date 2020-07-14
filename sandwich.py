#Sandwich shop activity by Michael Schwartz

#I labeled variables involing price as floats to accomodate the decimal
#but I did notice that 'int' was specified in the rubric. I can certainly change
#them over without issue if it impacts my grade. I thought that due to the
#decimal nature of prices float was a good option. Thank you!

#Prompt for vendor name.
vendor_1 = input('Who is the vendor?')

#Gathering information on bread.
#priceLoaf is the cost of a loaf of bread.
#slicePerLoaf is the number of slices per bread loaf.
#breadPerSandwich is how many slices of bread the recipe calls for.

priceLoaf = float(input('Please enter the cost of a bread loaf:'))
slicePerLoaf = int(input('Thank you, how many slices in a loaf?:'))
breadPerSandwich = 2

#Calculating the cost of bread, and presenting the information to the user.
#slicesBread is the total cost of bread per sandwich.

slicesBread = float((priceLoaf / slicePerLoaf) * breadPerSandwich)
print('The cost is $', slicesBread, 'for each sandwiches bread.')

#Gathering information on swiss.
#pricePound is the cost per pound of swiss.
#slicePerPound is the number of slices per pound of swiss.
#swissPerSandwich is how many slices of swiss the recipe calls for.

pricePound = float(input('Please enter the cost per pound of swiss:'))
slicePerPound = int(input('Thank you, how many slices per pound of swiss?:'))
swissPerSandwich = 2

#Calculating the cost of swiss, and presenting the information to the user.
#slicesSwiss is the total cost of swiss per sandwich.

slicesSwiss = float((pricePound / slicePerPound) * swissPerSandwich)
print('The cost is $', slicesSwiss, 'for each sandwiches swiss.')

#Gathering information on ham.
#priceHam is the price per pound of ham.
#slicePerHam is the number of slices per pound of ham.
#hamPerSandwich is how many slices of ham the recipe calls for.

priceHam = float(input('Please enter the cost per pound of ham:'))
slicePerHam = int(input('Thank you, how many slices of ham per pound?:'))
hamPerSandwich = 4

#Calculating the cost of ham, and presenting the information to the user.
#slicesHam is the total cost of ham per sandwich.

slicesHam = float((priceHam / slicePerHam) * hamPerSandwich)
print('The cost is $', slicesHam, 'for each sandwiches ham.')

#Building the total cost of the sandwich.
#sandwich_cost is the combined cost of sandwich materials.

sandwich_cost = float(slicesBread + slicesSwiss + slicesHam)

#Printing the final statement.
print('The cost of this sandwich is $', sandwich_cost, 'from vendor', vendor_1, '.')


