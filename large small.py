#to store numbers 
lst = []

#to get numbers 
while True : 
    number = input("Enter a number: ")

    #stop the program 
    if number == "done": 
        break 
    
    #catch error and append nums to list 
    try : 
        float(number) 
        lst.append(int(number))
    except: 
        print("Invalid input") 

#find the samllest num 
samllest = None 
largest = None 

for num in lst :
    if samllest is None : 
        samllest = num 
    elif num < samllest: 
        samllest = num
    
    
for nn in lst :
    if largest is None : 
        largest = nn 
    elif nn > largest: 
        largest = nn
    
print("samllest: ",samllest, "\nlargest: ",largest)