def ap(y):
    return len(y)*(y[0]+y[-1])//2

print ap(range(int(raw_input().split(" ")[0]) + 1))
