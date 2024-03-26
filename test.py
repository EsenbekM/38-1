
dct = {
    "name": "John",
    "age": 25
}

variant_1 = dct["name"]
variant_2 = dct.get("nam", "default_value")

print(variant_1)
print(variant_2)