# Take input of name and marks of 10 students and store to a dictionary.
# dictionary=dict(
# sonu=85,
# Kartik=90,
# Deepak=96,
# Aman=76,
# Somesh=60,
# Umesh=85,
# Amarpal=70,
# Roshan=57,
# Riyaz=98,
# Shabid=56)
# print(dictionary)

# Output :-
# {'sonu':85,
# 'Kartik':90,
# 'Deepak':96,
# 'Aman':76,
# 'Somesh':60,
# 'Umesh':85,
# 'Amarpal':70,
# 'Roshan':57,
# 'Riyaz':98,
# 'Shabid':56}



d={}
for i in (range(1,10)):
    k=input("enter a key:")
    v=input("enter a key value:")
    d.update({k:v})
print(d)