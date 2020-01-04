# First Part

print(format("Fahrenheit",'14'),format("Celsius",'14'))
print('-'*22)

# Loop for temp=F
tempF=0
while tempF<=100:
    tempC=(tempF-32)*5/9
    print(format(tempF,'6'),format(tempC,'14.2f'))
    tempF+=10

print()
print()


# Second Part

# Input for variables
n1,n2,n3=eval(input("Enter 3 numbers: "))

# Avoids incorrect range
if n1>n2:
	n1,n2=n2,n1

print("The numbers between",n1,"and",n2,"that are evenly divisible by",n3,"are:")

# Loop for n1
while n1<=n2:
    if n1%n3==0:
        print(n1,end=' ')
    n1+=1
