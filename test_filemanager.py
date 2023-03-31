import io
import sys
# from HW_3_Quiz_Game.victory import quiz_game

# Если не вызывать тестируемую функцию, а прописать её в коде (ниже закомментировано и реализовано в sandbox.py),
# то тест работает, в текущем написании тест не работает.
from console_file_manager import print_lines


# def print_lines():
#     return print('-' * 50)


def test_print_lines():
    capturedOutput = io.StringIO()                              # Create StringIO object
    sys.stdout = capturedOutput                                 # and redirect stdout.
    print_lines()                                               # Call function.
    assert capturedOutput.getvalue() == str('-' * 50 + '\n')
    sys.stdout = sys.__stdout__                                 # Reset redirect.
    # print('Captured', capturedOutput.getvalue())              # Now works as before.







