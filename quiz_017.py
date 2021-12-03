def quiz_017(a,b,c):
    
    if a+b>c and b+c>a and a+c>b:
        statement=True
    else:
        statement=False
    return statement
    
print(quiz_017(1,1,2))
print(quiz_017(5,6,3))
print(quiz_017(1,2,9))