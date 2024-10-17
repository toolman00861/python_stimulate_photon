import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit

'''
Name:  Weicheng Wang
SID:  540396663
Unikey: WWAN0525

run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    index = 0
    while index < len(args):
        if args[index].strip() == '-RUN-MY-CIRCUIT':
            return True
        index += 1
    return False



def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    index = 0
    while index < len(args):
        if args[index].strip() == '-ADD-MY-MIRRORS':
            return True
        index += 1
    return False


def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    print("Creating circuit board...")
    user_input = input("> ").strip()
    user_input = user_input.replace('#', '')
    size = input_parser.parse_size(user_input.strip())
    while size is None:
        user_input = input('> ')
        user_input = user_input.replace("#", "")
        size = input_parser.parse_size(user_input.strip())
    laser_circuit = LaserCircuit(size[0], size[1])
    print(f"{laser_circuit.get_width()}x{laser_circuit.get_height()} board created.\n")

    print("Adding emitter(s)...")
    while True:
        if len(laser_circuit.get_emitters()) >= 10:
            break

        user_input = input('> ').strip()

        if user_input == "END EMITTERS":
            break
        user_input = user_input.replace("#", "")
        emitter = input_parser.parse_emitter(user_input.strip())
        if emitter is None:
            continue
        laser_circuit.add_emitter(emitter)
    print(f"{len(laser_circuit.get_emitters())} emitter(s) added.\n")

    print("Adding receiver(s)...")
    while True:
        if len(laser_circuit.get_receivers()) >= 10:
            break

        user_input = input('> ').strip()

        if user_input == "END RECEIVERS":
            break
        user_input = user_input.replace("#", "")
        receiver = input_parser.parse_receiver(user_input.strip())
        if receiver is None:
            continue
        laser_circuit.add_receiver(receiver)
    print(f"{len(laser_circuit.get_receivers())} receiver(s) added.\n")

    return laser_circuit


def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    print("Setting pulse sequence...")
    line_num = 1
    emitters = circuit.get_emitters()
    added_emitter = []
    index = 0
    waiting_add_emitter = []
    while index < len(emitters):
        waiting_add_emitter.append(emitters[index].get_symbol())
        index += 1

    while True:
        def check_add_emitter(symbol: str) -> bool:
            index_ = 0
            while index_ < len(added_emitter):
                if symbol == added_emitter[index_]:
                    return True
                index_ += 1
            return False

        def check_waiting_add_emitter(symbol: str) -> bool:
            index_ = 0
            while index_ < len(waiting_add_emitter):
                if symbol == waiting_add_emitter[index_]:
                    return True
                index_ += 1
            return False

        def find_index(symbol: str) -> int:
            index_ = 0
            while index_ < len(emitters):
                if symbol == emitters[index_].get_symbol():
                    return index_
                index_ += 1
            return -1

        def pop_waiting_add_emitter(symbol: str) -> None:
            index_ = 0
            while index_ < len(waiting_add_emitter):
                if symbol == waiting_add_emitter[index_]:
                    waiting_add_emitter.pop(index_)
                    return
                index_ += 1

        # 更新等待增加的emitter列表
        index = 0
        while index < len(added_emitter):
            pop_waiting_add_emitter(added_emitter[index])
            index += 1

        index = 0
        emitters_str = []

        # 检查剩余的emitter：
        while index < len(waiting_add_emitter):
            emitters_str.append(waiting_add_emitter[index])
            index += 1
        emitters_str = sorted(emitters_str)
        emitters_str = '-- (' + ', '.join(emitters_str) + ')'
        print(emitters_str)

        # 读取指令
        
        line = file_obj.readline()
        if line == "":
            break
        print(f'Line {line_num}: {line.strip()}')
        pulse_sequence = input_parser.parse_pulse_sequence(line.strip())
        line_num += 1
        if pulse_sequence is None:
            continue

        # 对等待添加的emitter进行添加操作
        index = 0
        while index < len(waiting_add_emitter):
            if check_add_emitter(pulse_sequence[0]):
                print(f"Error: emitter {pulse_sequence[0]} already has its pulse sequence set.")
                index += 1
                continue
            if not check_waiting_add_emitter(pulse_sequence[0]):
                print(f"Error: emitter '{pulse_sequence[0]}' does not exist")
                break
            change_index = find_index(pulse_sequence[0])
            if change_index != -1:
                emitters[change_index].set_pulse_sequence(pulse_sequence[1], pulse_sequence[2])
                added_emitter.append(pulse_sequence[0])
                break
            index += 1

        if len(added_emitter) == len(emitters):
            print("Pulse sequence set.\n")
            file_obj.close()
            break


def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    print("Adding mirror(s)...")
    while True:
        user_input = input('> ').strip()
        if user_input == "END MIRRORS":
            break
        user_input = user_input.replace('#', '')
        mirror = input_parser.parse_mirror(user_input)
        if mirror is None:
            continue
        circuit.add_mirror(mirror)
    print(f"{len(circuit.get_mirrors())} mirror(s) added.")


def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''
    laser_circuit = initialise_circuit()
    if is_add_my_mirrors_enabled(args):
        print('<ADD-MY-MIRRORS FLAG DETECTED!>\n')
        add_mirrors(laser_circuit)

    laser_circuit.print_board()

    if is_run_my_circuit_enabled(args):
        print('\n<RUN-MY-CIRCUIT FLAG DETECTED!>\n')
        file_path = '/home/input/pulse_sequence.in'
        try:
            file_obj = open(file_path, 'r')
            set_pulse_sequence(laser_circuit, file_obj)
            laser_circuit.run_circuit()
        except FileNotFoundError:
            print(f"Error: -RUN-MY-CIRCUIT flag detected but {file_path} does not exist")




if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    # main(sys.argv)
    circuit = LaserCircuit(2, 2)
    # circuit.add_emitter(Emitter('A', 0, 0))
    circuit.add_receiver(Receiver('R0', 0, 1))
    # set_pulse_sequence(circuit, open('home/input/pulse_sequence.in', 'r'))
    circuit.print_board()
    circuit.run_circuit()
