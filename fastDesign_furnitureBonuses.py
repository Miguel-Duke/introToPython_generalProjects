# Week 4 project Fast Design Furniture bonuses by Michael Schwartz!

# Employees who make $30k+ get 4% bonus
# Employees who make $25k to $30k get %4.5 bonus
# Employees who make $20k to $25k get 5% bonus

# Prompt George for the total amount that can be spent on bonuses.
# Accept 5 employee names and salaries.
# For each employee print: Name, Salary, Bonus
# Output the total of the bonuses.
# Print out a message indicating if George can afford the bonus plan or not!

# As always properly comment each step of the program.

# First we prompt for our total budget.
bonuses_affordable = int(input('Please enter how much you can afford for bonuses: $'))

# Next we need to gather some employee information.
employee1 = input('First employee:')
employee1_sal = int(input('Salary: $'))

employee2 = input('Second employee:')
employee2_sal = int(input('Salary: $'))

employee3 = input('Third employee:')
employee3_sal = int(input('Salary: $'))

employee4 = input('Fourth employee:')
employee4_sal = int(input('Salary: $'))

employee5 = input('Fifth employee:')
employee5_sal = int(input('Salary: $'))

# Now we take each employee's salary and we determine which bonus bracket they belong in
# and what their salary should be after the bonus is applied.

# Employee 1 salary conversion:
if employee1_sal >= 20000: # Only employee's that make $20k+ are eligeable!
    if employee1_sal > 30000:
        employee1_bonus = (employee1_sal * .04)
    elif 30000 >= employee1_sal > 25000:
        employee1_bonus = (employee1_sal * .045)
    else:
        employee1_bonus = (employee1_sal * .05)
else:
    employee1_bonus = 'Employees who make less than $20,000 are not eligable!'

# Employee 2 salary conversion:
if employee2_sal >= 20000:
    if employee2_sal > 30000:
        employee2_bonus = (employee2_sal * .04)
    elif 30000 >= employee2_sal > 25000:
        employee2_bonus = (employee2_sal * .045)
    else:
        employee2_bonus = (employee2_sal * .05)
else:
    employee2_bonus = 'Employees who make less than $20,000 are not eligable!'

# Employee 3 salary conversion:
if employee3_sal >= 20000:
    if employee3_sal > 30000:
        employee3_bonus = (employee3_sal *.04)
    elif 30000 >= employee3_sal > 25000:
        employee3_bonus = (employee3_sal *.045)
    else:
        employee3_bonus = (employee3_sal *.05)
else:
    employee3_bonus = 'Employees who make less than $20,000 are not eligable!'

# Employee 4 salary conversion:
if employee4_sal >= 20000:
    if employee4_sal > 30000:
        employee4_bonus = (employee4_sal * .04)
    elif 30000 >= employee4_sal > 25000:
        employee4_bonus = (employee4_sal * .045)
    else:
        employee4_bonus = (employee4_sal * .05)
else:
    employee4_bonus = 'Employees who make less than $20,000 are not eligable!'

# Employee 5 salary conversion:
if employee5_sal >= 20000:
    if employee5_sal > 30000:
        employee5_bonus = (employee5_sal * .04)
    elif 30000 >= employee5_sal > 25000:
        employee5_bonus = (employee5_sal * .045)
    else:
        employee5_bonus = (employee5_sal * .05)
else:
    employee5_bonus = 'Employees who make less than $20,000 are not eligable!'

# Here we need to print out a chart of all the employees, their salaries and their bonuses.
print(str(employee1) + ', $' + str(employee1_sal) + ', $' + str(employee1_bonus))
print(str(employee2) + ', $' + str(employee2_sal) + ', $' + str(employee2_bonus))
print(str(employee3) + ', $' + str(employee3_sal) + ', $' + str(employee3_bonus))
print(str(employee4) + ', $' + str(employee4_sal) + ', $' + str(employee4_bonus))
print(str(employee5) + ', $' + str(employee5_sal) + ', $' + str(employee5_bonus))

# We need to calculate the total bonuses being paid out
total_bonuses = int((int(employee1_bonus) + int(employee2_bonus) + int(employee3_bonus) + int(employee4_bonus) + int(employee5_bonus)))
print('Total bonuses paid out: $' + str(total_bonuses))

# Last we need to tell George if this bonus plan is affordable.
if bonuses_affordable > total_bonuses:
    print('This bonus plan is within budget!')
else:
    print('This bonus plan is not within budget.')



    
