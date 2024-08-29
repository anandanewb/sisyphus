def fizzbuzz(upTo):
    answer = ""
    for x in range(1,upTo+1):
        answer += getsubtext(x) + " "
        
    print(answer)
       

def getsubtext(x):
    if (x % 15  == 0):
        sub_str = "fizzbuzz"
    elif(x % 3 == 0):
        sub_str = "fizz"
    elif(x % 5 == 0):
        sub_str = "buzz"
    else:
        sub_str = str(x)
    
    return sub_str

    

fizzbuzz(30)
