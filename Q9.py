# Store the unique letters and their frequency of the letters from 
# the word "MISSISSIPPI" to a dictionary, were the letters are the keys 
# and their frequencies are the values.

k={}
# string="MISSISSIPPI"
string=input("enter a text:")
for i in string:
    count=0
    for j in string:
        if i==j:
            count+=1
        k.update({i:count})
print(k)



# Output :-
# {'M':1,'I':4,'S':4,'P':2}