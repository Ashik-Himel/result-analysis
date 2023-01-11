openResult = open("result.txt")
readResult = openResult.readlines()
resultList = []
for i in readResult:
    singleResult = ""
    for j in i:
        if j in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            singleResult += j
    if len(singleResult) == 0:
        resultList.append(0)
    else:
        resultList.append(float(singleResult))


openName = open("student_name.txt")
readName = openName.readlines()
nameList = []
for i in readName:
    if "\n" in i: nameList.append(i[:-2].title())
    else: nameList.append(i.title())


idNameResult = []
for i in range(len(resultList)):
    idNameResult.append([i+1, nameList[i], resultList[i]])


print("FALL-2022 SEMISTER RESULT".center(50))
print("==================================================\n")
key = int(input("Press 1 for sorted result, Press 2 for unsorted result: "))
print("\n\n")

def resultFunc():
    print("ID".ljust(5), "Name".ljust(25), "Result", sep="")
    print("===========================================")
    for i in range(len(idNameResult)):
            print(str(idNameResult[i][0]).ljust(5), str(idNameResult[i][1]).ljust(25), idNameResult[i][2], sep="")

def sortedResultFunc():
    sortedResult = sorted(idNameResult, key=lambda i: i[2], reverse=True)
    print("SL".ljust(5), "ID".ljust(5), "Name".ljust(25), "Result", sep="")
    print("=================================================")
    for i in range(len(sortedResult)):
            print(f"{str(i+1)}.".ljust(5) ,str(sortedResult[i][0]).ljust(5), str(sortedResult[i][1]).ljust(25), sortedResult[i][2], sep="")

if key == 1:
    sortedResultFunc()
elif key == 2:
    resultFunc()
else:
    print("You entered a wrong key!")


print("""\n\n===============================================================================
===============================================================================""")
input("Press enter to exit: ")