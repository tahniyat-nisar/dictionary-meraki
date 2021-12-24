# Write a program to sort a dictionary in ascending or descending
#  according to its values .
dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in range(len(dic)):
    for j in range(len(dic))-1:
        if dic[j]<dic[j-1]:
            
    








# Expected result in Ascending Order:
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}


# Expected result in Descending Order:
# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}