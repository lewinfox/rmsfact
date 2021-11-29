import os
import pickle
import random
from typing import Callable


# Rather than having the `rmsfact()` function parse the source file each time, using a closure like
# this allows us to offload the parsing and data validation (not that there is any at the moment)
# and save time when `rmsfact()` is called.
#
# TODO: Is there an advantage to using `pickle` or similar to store a binary version of the `facts`
#       object rather than parsing the text file every time the package is loaded?


def _new_rmsfact() -> Callable:
    """
    Generate an `rmsfact()` function

    This function runs when the package is imported. It loads the "facts" from their binary store
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
    # TODO: Is there a more Pythonic way of referring to the file?
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.normpath("{ROOT_DIR}/data".format(ROOT_DIR=ROOT_DIR))
    FACT_FILE = os.path.normpath("{DATA_DIR}/rmsfact.dat".format(DATA_DIR=DATA_DIR))
    # TODO: Error handling needed here?
    with open(FACT_FILE, "rb") as f:
        facts = pickle.load(f)

    n_facts = len(facts)

    def rmsfact() -> str:
        """
        Return a random fact about Richard M. Stallman

        Returns
        -------

        str
            A randomly-selected fact.
        """
        idx = random.randint(0, n_facts)
        return facts[idx]

    return rmsfact
