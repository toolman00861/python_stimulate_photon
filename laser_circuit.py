import sorter
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''
Name:  Weicheng Wang
SID:  540396663
Unikey: WWAN0525


LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating 
tasks to the specific components e.g. making each emitter emit a photon, getting 
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class LaserCircuit:

    def __init__(self, width: int, height: int):
        '''        
        Initialise a LaserCircuit instance given a width and height. All 
        lists of components and photons are empty by default.
        board_displayer is initialised to a BoardDisplayer instance. clock is
        0 by default.

        emitters:        list[Emitter]  - all emitters in this circuit
        receivers:       list[Receiver] - all receivers in this circuit
        photons:         list[Photon]   - all photons in this circuit
        mirrors:         list[Mirror]   - all mirrors in this circuit
        width:           int            - the width of this circuit board
        height:          int            - the height of this circuit board
        board_displayer: BoardDisplayer - helper class for storing and 
                                          displaying the circuit board
        clock:           int            - a clock keeping track of how many 
                                          nanoseconds this circuit has run for

        Parameters
        ----------
        width  - the width to set this circuit board to
        height - the width to set this circuit board to
        '''
        self.emitters = []
        self.receivers = []
        self.photons = []
        self.mirrors = []
        self.width = width
        self.height = height
        self.board_displayer = BoardDisplayer(width, height)
        self.clock = 0

    def emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Gets each emitter in this circuit's list of emitters to emit a photon.
        The photons emitted should be added to this circuit's photons list.
        '''
        index = 0
        while index < len(self.emitters):
            self.emitters[index].emit_photon()
            self.photons.append(self.emitters[index].emit_photon())
            index += 1

    def is_finished(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns whether or not this circuit has finished running. The
        circuit is finished running if every photon in the circuit has been
        absorbed.

        Returns
        -------
        True if the circuit has finished running or not, else False.
        '''
        index = 0
        if len(self.photons) == 0:
            return True
        while index < len(self.photons):
            if not self.photons[index].is_absorbed():
                return False
            index += 1
        return True

    def print_emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for each emitter emitting a photon.
        
        It will also need to write the output into a
        /home/output/emit_photons.out output file. 
        
        You can assume the /home/output/ path exists.
        '''
        index = 0
        print()
        print(f'{str(self.clock)}ns: Emitting photons.')
        while index < len(self.emitters):
            if self.emitters[index].frequency > 0:
                print(f'{self.emitters[index].get_symbol()}: {self.emitters[index].get_frequency()}THz, '
                      f'{self.emitters[index].dire()}')
            index += 1
        with open('home/output/emit_photons.out', 'w') as file:
            # file.write(f'{str(self.clock)}ns: Emitting photons.\n')
            index = 0
            while index < len(self.emitters):
                if self.emitters[index].frequency > 0:
                    file.write(f'{self.emitters[index].get_symbol()}: {self.emitters[index].get_frequency()}THz, '
                               f'{self.emitters[index].dire()}\n')
                index += 1
        print()

    def print_activation_times(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the activation times for each receiver, sorted
        by activation time in ascending order. Any receivers that have not
        been activated should not be included.
        
        It will also need to write the output into a
        /home/output/activation_times.out output file.

        You can assume the /home/output/ path exists.
        '''
        active_receivers = []
        index = 0
        while index < len(self.receivers):
            if self.receivers[index].is_activated():
                active_receivers.append(self.receivers[index])
            index += 1
        active_receivers = sorter.sort_receivers_by_activation_time(active_receivers)
        index = 0
        while index < len(active_receivers):
            print(f'{active_receivers[index].symbol}: {active_receivers[index].get_activation_time()}ns')
            index += 1
        print()
        with open('home/output/activation_times.out', 'w') as file:
            index = 0
            while index < len(active_receivers):
                file.write(f'{active_receivers[index].symbol}: '
                           f'{active_receivers[index].get_activation_time()}ns\n')
                index += 1

    def print_total_energy(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the total energy absorbed for each receiver,
        sorted by total energy absorbed in descending order. Any receivers
        that have not been activated should not be included.
        
        It will also need to write the output into a
        /home/output/total_energy_absorbed.out output file.

        You can assume the /home/output/ path exists.
        '''
        active_receivers = []
        index = 0
        while index < len(self.receivers):
            if self.receivers[index].is_activated():
                active_receivers.append(self.receivers[index])
            index += 1
        active_receivers = sorter.sort_receivers_by_total_energy(active_receivers)

        index = 0
        while index < len(active_receivers):
            print(active_receivers[index])
            index += 1

        with open('home/output/total_energy.out', 'w') as file:
            index = 0
            while index < len(active_receivers):
                file.write(str(active_receivers[index]) + '\n')
                index += 1
        print()

    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board()

    def get_collided_emitter(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Emitter | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another emitter in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no emitter occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        An emitter if it has the same position as entity, else None.
        '''
        index = 0
        while index < len(self.emitters):
            if self.emitters[index].get_x() == entity.get_x() and self.emitters[index].get_y() == entity.get_y():
                return self.emitters[index]
            index += 1

    def get_collided_receiver(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Receiver | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another receiver in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no receiver occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A receiver if it has the same position as entity, else None.
        '''
        index = 0
        while index < len(self.receivers):
            if self.receivers[index].get_x() == entity.get_x() and self.receivers[index].get_y() == entity.get_y():
                return self.receivers[index]
            index += 1

    def get_collided_mirror(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Mirror | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another mirror in the 
        circuit. 

        If it does, return the mirror already in the entity's position.
        Else, return None, indicating there is no mirror occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A mirror if it has the same position as entity, else None.
        '''
        index = 0
        while index < len(self.mirrors):
            if self.mirrors[index].get_x() == entity.get_x() and self.mirrors[index].get_y() == entity.get_y():
                return self.mirrors[index]
            index += 1

    def get_collided_component(self, photon: Photon) -> Emitter | Receiver | Mirror | None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Given a photon, returns the component it has collided with (if any).
        A collision occurs if the positions of photon and the component are
        the same.

        Parameters
        ----------
        photon - a photon to check for collision with the circuit's components

        Returns
        -------
        If the photon collided with a component, return that component.
        Else, return None.

        Hint
        ----
        Use the three collision methods above to handle this.
        '''
        if self.get_collided_emitter(photon) is not None:
            return None
        if self.get_collided_receiver(photon) is not None:
            return self.get_collided_receiver(photon)
        if self.get_collided_mirror(photon) is not None:
            return self.get_collided_mirror(photon)
        return None

    def tick(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs a single nanosecond (tick) of this circuit. If the circuit has
        already finished, this method should return out early.
        
        Otherwise, for each photon that has not been absorbed, this method is
        responsible for moving it, updating the board to show its new position
        and checking if it collided with a component (and handling it if did
        occur). At the end, we then increment clock.
        '''
        index = 0
        self.clock += 1
        while index < len(self.photons):
            # move
            self.photons[index].move(self.get_width(), self.get_height())
            self.board_displayer.add_photon_to_board(self.photons[index])
            # check collision
            collided_component = self.get_collided_component(self.photons[index])
            if collided_component is not None:
                self.photons[index].interact_with_component(collided_component, self.clock)
            index += 1

    def run_circuit(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs the entire circuit from start to finish. This involves getting
        each emitter to emit a photon, and continuously running tick until the
        circuit is finished running. All output in regards of running the 
        circuit should be contained in this method.
        '''
        print('========================\n   RUNNING CIRCUIT...\n========================')

        index = 0
        if len(self.emitters) != 0:
            while index < len(self.emitters):
                if self.emitters[index].frequency > 0:
                    self.add_photon(self.emitters[index].emit_photon())
                index += 1
            self.print_emit_photons()

        while not self.is_finished():
            # TODO: call tick
            self.tick()

            # TODO: handle displaying receivers activated and board (if required)
            # HINT: you have a clock keep tracking of how many nanoseconds has passed
            if self.clock % 5 == 0 or self.is_finished():
                # active_receiver
                active_receivers = []
                receiver = self.get_receivers()
                index = 0
                while index < len(receiver):
                    if self.receivers[index].is_activated():
                        active_receivers.append(receiver[index])
                    index += 1

                print(f"{self.clock}ns: {len(active_receivers)}/"
                      f"{len(self.receivers)} receiver(s) activated.")

                self.print_board()
                print('')

        if self.clock == 0:
            print(f"{self.clock}ns: 0/"
                  f"{len(self.receivers)} receiver(s) activated.")
            self.print_board()

        print("Activation times:")
        self.print_activation_times()
        print("Total energy absorbed:")
        self.print_total_energy()

        print('========================\n   CIRCUIT FINISHED!\n========================')

    def add_emitter(self, emitter: Emitter) -> bool:
        '''
        If emitter is not an Emitter instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The emitter's position is within the bounds of the circuit.
          2)  The emitter's position is not already taken by another emitter in
              the circuit.
          3)  The emitter's symbol is not already taken by another emitter in 
              the circuit.
          
        If at any point a check is not passed, an error message is printed
        stating the causeof the error and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  emitter is added in the circuit's list of emitters. emitter
              needs to be added such that the list of emitters remains sorted
              in alphabetical order by the emitter's symbol. You can assume the
              list of emitters is already sorted before you add the emitter.
          2)  emitter's symbol is added into board_displayer.
          3)  The method returns True.   

        Paramaters
        ----------
        emitter - the emitter to add into this circuit's list of emitters

        Returns
        ----------
        Returns true if all checks are passed and the emitter is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter method to check for position collision.
        You will need to find your own way to check for symbol collisions
        with other emitters.
        '''
        if not isinstance(emitter, Emitter):
            print("error")
            return False
        if emitter.get_x() < 0 or emitter.get_x() >= self.width or emitter.get_y() < 0 or emitter.get_y() >= self.height:
            print(
                f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is out-of-bounds of "
                f"{self.get_width()}x{self.get_height()} circuit board")
            return False
        collided_emitter = self.get_collided_emitter(emitter)
        if collided_emitter is not None:
            print(
                f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is already taken by emitter '{collided_emitter.get_symbol()}'")
            return False
        index = 0
        while index < len(self.emitters):
            if emitter.get_symbol() == self.emitters[index].get_symbol():
                print(f"Error: symbol {emitter.get_symbol()} is already taken")
                return False
            index += 1
        self.emitters.append(emitter)
        self.board_displayer.add_component_to_board(emitter)
        return True

    def get_emitters(self) -> list[Emitter]:
        '''Returns emitters.'''
        i = 0
        while i < len(self.emitters):
            j = i + 1
            while j < len(self.emitters):
                if self.emitters[i].get_symbol() > self.emitters[j].get_symbol():
                    self.emitters[i], self.emitters[j] = self.emitters[j], self.emitters[i]
                j += 1
            i += 1
        return self.emitters

    def add_receiver(self, receiver: Receiver) -> bool:
        '''
        If receiver is not a Receiver instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The receiver's position is within the bounds of the circuit.
          2)  The receiver's position is not already taken by another emitter
              or receiver in the circuit.
          3)  The receiver's symbol is not already taken by another receiver in
              the circuit. 
             
        If at any point a check is not passed, an error message is printed stating
        the cause of the error and returns False, skipping any further checks. If 
        all checks pass, then the following needs to occur:
          1)  receiver is added in the circuit's list of receivers. receiver
              needs to be added such that the list of receivers  remains sorted
              in alphabetical order by the receiver's symbol. You can assume the
              list of receivers is already sorted before you add the receiver. 
          2)  receiver's symbol is added into board_displayer.
          3)  The method returns True.

        Paramaters
        ----------
        receiver - the receiver to add into this circuit's list of receivers

        Returns
        ----------
        Returns true if all checks are passed and the receiver is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter and get_collided_receiver methods to
        check for position collisions.
        You will need to find your own way to check for symbol collisions
        with other receivers.
        '''
        if not isinstance(receiver, Receiver):
            return False
        if receiver.get_x() < 0 or receiver.get_x() >= self.width or receiver.get_y() < 0 or receiver.get_y() >= self.height:
            print(
                f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is out-of-bounds of "
                f"{self.get_width()}x{self.get_height()} circuit board")
            return False
        collided_emitter = self.get_collided_emitter(receiver)
        if collided_emitter is not None:
            print(
                f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by emitter '{collided_emitter.get_symbol()}'")
            return False
        collided_receiver = self.get_collided_receiver(receiver)
        if collided_receiver is not None:
            print(
                f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by receiver '{collided_receiver.symbol}'")
            return False
        index = 0
        while index < len(self.receivers):
            if receiver.get_symbol() == self.receivers[index].get_symbol():
                print(f"Error: symbol '{receiver.symbol}' is already taken")
                return False
            index += 1
        self.receivers.append(receiver)
        self.board_displayer.add_component_to_board(receiver)
        return True

    def get_receivers(self) -> list[Receiver]:
        '''Returns receivers.'''
        self.receivers = sorter.sort_receivers_by_symbol(self.receivers)
        return self.receivers

    def add_photon(self, photon: Photon) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        If the photon passed in is not a Photon instance, it does not add it in
        and returns False. Else, it adds photon in this circuit's list of
        photons and returns True.

        Paramaters
        ----------
        photon - the photon to add into this circuit's list of photons

        Returns
        -------
        Returns True if the photon is added in, else False.
        '''
        if not isinstance(photon, Photon):
            return False
        self.photons.append(photon)
        self.board_displayer.add_photon_to_board(photon)
        return True

    def get_photons(self) -> list[Photon]:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns photons.'''
        return self.photons

    def add_mirror(self, mirror: Mirror) -> bool:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        If mirror is not a Mirror instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The mirror's position is within the bounds of the circuit.
          2)  The mirror's position is not already taken by another emitter, 
              receiver or mirror in the circuit.
             
        If at any point a check is not passed, an error message is printed
        stating the cause of theerror and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur: 
          1)  mirror is added in the circuit's list of mirrors.
          2) mirror's symbol is added into board_displayer.
          3)   The method returns True.

        Paramaters
        ----------
        mirror - the mirror to add into this circuit's list of mirrors

        Returns
        ----------
        Returns true if all checks are passed and the mirror is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.
        '''
        if not isinstance(mirror, Mirror):
            return False
        if mirror.get_x() < 0 or mirror.get_x() >= self.width or mirror.get_y() < 0 or mirror.get_y() >= self.height:
            print(
                f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is out-of-bounds of "
                f"{self.get_width()}x{self.get_height()} circuit board")
            return False
        else:
            collided_emitter = self.get_collided_emitter(mirror)
            if collided_emitter is not None:
                print(
                    f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by {collided_emitter.get_component_type()} '{collided_emitter.get_symbol()}'")
                return False
            collided_receiver = self.get_collided_receiver(mirror)
            if collided_receiver is not None:
                print(
                    f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by {collided_receiver.get_component_type()} '{collided_receiver.get_symbol()}'")
                return False
            collided_mirror = self.get_collided_mirror(mirror)
            if collided_mirror is not None:
                print(
                    f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by {collided_mirror.get_component_type()} '{collided_mirror.get_symbol()}'")
                return False
            self.mirrors.append(mirror)
            self.board_displayer.add_component_to_board(mirror)
            return True

    def get_mirrors(self) -> list[Mirror]:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns mirrors.'''
        return self.mirrors

    def get_width(self) -> int:
        '''Returns width.'''
        return self.width

    def get_height(self) -> int:
        '''Returns height.'''
        return self.height
