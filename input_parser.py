from emitter import Emitter
from receiver import Receiver
from mirror import Mirror

'''
Name:   Weicheng Wang
SID:   540396663
Unikey: WWAN0525


input_parser - A module that parses the inputs of the program. 
We define parsing as checking the validity of what has been entered 
to determine if it's valid. If it's not valid, an appropriate message 
should be printed. Whenever we retrieve input in the program, we 
should be using functions from this module to validate it.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def parse_size(user_input: str) -> tuple[int, int] | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Checks if user_input is a valid input for the size of the circuit board by
    performing the following checks:
      1)  user_input contains exactly 2 tokens. If there are 2 tokens, we
          interpret the first token as width and the second token as height for
          the remaining checks.
      2)  width is an integer.
      3)  height is an integer.
      4)  width is greater than zero.
      5)  height is greater than zero.

    Parameters
    ----------
    user_input - the user input for the circuit's board size

    Returns
    -------
    If all checks pass, returns a tuple containing the width and height of
    the circuit board.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.

    Example 1:
    # >>> size = parse_size('18 0')
    # Error: height must be greater than zero
    # >>> size
    # None
    #
    # Example 2:
    # >>> size = parse_size('18 6')
    # >>> size
    (18, 6)
    '''
    size = user_input.strip().split(' ')
    if len(size) != 2:
        print('Error: <width> <height>')
        return None
    else:
        try:
            width = int(size[0])
        except ValueError:
            print('Error: width is not an integer')
            return None
        try:
            height = int(size[1])
        except ValueError:
            print('Error: height is not an integer')
            return None

        if width <= 0:
            print('Error: width must be greater than zero')
            return None
        if height <= 0:
            print('Error: height must be greater than zero')
            return None

        return width, height


def parse_emitter(user_input: str) -> Emitter | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Checks if user_input is a valid input for creating an emitter by
    performing the following checks in order for any errors: 
      1)  user_input contains exactly 3 tokens. If there are 3 tokens, we 
          interpret the first token  as symbol, the second token as x and the 
          third token as y for the remaining checks.
      2)  symbol is a character between 'A' to 'J'. 
      3)  x is an integer.
      4)  y is an integer.
      5)  x is greater than 0.
      6)  y is greater than 0

    Parameters
    ----------
    user_input - the user input for creating a new emitter

    Returns
    -------
    If all checks pass, returns a new Emitter instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.
    '''
    name_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    emitter = user_input.strip().split(' ')
    if len(emitter) != 3:
        print('Error: <symbol> <x> <y>')
        return None
    else:
        try:
            symbol = emitter[0]
            index = 0
            ok = False
            while not ok and index < len(name_list):
                if symbol == name_list[index]:
                    ok = True
                index += 1
            if not ok:
                print('Error: symbol is not between \'A\'-\'J\'')
                return None
        except ValueError:
            print('Error: symbol is not a character')
            return None
        try:
            x = int(emitter[1])
        except ValueError:
            print('Error: x is not an integer')
            return None
        try:
            y = int(emitter[2])
        except ValueError:
            print('Error: y is not an integer')
            return None
        if x < 0:
            print('Error: x cannot be negative')
            return None
        if y < 0:
            print('Error: y cannot be negative')
            return None
        return Emitter(symbol, x, y)


def parse_receiver(user_input: str) -> Receiver | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Identical to parse_emitter, with the only differences being
    that the symbol must be between 'R0' to 'R9', and that a new Receiver
    instance is returned if all checks pass.

    Parameters
    ----------
    user_input - the user input for creating a new receiver

    Returns
    -------
    If all checks pass, returns a new Receiver instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    name_list = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9']
    receiver = user_input.strip().split(' ')
    if len(receiver) != 3:
        print('Error: <symbol> <x> <y>')
        return None
    else:
        try:
            symbol = receiver[0]
            index = 0
            ok = 0
            while index < len(name_list):
                if symbol == name_list[index]:
                    ok = 1
                    break
                index += 1
            if not ok:
                print('Error: symbol is not between R0-R9')
                return None
        except ValueError:
            print('Error: symbol is not a character')
            return None
        try:
            x = int(receiver[1])

        except ValueError:
            print('Error: x is not an integer')
            return None
        try:
            y = int(receiver[2])

        except ValueError:
            print('Error: y is not an integer')
            return None
        if x < 0:
            print('Error: x cannot be negative')
            return None
        if y < 0:
            print('Error: y cannot be negative')
            return None
        return Receiver(symbol, x, y)


def parse_pulse_sequence(line: str) -> tuple[str, int, str] | None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Checks if line is valid for setting the pulse sequence of an emitter by
    performing the following checks in order for any errors:
      1)  line contains exactly 3 tokens.
          If there are 3 tokens, we interpret the first token as symbol, the
          second token as frequency and the third token as direction for the
          remaining checks.
      2)  symbol is a character between 'A' to 'J'.
      3)  frequency is an integer.
      4)  frequency is greater than zero.
      5)  direction is either 'N', 'E', 'S' or 'W'.

    Parameters
    ----------
    user_input - the user input for setting the pulse sequence of an emitter

    Returns
    -------
    If all checks pass, returns a tuple containing the specified symbol,
    frequency and direction which can be used for setting the pulse sequence
    of the emitter.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    name_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    direction_list = ['N', 'E', 'S', 'W']
    if len(line.split(' ')) != 3:
        print('Error: <symbol> <frequency> <direction>')
        return None
    try:
        symbol = line.split(' ')[0]
        index = 0
        ok = False
        while not ok and index < len(name_list):
            if symbol == name_list[index]:
                ok = True
            index += 1
        if not ok:
            print('Error: symbol is not between \'A\'-\'J\'')
            return None
    except ValueError:
        print('Error: symbol is not a character.')
        return None
    try:
        frequency = int(line.split(' ')[1])
        if frequency <= 0:
            print('Error: frequency must be greater than zero')
            return None
    except ValueError:
        print('Error: frequency is not an integer')
    try:
        direction = line.split(' ')[2].strip()
        index = 0
        ok = False
        while not ok and index < len(direction_list):
            if direction == direction_list[index]:
                ok = True
            index += 1
        if not ok:
            print('Error: direction must be \'N\', \'E\', \'S\' or \'W\'')
            return None
    except ValueError:
        print('Error: direction is not a character')
        return None
    return symbol, frequency, direction


def parse_mirror(user_input: str) -> Mirror | None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Checks if user_input is a valid input for creating a mirror by performing
    the following checks in order for any errors:
      1)  user_input contains exactly 3 tokens. If there are 3 tokens, we
          interpret the first token  as symbol, the second token as x and the
          third token as y for the remaining checks.
      2)  symbol is either '/', '\', '>', '<', '^' or 'v'
      3)  x is an integer.
      4)  y is an integer.
      5)  x is greater than 0.
      6)  y is greater than 0.

    Parameters
    ----------
    user_input - the user input for creating a mirror

    Returns
    -------
    If all checks pass, returns a new Mirror instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    symbol_list = ['/', '\\', '>', '<', '^', 'v']

    mirror = user_input.split(' ')
    if len(mirror) != 3:
        print('Error: <symbol> <x> <y>')
        return None
    else:
        try:
            symbol = mirror[0]
            index = 0
            ok = False
            while index < len(symbol_list):
                if symbol == symbol_list[index]:
                    ok = True
                    break
                index += 1
            if not ok:
                print('Error: symbol must be \'/\', \'\\\', \'>\', \'<\', \'^\' or \'v\'')
                return None
        except ValueError:
            print('Error: symbol not a character.')
            return None
        try:
            x = int(mirror[1])
            if x < 0:
                print('Error: x cannot be negative')
                return None
        except ValueError:
            print('Error: x is not an integer')
            return None
        try:
            y = int(mirror[2])
            if y < 0:
                print('Error: y cannot be negative.')
                return None
        except ValueError:
            print('Error: x is not an integer.')
            return None
        return Mirror(symbol, x, y)
