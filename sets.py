s={"amrinder","singh",7}
print(s)
print(type(s))

empty=set()  #empty set

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      
print('orange' in basket)                 
print('crabgrass' in basket)

s1=set("gcsdhagvsfdsfj")
print(s1)
s2=set("ifshiufshfu")
print(s2)

print(s1-s2)    #set difference
print(s1|s2)    #union
print(s1&s2)    #intersection
print(s1^s2)    #symmetric difference(s1-s2 union s2-s1)
