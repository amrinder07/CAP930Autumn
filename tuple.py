#Tuples are immutable, store heterogeneous data

me=("amrinder","male",23)
print(me)
print(me[1])
print(len(me))
print(me[:3])
print("male" in me)

a1=123,'abc',69.69
print(a1)
a,b,c=a1    #unpacking
print(b)
