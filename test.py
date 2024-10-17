from emitter import Emitter
from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
Name:  Weicheng Wang
SID:  540396663
Unikey: WWAN0525

This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters, 
or implementations...), however, DO NOT ALTER the code in circuit_for_testing 
file, which provides the circuit. The circuit can be retrieved by calling 
get_my_lasercircuit(), and it should be used as an argument for the 
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''

def check_emitter(emitter: Emitter, except_name: str, except_frequency: int, except_direction: str):
    if emitter.get_symbol() != except_name:
        return False
    if emitter.get_frequency() != except_frequency:
        return False
    if emitter.get_direction() != except_direction:
        return False
    return True

def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Positive test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    # my_circuit.print_board()

    # TODO: Check if emitters' pulse sequence are correctly set up
    assert check_emitter(my_circuit.get_emitters()[0], 'A', 100, 'E'), "Emitter A's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[1], 'B', 100, 'W'), "Emitter B's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[2], 'C', 100, 'W'), "Emitter C's pulse sequence is incorrect"

    # don't forget to close the file
    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    # my_circuit.print_board()

    # TODO: Check if emitters' pulse sequence are correctly set up
    assert check_emitter(my_circuit.get_emitters()[0], 'A', 100, 'S'), "Emitter A's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[1], 'B', 200, 'W'), "Emitter B's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[2], 'C', 300, 'N'), "Emitter C's pulse sequence is incorrect"

    file_obj.close()

def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # TODO: Check if emitters' pulse sequence are correctly set up
    assert check_emitter(my_circuit.get_emitters()[0], 'A', 100, 'S'), "Emitter A's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[1], 'B', 200, 'W'), "Emitter B's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[2], 'C', 300, 'N'), "Emitter C's pulse sequence is incorrect"

    # don't forget to close the file
    file_obj.close()


def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # TODO: Check if emitters' pulse sequence are correctly set up
    assert check_emitter(my_circuit.get_emitters()[0], 'A', 100, 'S'), "Emitter A's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[1], 'B', 200, 'W'), "Emitter B's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[2], 'C', 300, 'N'), "Emitter C's pulse sequence is incorrect"

    file_obj.close()


def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # TODO: Check if emitters' pulse sequence are correctly set up
    assert check_emitter(my_circuit.get_emitters()[0], 'A', 0, 'S'), "Emitter A's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[1], 'B', 0, 'W'), "Emitter B's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[2], 'C', 0, 'N'), "Emitter C's pulse sequence is incorrect"

    file_obj.close()


def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # TODO: Check if emitters' pulse sequence are correctly set up
    assert check_emitter(my_circuit.get_emitters()[0], 'A', 100, 'S'), "Emitter A's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[1], 'B', 200, 'W'), "Emitter B's pulse sequence is incorrect"
    assert check_emitter(my_circuit.get_emitters()[2], 'C', 300, 'N'), "Emitter C's pulse sequence is incorrect"

    file_obj.close()

if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), 'home/input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), 'home/input/pulse_sequence_2.in')
    # You should have more below...
    # negative test
    # negative_test_1(get_my_lasercircuit(), 'home/input/pulse_sequence_3.in')
    # negative_test_2(get_my_lasercircuit(), 'home/input/pulse_sequence_4.in')
    # edge test
    # edge_test_1(get_my_lasercircuit(), 'home/input/pulse_sequence_5.in')
    edge_test_2(get_my_lasercircuit(), 'home/input/pulse_sequence_6.in')

