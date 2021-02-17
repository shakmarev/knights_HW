from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, And(AKnave, AKnight)),  # Suppose that A says truth: "I am both a knight and a knave".
    Implication(AKnave, Not(And(AKnave, AKnight)))  # Suppose that A lies.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, And(AKnave, BKnave)),  # Suppose that A says truth: "We are both knaves".
    Implication(AKnave, Not(And(AKnave, BKnave)))  # Suppose that A lies.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # Suppose that A says truth: "We are the same kind".
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),  # Suppose that A lies.
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),  # Suppose that B says truth: "We are of different kinds".
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))  # Suppose that B lies.
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Implication(AKnight, Or(AKnight, AKnave)),  # Suppose that A says truth: "I am a knight" or "I am a knave".
    Implication(AKnave, Not(Or(AKnight, AKnave))),  # Suppose that A lies.
    Implication(BKnight, Implication(AKnight, AKnave)),  # Suppose that B says truth: "A said 'I am a knave'".
    Implication(BKnave, Not(Implication(AKnight, AKnave))),  # Suppose that B lies.
    Implication(BKnight, CKnave),  # Suppose that B says truth: "C is a knave".
    Implication(BKnave, Not(CKnave)),  # Suppose that B lies.
    Implication(CKnight, AKnight),  # Suppose that C says truth: "A is a knight".
    Implication(CKnave, Not(AKnight))  # Suppose that C lies.
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
