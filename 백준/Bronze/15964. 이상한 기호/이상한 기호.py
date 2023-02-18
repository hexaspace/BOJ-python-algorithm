def new_tool(a,b):
    return (a+b)*(a-b)


a, b = map(int, input().split())
print(new_tool(a,b))