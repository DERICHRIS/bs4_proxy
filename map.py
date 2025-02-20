## for map() function

#general method
import math
def area_math(r):
    return math.pi*(r**2)
r=[1,2,3,4]
area=[]

for i in r:
    a=area_math(i)
    area.append(a)

#print(area)

# with map() functionality

#print(list(map(area_math,r))) # map(func,iterable)



temp=[('trichy',34),('chennai',35),('kodaikanal',18)]

c_to_f=lambda data:(data[0],(9/5)*data[1]+32)

output=list(map(c_to_f,temp))
#print(output)

# filter()
import statistics
a=[0.8,1.4,9.5,6,1,0,1,0.2]

avg=statistics.mean(a)
print(avg)

output=list(filter(lambda x: x>avg,a)) # syntax--> filter(func,data)
print(output)

country=['china','india','','','usa']

print(list(filter(None,country)))  

# reduce() function acts or iterates along sequence manner
from functools import reduce
a=[1,3,5,7,9,11]

out=lambda x,y:x*y

print(reduce(out,a))
