def create_phone_number(n):
    #your code here
    one = "".join(map(str,n[:3]))
    two = "".join(map(str,n[3:6]))
    three = "".join(map(str,n[6:]))
    
    return "("+one+") "+two+"-"+three

    


print(create_phone_number(list(range(0,10))))
