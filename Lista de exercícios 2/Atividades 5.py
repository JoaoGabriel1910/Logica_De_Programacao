paisA = 90000000 
paisB = 140000000 
i = 0 

while paisA < paisB:
    paisA = (paisA * 1.035)
    paisB = (paisB * 1.01)
    i += 1

print(i, "Anos")