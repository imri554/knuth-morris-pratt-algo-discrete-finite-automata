import sys


def createFailureFunction(pattern):
    length = len(pattern)

    result = {1: 0}
    i = 0
    for j in range(2, length + 1):
        i = result.get(j - 1)
        while pattern[j - 1] is not pattern[i] and (i > 0):
            i = result.get(i)
        if pattern[j - 1] is not pattern[i] and (i == 0):
            result[j] = 0
        else:
            result[j] = i + 1

    return result


def getDestination(j, a):
    if a == sequence[j]:
        return j + 1
    if j == 0 and a is not sequence[0]:
        return 0
    return getDestination(failureFunction.get(j), a)


lines = []
inputFile = sys.argv[1]

outputPath = sys.argv[2]

file_object = open(inputFile, "r")
for line in file_object:
    for phrase in line.split():
        lines.append(phrase.upper())

sequence = lines[0]

outputFile = open(outputPath, 'w')

linesToWrite = []

failureFunction = createFailureFunction(sequence)
print(failureFunction)

outputFile.write("digraph dfa {" + "\n")

for i in range(0, len(sequence)):
    line = str(i) + "->" + str((i + 1)) + " " + "[ label = \"" + sequence[i] + "\"]"
    outputFile.write(line)
    outputFile.write('\n')

    if i == (len(sequence) - 1):
        line = str(i + 1) + " " + "[peripheries = 2]"
        outputFile.write(line)
        outputFile.write('\n')
used = []
for i in range(0, len(sequence)):
    #if sequence[i] is not sequence[0] and not (sequence[i] in used):
    if not (sequence[i] in used):
        used.append(sequence[i])

for i in range(1, len(sequence)):
    for offendingLetter in used:
        if offendingLetter is not sequence[i] and (getDestination(i, offendingLetter) != 0):
            line = str(i) + "->" + str(getDestination(i, offendingLetter)) + " " + "[ label = \"" + offendingLetter + "\"]"
            outputFile.write(line)
            outputFile.write('\n')
#     if sequence[i] is proceedLetter:
#         while sequence[i] is proceedLetter:
#             failureDestination = i + 1
#             proceedLetter = sequence[failureDestination]
#         if failureDestination != 0:
#             line = str(i) + "->" + str(failureDestination) + " " + "[ label = \"" + str(proceedLetter) + "\"]"
#     elif failureDestination != 0:
#         line = str(i) + "->" + str(failureFunction.get(i)) + " " + "[ label = \"" + "?" + "\"]"
#     outputFile.write(line)
#     outputFile.write('\n')

# for i in range(1, len(sequence)):
#     proceedLetter = sequence[failureFunction.get(i)]
#     failureDestination = failureFunction.get(i)
#     print(failureDestination)
#     if sequence[i] is proceedLetter:
#         while sequence[i] is proceedLetter:
#             failureDestination = i + 1
#             proceedLetter = sequence[failureDestination]
#         if failureDestination != 0:
#             line = str(i) + "->" + str(failureDestination) + " " + "[ label = \"" + str(proceedLetter) + "\"]"
#     elif failureDestination != 0:
#         line = str(i) + "->" + str(failureFunction.get(i)) + " " + "[ label = \"" + "?" + "\"]"
#     outputFile.write(line)
#     outputFile.write('\n')

outputFile.write("}")
