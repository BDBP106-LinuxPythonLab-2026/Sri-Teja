"""Program to interchange the even and odd components of an input list. The list
can contain any type of variables. Output the result for the following example:
[23,32,33,44,’BDBH101’,’hello’,’python’, 15, 1e-10, True,’hit’]"""

input_list=[23,32,33,44,'BDBH101','hello','python',15,1e-10,True,'hit']
print('Before:',input_list)

list=input_list.copy()
for i in range(0,len(list)-1,2):
    list[i],list[i+1] = list[i+1],list[i]

print('After:',list)