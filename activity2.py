def matchwords(words):
    count=0
    list1=[]
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            count=count+1
            list1.append(i)
    print ("the list is",list1)
    return count
word1=matchwords(["abc","cfc","xyz","aba","1221"])
print (f"the number of words are {word1}")