import os
import random
from typing import Callable

# Rather than having the `rmsfact()` function parse the source file each time, using a closure like
# this allows us to offload the parsing and data validation (not that there is any at the moment)
# and save time when `rmsfact()` is called.


def _new_rmsfact() -> Callable:
    """
    Generate an `rmsfact()` function

    This function runs when the package is imported. It loads the "facts" from the text file
    and returns a function that will retrieve a random fact.

    Returns
    -------

    function
        A function that, when called, returns a random fact.

    Examples
    --------

    >>> f = _new_rmsfact()
    >>> fact = f()
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.normpath("{ROOT_DIR}/data".format(ROOT_DIR=ROOT_DIR))
    FACT_FILE = os.path.normpath("{DATA_DIR}/rmsfact.txt".format(DATA_DIR=DATA_DIR))

    with open(FACT_FILE, "r") as f:
        lines = f.readlines()
        facts = [
            line.strip() for line in lines if line.strip() and not line.startswith("#")
        ]

    n_facts = len(facts)

    def rmsfact() -> str:
        """
        Return a random fact about Richard M. Stallman

        Returns
        -------

        str
            A randomly-selected fact.
        """
        idx = random.randint(0, n_facts - 1)
        return facts[idx]

    return rmsfact
