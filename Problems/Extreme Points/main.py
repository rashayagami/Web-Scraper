# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

t = {y: x for x, y in test_dict.items()}
print("min:", t.get(min(t)))
print("max:", t.get(max(t)))
