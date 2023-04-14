num=int(input('Enter the number of elements you want to insert: '))
lst=[]
for i in range(num):
    element=input("Enter the string value:")
    lst.append(element)
sorted_list = sorted(lst, key=lambda x: x[-2])
print(sorted_list)
