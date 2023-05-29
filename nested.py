def get_value_from_nested_object(obj, key):
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for k, v in obj.items():
            result = get_value_from_nested_object(v, key)
            if result is not None:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = get_value_from_nested_object(item, key)
            if result is not None:
                return result
    return None


Expected output::
obj1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
result1 = get_value_from_nested_object(obj1, key1)
print(result1)  # Output: d