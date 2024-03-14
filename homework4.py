immutable_var=1,2,'это',False,[3,4,'ivan']
print(2) # номер задания 2
print('Immtable tuple:',immutable_var)
print(type(immutable_var))
print(3)# номер задания 3
#immutable_var[3]=True
#print(immutable_var) # выполнить нельзя,ошибка т.к.кортеж относится к неизменяемым типам данных.
print(4)# номер задания 4
mutable_list=[1,2,'ivan',True]
print('Mutable list:',mutable_list)
mutable_list[3]=False
mutable_list[2]=3
print('Mutable list:',mutable_list)