dictionary = {"salt": 5, "peper": 6}

#print(*dictionary)

for key, value in dictionary.items():
    print(f"{key} -> {value}")


print(', '.join([f"{key}: {value}" for key, value in dictionary.items()]))