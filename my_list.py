#Creating an empty list
my_list = []

#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#adding 15 to the list 
index = 1
item = 15
my_list.insert(index, item)

#extending my_list with another list
#create another list
list_2 = [50, 60, 70]

#extend the list
my_list.extend(list_2)

#removing the last element from my_list
del my_list[-1]

#alternatively remove() can be used as shown below
# my_list.remove(70)

#sorting the list
my_list.sort()

#finding the index of 30
index = my_list.index(30)
print(f'The index of 30 is {index}')

print(f'The items in my list are {my_list}')