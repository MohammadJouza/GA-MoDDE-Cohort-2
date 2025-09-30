import sys

import inspect

def p_w_l_n(message, *args):
    # all_args = " ".join(args)
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    line_number = caller_frame.f_lineno
    print(f"L-{line_number}: {message}")
    if len(args) > 1:
        print("+PAR:", *args)