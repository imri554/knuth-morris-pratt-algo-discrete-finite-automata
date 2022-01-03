import sys


# class DFA:
#     def __init__(self):
#         self.startingState = None
#         self.endState = []
#         self.handlers = {}
#
#     def add_state(self, name, handler, end_state = 0):
#         name = name.upper()
#         self.handlers[name] = handler
#         if end_state:
#             self.endState.append(name)
#     def set_start(self, name):
#         self.startingState = name.upper()
#
#     def run(self, package):
#         try:
#             handler = self.handlers[self.startingState]
#         except:
#             raise Exception("must call .set_start before running")
#         if not self.endState:
#             raise Exception("at least one state must be an end state")

def createFailureFunction(pattern):
    length = len(pattern)

    result = {}
    result[1] = 0
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

lines = []

inputFile = sys.argv[1]
file_object = open(inputFile, "r")
for line in file_object:
    for phrase in line.split():
        lines.append(phrase.upper())

text = lines[0]
pattern = lines[1]

record = []
failureFunctionDict = createFailureFunction(pattern)

dfa = {0: {pattern[0]: 1, 'else': 0}}
for i in range(1, len(pattern)):
    dfa[i] = {pattern[i]: i + 1, 'else': failureFunctionDict.get(i)}

dfaState = 0
tapeHead = 0

while tapeHead != len(text):

    if text[tapeHead] is pattern[dfaState]:
        dfaState = dfaState + 1
        tapeHead = tapeHead + 1
        if dfaState is len(pattern):
            #record this?
            record.append((tapeHead-1) - len(pattern) + 1)
            dfaState = failureFunctionDict.get(len(pattern))
    else:
        if dfaState == 0:
            tapeHead = tapeHead + 1
        else:
            dfaState = failureFunctionDict.get(dfaState)
if len(record) == 0:
    print(-1)
else:
    print(record)
