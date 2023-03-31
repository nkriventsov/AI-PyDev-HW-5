import io
import sys


def print_lines():
    return print('-' * 50)


def test_print_lines():
    capturedOutput = io.StringIO()                              # Create StringIO object
    sys.stdout = capturedOutput                                 # and redirect stdout.
    print_lines()                                               # Call function.
    assert capturedOutput.getvalue() == str('-' * 50 + '\n')
    sys.stdout = sys.__stdout__                                 # Reset redirect.
    # print('Captured', capturedOutput.getvalue())                # Now works as before.
