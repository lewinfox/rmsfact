import sys
import unittest

# Make sure the package is importable
sys.path.append("../rmsfact")

loader = unittest.TestLoader()
test_suite = loader.discover("test")
test_runner = unittest.TextTestRunner()
result = test_runner.run(test_suite)

# Ensure that if any tests fail we return a failure code from the process. This is useful for things
# like `make` and CI/CD pipelines.
if result.wasSuccessful():
    exit(0)

exit(1)
