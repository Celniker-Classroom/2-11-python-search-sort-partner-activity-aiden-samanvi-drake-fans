from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

ranNums = [] #name your list and make sure it is empty!
doubleList = []
oddList = []
evenList = []

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for index in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list

print("Your generated list: ", ranNums)

for i in range(len(ranNums)):
    if int(ranNums[i]) % 2 == 0:
        evenList.append(ranNums[i])
    else: 
        oddList.append(ranNums[i])


for i in range(len(ranNums)): # finds double of each number in list
    ranNums[i] = 2 * int(ranNums[i])
    doubleList.append(ranNums[i])

print("Your list doubled is: ", doubleList) #doubled list
print("The even numbers in your list: ", evenList)
print("The odd numbers in your list: ", oddList)