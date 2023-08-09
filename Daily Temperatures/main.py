temperatures = [30, 60, 90]
record = [0] * len(temperatures)


def fonc():

    for num in range(len(temperatures)):
        sayac = 0
        for i in range(num+1, len(temperatures)):
            sayac = sayac + 1
            if temperatures[num] < temperatures[i]:
                record[num] = sayac
                sayac = 0
                break

    return record

def fonc2():
    result = [0] * len(temperatures)
    myStack = []
    for ix, temperature in enumerate(temperatures):
        while myStack and temperature > myStack[-1][0]:
            stackTemp, stackIndex = myStack.pop()
            result[stackIndex] = ix - stackIndex
        myStack.append([temperature, ix])
    return result


print(fonc2())
print(fonc())
