import random

testList = []

for i in range (1, 11, 1):
    testList.append(random.randrange(1,100))

print(testList)

sortedTestList = sorted(testList)
print(sortedTestList)


randomLinksList = [
    "https://www.instagram.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://x.com/home"
    ]

print(randomLinksList)
for link in randomLinksList:
    print(link.removeprefix("https://"))

howManyEvens = 0
howManyOdd = 0
for i in testList:
    if i % 2 == 0:
        howManyEvens += 1
    elif i % 2 == 1:
        howManyOdd += 1


print(f"How much evens: {howManyEvens}")
print(f"How much odds: {howManyOdd}")

for x in range (0, len(testList)):
    print(testList[x])

print("\n")

for y in testList:
    print(y)

print("\n")

for item in testList[:]:
    if item % 2 == 0:
        testList.remove(item)

print(testList)


firstList = [1,2,3,4,6,7,8]
secondList = [1,3,3,8,6,7,9,10]

#laczanie list bez powtórzeń
def mergeArrays(array1, array2):
    return sorted(set(array1 + array2))

thirdList = mergeArrays(firstList, secondList)


print(firstList)
print(secondList)
print(thirdList)
