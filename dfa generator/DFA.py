import graphviz


class DFA:

    def __init__(self, states, alphabet, transition_function, start_state,
                 accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def is_accepted(self, string):
        current_state = self.start_state
        for c in string:
            current_state = self.transition_function[current_state][c]
        return current_state in self.accept_states

    @staticmethod
    def integers(text):
        states = {0, 1, 2}
        alphabet = {str(i) for i in range(10)}
        transition_function = {
            0: {str(i): 1
                for i in range(1, 10)},
            1: {str(i): 1
                for i in range(10)},
            1: {str(i): 2
                for i in range(10)},
        }
        start_state = 0
        accept_states = {1}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)

    @staticmethod
    def real(text):
        states = {0, 1, 2, 3, 4, 5}
        alphabet = {str(i) for i in range(10)}
        transition_function = {
            0: {str(i): 1
                for i in range(1, 10)},
            1: {str(i): 1
                for i in range(10)},
            1: {
                '.': 2
            },
            2: {str(i): 3
                for i in range(10)},
            3: {str(i): 3
                for i in range(10)},
            3: {
                'e': 4
            },
            4: {
                '+': 5,
                '-': 5
            },
            5: {str(i): 6
                for i in range(10)},
            6: {str(i): 6
                for i in range(10)},
        }
        start_state = 0
        accept_states = {1, 3, 6}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)

    @staticmethod
    def name(text):
        states = {0, 1, 2, 3}
        alphabet = {chr(i)
                    for i in range(65, 91)} | {chr(i)
                                               for i in range(97, 123)
                                               } | {'_'}
        transition_function = {
            0: {chr(i): 1
                for i in range(65, 91)} | {chr(i)
                                           for i in range(97, 123)}
            | {'_'},  # type: ignore
            1: {chr(i): 1
                for i in range(65, 91)} | {chr(i)
                                           for i in range(97, 123)} | {'_'}
            | {str(i)
               for i in range(10)},  # type: ignore
            1: {str(i): 2
                for i in range(10)},
            2: {str(i): 2
                for i in range(10)},
        }
        start_state = 0
        accept_states = {1, 2}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)

    @staticmethod
    def char(text):
        states = {0, 1, 2, 3}
        alphabet = {chr(i) for i in range(32, 127)} - {'\'', '\\'}
        transition_function = {
            0: {
                '\'': 1
            },
            1: {chr(i): 2
                for i in range(32, 127)} - {'\'', '\\'},  # type: ignore
            2: {
                '\'': 3
            },
        }
        start_state = 0
        accept_states = {3}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)

    @staticmethod
    def string(text):
        states = {0, 1, 2, 3, 4}
        alphabet = {chr(i) for i in range(32, 127)} - {'\"', '\\'}
        transition_function = {
            0: {
                '\"': 1
            },
            1: {chr(i): 2
                for i in range(32, 127)} - {'\"', '\\'},  # type: ignore
            2: {
                '\"': 3
            },
            3: {
                '\"': 4
            },
        }
        start_state = 0
        accept_states = {3}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)

    @staticmethod
    def variable_name(text):
        states = {0, 1, 2, 3, 4}
        alphabet = {chr(i) for i in range(32, 127)} - {'\"', '\\'}
        transition_function = {
            0: {
                '\"': 1
            },
            1: {chr(i): 2
                for i in range(32, 127)} - {'\"', '\\'},  # type: ignore
            2: {
                '\"': 3
            },
            3: {
                '\"': 4
            },
        }
        start_state = 0
        accept_states = {3}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)

    @staticmethod
    def anonymous(text):
        states = {0, 1, 2, 3, 4}
        alphabet = {chr(i) for i in range(32, 127)} - {'\"', '\\'}
        transition_function = {
            0: {
                '\"': 1
            },
            1: {chr(i): 2
                for i in range(32, 127)} - {'\"', '\\'},  # type: ignore
            2: {
                '\"': 3
            },
            3: {
                '\"': 4
            },
        }
        start_state = 0
        accept_states = {3}
        return DFA(states, alphabet, transition_function, start_state,
                   accept_states)
