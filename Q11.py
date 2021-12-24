# Write a program to print the top 3 highest values of a given dictionary.
my_dict = {'a':50,'b':10,'c':56,'d':40,'e':100,'f':20}
max=0
dic={}
for i in my_dict:
    if my_dict[i]>max:
        key1=i
        max=my_dict[i]
dic[key1]=max

# sec_max=0
# for i in my_dict:
#     if my_dict[i]>sec_max and my_dict[i]!=max:
#         key2=i
#         sec_max=my_dict[i]
# dic[key2]=sec_max

# thrd_max=0
# for i in my_dict:
#     if my_dict[i]>thrd_max and my_dict[i]!=sec_max and my_dict[i]!=max:
#         key3=i
#         thrd_max=my_dict[i]
# dic[key3]=thrd_max
# print(dic)








# my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# x=[]
# c=[]
# for i in my_dict.values():
#     x.append(i)
# max=0
# for i in range(len(x)):
#     if max<x[i]:
#         max=x[i]
# c.append(max)
# # print(max)
# sec_max=0
# for i in range(len(x)):
#     if sec_max<x[i] and x[i]!=max:
#         sec_max=x[i]
# c.append(sec_max)        
# # print(sec_max)
# thrd_max=0
# for i in range(len(x)):
#     if thrd_max<x[i] and x[i]!=max and x[i]!=sec_max:
#         thrd_max=x[i]
# c.append(thrd_max)
# # print(thrd_max)
# print(c)

# Output :-
# [58,56,100]

# Q13
# Output :-
# expect result:-['e','b','c']