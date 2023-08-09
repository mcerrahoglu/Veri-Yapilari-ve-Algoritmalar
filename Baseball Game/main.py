ops = ["5", "2", "C", "D", "+"]
record = []


def fonc():
    score = 0
    for num in range(len(ops)):

        if ops[num] == "+":
            record.append(int(record[-1]) + int(record[-2]))

        elif ops[num] == "C":
            record.pop(-1)

        elif ops[num] == "D":
            a = int(record[-1])
            a = a * 2
            record.append(a)
        else:
            record.append(int(ops[num]))

    return sum(record)


print(fonc())
