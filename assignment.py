#string concatenation
base1 =input("enter your name")
base2="hello"
base3="Welcome to Python programming"
print(base2,base1,",",base3)

#string slicing and indexing
base4= "hello Niyas,welcome to python programming"

print(base4[0])

print(base4[-1])

print(base4[0:6])

print(base4[30:41])

print(base4[::-1])

print(base4[23:29])


#string methods

strM="Python beginner tutorial" 

print(strM.upper())

print(strM.lower())

print(strM.capitalize())

print(strM.count("t"))

print(strM.replace("Python","Machine learning"))

#tuples

tuple1 = (10,20,30)
tuple2 = (40,50,60)

t_combine = tuple1 + tuple2

print(t_combine)

print(t_combine*3)

print(t_combine [2])

print(t_combine[:3])

print(t_combine[3:6])