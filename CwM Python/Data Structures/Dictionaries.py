point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 4
print(point)

print(point.get("a", 0))

# value = []
# for x in range(5):
#    value.append(x * 2)

# values = {x * 2 for x in range(5)}