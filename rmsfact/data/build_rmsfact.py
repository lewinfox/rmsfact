import os
import pickle


def _build_rmsfact():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    with open(f"{THIS_DIR}/rmsfact.txt", "r") as f:
        lines = f.readlines()
        facts = [line.strip("\n")
                 for line in lines if not line.startswith("#")]

    OUTFILE = f"{THIS_DIR}/rmsfact.dat"

    with open(OUTFILE, "wb") as f:
        pickle.dump(facts, f)

    # Read back in to verify
    with open(OUTFILE, "rb") as f:
        new_facts = pickle.load(f)

    assert new_facts == facts, "New data does not match old data"


if __name__ == "__main__":
    _build_rmsfact()