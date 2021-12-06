def sum67(list1):
    s=0
    statement=True
    for i in range (len(list1)):
        if list1[i]==6:
            statement=False
        if statement==True:
            s+=list1[i]
        if list1[i]==7:
            statement=True
    return s
    
print(sum67([1,2,2]))
print(sum67([1,2,12,6,92,2,7,10]))
print(sum67([1,7,6,7,2]))
            