def quiz_016(A):
    list1 = list(A)
    for i in range(0, int((len(list1)/2)), 2):
        temp=list1[i]
        list1[i]=(list1[i+1])
        list1[i+1]=(temp)
    A="".join(list1)
    return(A)
    
print(quiz_016("Ahrgt"))
