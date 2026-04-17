# mylist=[1,2,3,4,5]
# mylist.reverse()
# print(mylist)
# mydict={"name":"Alice","age":30}
# if "age" in mydict:
#     print("key exist")
# list=[4,7,6,9,5]
# list.sort()
# print(list)
# print(list[-2])
mylist =[1,2,3,2,1]
original=mylist
reverse=0
while int(mylist)>0:
    digit=mylist%10
    reverse=reverse*10+digit
    mylist=mylist//10
    if reverse==original:
        print("palindrome")
    else:
        print("not palindrme")



