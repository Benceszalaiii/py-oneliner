def handleInput(fileName: str):
    with open(fileName) as file:
        return file.read().splitlines()


def toOneLiner(lines: list[str], char="X", nullChar="-"):
    lineInstructions: list[str] = []
    for line in lines:
        indexes = [i for i in range(len(line)) if line[i] == char]
        lineInstructions.append(
            f"[\"{char}\" if [{", ".join(str(j) for j in indexes)}].__contains__(i) else \"{nullChar}\" for i in range({len(line)})]"
        )
    return f"[print(*line, end=\"\\n\") for line in [{", ".join(lineInstructions)}]]"


solution = toOneLiner(handleInput("fa.txt"))
with open("oneliner.py", "w") as file:
    file.write(solution)
