# Initialization
faits = ["B", "C"]
But = "H"
regles = []


# Loading data from text file
TXT = open('Base.txt', 'r')

# Adding every condition in a list called "regles"
line = TXT.readline()
while line:
    regles.append(line.rstrip().split('=', 1))
    line = TXT.readline()

# Now it's time to check and pply those conditions
loop = 1  # If something changes in "faits" we should check the rest of conditions again
while loop > 0:
    loop = loop - 1
    for x in regles:  # Passing by all conditions now
        check = True

        for y in x[0]:  # Checking if they are correct
            if y not in faits:
                check = False

        if check:  # If they are correct, we try to apply it 

            if x[1] not in faits:  #  But first we should check if we already have the result in the list to avoid repetition
                faits.append(x[1])
                print("Applying ", x, "-----> ", faits)

                if x[1] == But:  # If it's the solution we stop here!
                    loop = 0
                else:
                    loop = loop + 1 # Else we continue...
            else:
                print("Applying ", x, "-----> ", "we alredy have ", x[1], " in the list!")

            regles.remove(x)  # Deleting the applied condition

print("\nThe final list: ", faits)
print("Checking if ", But, "is in the list...")
if But in faits:
    print('* Yes, We found it! *')
else:
    print("* NO, sorry! *")
