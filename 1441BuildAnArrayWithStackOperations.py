operations = []
stack = []
pos = 0
num = 1
while num <= n and len(stack) < len(target):
    stack.append(num)
    operations.append("Push")
    if num != target[pos]:
        stack.pop(0)
        operations.append("Pop")
    pos += 1
    num += 1
print (operations)