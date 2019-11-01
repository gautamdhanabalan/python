# mylist1 = list(range(0,5))
# mylist2 = list(range(0,10,1))
# mylist3 = list(range(0,20,3))
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
#
# for item in zip(mylist1,mylist2,mylist3):
#      print(item)
#print(mylist1)
#print(mylist2)

numrange = [x for x in range(0,100)]
for index,x in enumerate(numrange):
    if x%3 == 0 and x%5==0:
        numrange[index] = "fizzbuzz"
    elif x%3 == 0:
        numrange[index] = "fizz"
    elif x%5 == 0:
        numrange[index] = "buzz"

print(numrange)
