def calculator():
    a=int(input("Enter a first value:" ))
    b=int(input("Enter a second value:"))
    print("options:\n A.add\n B.sub \n C.mul \n D.div \n")
    cho=(input("Select your option:"))
    if cho.upper()== 'A' :
        r=a+b
       
    elif cho.upper() == 'B' :
        r=a-b
    elif cho.upper() == 'C' :
        r=a*b
    elif cho.upper() == 'D' :
        if b== 0:
            print("B value should be greater then or equal to 1")
        else:
            r=a/b
    return r

print(calculator())
        
