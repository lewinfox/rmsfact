import os
import pickle
import random


class RMSFact(object):
    def __init__(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_DIR = os.path.normpath(f"{ROOT_DIR}/data")
        self._BINARY_FILE = os.path.normpath(f"{DATA_DIR}/rmsfact.dat")
        self._TEXT_FILE = os.path.normpath(f"{DATA_DIR}/rmsfact.txt")

        if not os.path.exists(self._BINARY_FILE):
            self._create_binary_data()

        with open(self._BINARY_FILE, "rb") as f:
            self._facts = pickle.load(f)

        self._n_facts = len(self._facts)

    def _read_source_data(self):
        with open(self._TEXT_FILE, "r") as f:
            lines = f.readlines()
            facts = [line.strip("\n")
                     for line in lines if not line.startswith("#")]
        return facts

    def _create_binary_data(self):
        facts = self._read_source_data()
        with open(self._BINARY_FILE, "wb") as f:
            pickle.dump(facts, f)

    def rmsfact(self):
        idx = random.randint(0, self._n_facts)
        return self._facts[idx]


if __name__ == "__main__":
    rms = RMSFact()
    rms.rmsfact()
