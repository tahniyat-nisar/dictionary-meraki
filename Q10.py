# Count the total number of items from the values of the dictionary which are 
# in the form of a list.
dict = {
'Alex': ['subj1', 'subj2', 'subj3'],
'David': ['subj1', 'subj2']}
count=0
for i in dict.values():
    for j in i:
        count+=1
print(count)
        
