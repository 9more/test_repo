from tools.insurance import run

result = run(
    {
        "age": 35,
        "sex": "male",
        "bmi": 28.5,
        "children": 2,
        "smoker": "no",
        "region": "northwest",
    }
)

print(result)

