def area(n):
    a= (3.14) * r * r
    print("area is:",a)    
def res(x,y,z):
    r1 = w * l
    r2 = r1 / area(r)
    print("radius is:",r2)
r=int(input("Enter the radius"))
result = area(r)
print(result)
w=int(input("Enter the Rho"))
l=int(input("Enter the length"))
result1 = res(w , l, area(r))
print(result1)
