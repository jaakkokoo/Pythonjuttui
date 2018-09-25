from stack import Stack

JaakonStack = Stack()

JaakonStack.push("test")
JaakonStack.push("string")

print("string ==", JaakonStack.pop())
print("test ==",JaakonStack.pop())
print("True ==", JaakonStack.is_empty())

JaakonStack.push("testing")

print("testing ==", JaakonStack.top())
print("testing ==", JaakonStack.pop())

print("True ==", JaakonStack.is_empty())


