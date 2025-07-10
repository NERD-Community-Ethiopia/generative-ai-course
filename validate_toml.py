import toml

try:
    with open("pyproject.toml", "r") as f:
        toml.load(f)
    print("pyproject.toml is valid")
except Exception as e:
    print(f"Error in pyproject.toml: {e}")