my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,

#list[start:end:step]

print my_list[1: ]     # [1,2,3,4,5,6,7,8,9]
print my_list[ :-1]    # [0,1,2,3,4,5,6,7,8]
print my_list[ : ]     # [0,1,2,3,4,5,6,7,8,9]
         
         #==========step allows to skip values===========#

print my_list[2:-1]      # [2, 3, 4, 5, 6, 7, 8,]
print my_list[2:-1:2]    # [2, 4, 6, 8]


# Get elements from second index to third index.
values = [100,200,300,400,500]
slice = values[1:3]
print(slice)

My_new_list = [ 1,2,3,4,5,6,7,8,9]
slice = values[ : ]
print(slice)

array = range(1,5) #[0,1,2,3,4]
#print(array)

for x in array[ : ]:
        print(x)