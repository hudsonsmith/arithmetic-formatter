from arithmetic_formatter import arithmetic_arranger

print(
    """
             (Arithmetic Formatter 1.0!)
/\\____/\\    /
|+    -|   /
| _/\_ |  /
|_\__/_|
|--DOG-|

"""
)

while True:
    question = input("EXPRESSION: ")

    if not " + " in question or not " - " in question:
        question = question.replace("+", " + ").replace("-", " - ")

    print(arithmetic_arranger([question], True))
