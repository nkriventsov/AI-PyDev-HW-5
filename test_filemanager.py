import io
import sys
# from HW_3_Quiz_Game.victory import quiz_game

from console_file_manager import print_lines


@print_lines
def sum_test():
    return

def test_print_lines():
    capturedOutput = io.StringIO()                              # Create StringIO object
    sys.stdout = capturedOutput                                 # and redirect stdout.
    sum_test()                                                  # Call function.
    assert capturedOutput.getvalue() == str(('-' * 50 + '\n')*2)
    sys.stdout = sys.__stdout__                                 # Reset redirect.
    # print('Captured', capturedOutput.getvalue())              # Now works as before.







