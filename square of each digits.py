#There might be a shorter way, but i am new to python, so just focussing on result 
def square_digits(num):
    #Converting the num to string
    str_num = str(num)
    #using list comprehension and type_casting getting each digit     
    a = [int(i) for i in str_num]
    #Again squaring each digit
    b = [i*i for i in a]
    #inorder to join the digit,using join and map on b
    res = "".join(map(str,b))
    #as we need result in int so type_casting again
    res1 = int(res)
    return res1
