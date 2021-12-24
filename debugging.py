# Q1
# a = {(1,2):1,(2,3):2}
# print(a[1,2])


# Q2
# a = {'a':1,'b':2,'c':3}
# print (a['a'])


# Q3
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)


# Q4
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 



# Q5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)



# Q6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates['box']))


# Q7
# rec = {
# "Name" : "Python",
# "Age":"20",
# "Addr" : "NJ",
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
# "Name" : "Python",
# "Age":"20",
# "Addr" : "NJ",
# "Country" : "USA"
# }
# id2 = id(rec)
# print(id1 == id2)



# 2-Q1
# details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org"}
# print(details["name"])
# print(details["email"])
# print(details["age"])


# 2-Q2
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum=sum+i
# print(sum)

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.keys():
#     sum=sum+i
# print(sum)


# 2-Q3
# c=dict()
# for i in range(1,16):
#     c=i*i
#     print(c)
# OUTPUT:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
# 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


# 2-Q4
# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)

