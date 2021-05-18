largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        ival = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None :
        largest = ival
        smallest = ival
    elif ival > largest :
        largest = ival
    elif ival < smallest :
        smallest = ival
    
    
print("Maximum", largest)
print("Minimum", smallest)