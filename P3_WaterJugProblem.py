a = int(input("Enter Capacity of A : "))
b = int(input("Enter Capacity of B : "))

ai = int(input("Enter Initial Capacity of A : "))
bi = int(input("Enter initial capacity of B : "))

af = int(input("Enter final state of A : "))
bf = int(input("Enter final state of B : "))

print("--- List of Water Jug Problem ---")

print("1. Fill Jug A Completely")
print("2. Fill jug B completely")
print("3. Empty jug A completely")
print("4. Empty jug B completely")
print("5. Pour from jug A till jug B fills completely or jug A becomes empty")
print("6. Pour from jug B till jug A fills completely or jug B becomes empty")
print("7. Pour all from jug A to jug B")
print("8. Pour all from jug B to jug A")

print("-------------------------------")

while(ai!=af or bi!=bf):
    op = int(input("Enter Operation : "))

    if(op == 1):
        ai=a
    elif(op==2):
        bi=b
    elif(op==3):
        ai=0
    elif(op==4):
        bi=0
    elif(op==5): #pour from A -> B till B gets FULL or A gets empty.
        if(b-bi>ai):
            bi=ai+bi
            ai=0
        else:
            ai=ai-(b-bi)
            bi=b
    elif(op==6):
        if(a-ai>bi):
            ai=ai+bi
            bi=0
        else:
            bi=bi-(a-ai)
            ai=0
    elif(op==7):
        bi=ai+bi
        ai=0
    elif(op==8):
        ai=ai+bi
        bi=0
    print(ai,bi)