# Take a list having dictionary elements as shown below (Sample Data) 
# and then store all the unique values into a list and print.
Dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},
{"six":"9"},{"seven":"7"}]


# Output :-
# [2', '7', '9', '5', '1']
x=[]
for i in Dic:
    count=0
    for j in i:
        for k in i:
            if i[j]==i[k]:
                count+=1
                if count<=1:
                    if i[j] not in x:
                        x.append(i[j])
print(x)
