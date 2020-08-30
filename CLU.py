
def add(*argv):  # Become list of tuple  
    result = 0
    for number in argv[0]:
         result += int(number)
    return (result)
    print("Sum of numbers{} is {}".format(argv,result))

def sub(*argv):
    
    result = 0
    bFirstTime = True
    for number in argv[0]:
       if( bFirstTime):
           result += int(number)
           bFirstTime = False
       else:
             result -= int(number)
    print("Diff of list of numbers{} is {}".format(argv,result))
   

def Multi(*argv):
    result = 1
    for number in argv[0]:
        result *= int(number)
    print("Multipicaton of list of numbers{} is {}".format(argv,result))

def Div(*argv):
    result = 0
    bFirstTime = True
    for number in argv[0]:
       if( bFirstTime):
           result += int(number)
           bFirstTime = False
       else:
             result /= int(number)
        
       
    print("Division of list of numbers{} is {}".format(argv,result))


def Calculator(Opcode,Arguments):

 
    if Opcode == "add":
        add(Arguments)
    elif Opcode == "sub":
        sub(Arguments)
    elif Opcode == "Multi":
        Multi(Arguments)
    elif Opcode == "Div":
        Div(Arguments)
    else:
        print("OP code is not correct\n")





if __name__ == "__main__":
    import sys
    if(len(sys.argv) < 4):
        print("Enter required parameters\n")

    Calculator(sys.argv[1],sys.argv[2:])

