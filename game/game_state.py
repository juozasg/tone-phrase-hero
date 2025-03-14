from game.generate_challenge import MelodyShape, generate_challenge, make_note_options
from game.notify import play_challenge

import random
# from enum import Enum

class GameState:
    def __init__(self):
        self.current_position = 0
        self.target_sequence = []
        # self.note_options = ['C4', 'D4']

        self.note_difficulty: int = 0 # 0 to 9
        self.shape_difficulty: int = 0 # 0 to 3
        self.leapiness_difficulty: float = 0.1 # 0 to 1

        self.consecutive_successes = 0
        self.consecutive_failures = 0

        self.total_successes = 0
        self.total_failures = 0

        self.length_difficulty = 0


    def update_difficulty(self):
        # if more wins than loses, roll 25% to increase note_difficulty. with more consecutive wins, increase chance
        if(self.total_successes > self.total_failures ):
            if(random.random() < 0.25 + (self.consecutive_successes * 0.05)):
                self.note_difficulty = min(9, self.note_difficulty + 1)
        # if more loses than wins, roll 50% to decrease note_difficulty
        else:
            if(random.random() < 0.50):
                self.note_difficulty = max(0, self.note_difficulty - 1)
        print(f'note_difficulty: {self.note_difficulty}')

       # every 3 successes or any failures roll 25% to increase or decrease shape_difficulty
        if(self.consecutive_successes % 3 == 0 and random.random() > 0.75):
            self.shape_difficulty = min(3, self.shape_difficulty + 1)
        elif(self.consecutive_failures > 0 and random.random() > 0.75):
            self.shape_difficulty = max(0, self.shape_difficulty - 1)


        print(f'shape_difficulty: {self.shape_difficulty}')

        print("totals: ", self.total_successes, self.total_failures, "consequetive totals: ", self.consecutive_successes, self.consecutive_failures)


    def new_challenge(self):
        # Randomize sequence length from 2 to 4
        sequence_length = random.randint(1, self.length_difficulty + 1)

        note_options = make_note_options(self.note_difficulty)

        # Convert numeric shape_difficulty to MelodyShape enum
        shape = MelodyShape(self.shape_difficulty)
        leapiness = ((self.length_difficulty + self.note_difficulty)/10.0) * self.leapiness_difficulty

        self.target_sequence = [note_options[0]] + generate_challenge(sequence_length, note_options, shape, leapiness)
        self.current_position = 0

        print("\n=== NEW CHALLENGE ===")
        print(f'Listen to this sequence of {len(self.target_sequence)} notes:')
        play_challenge(self.target_sequence)

    def replay_challenge(self):
        self.current_position = 0

        # Replay the sequence to remind the player
        print("\n=== REPLAYING SEQUENCE ===")
        print(f'Listen to this sequence of {len(self.target_sequence)} notes again:')
        play_challenge(self.target_sequence)

    def current_target_note(self):
        """Return the note at the current position in the target sequence"""
        return self.target_sequence[self.current_position]

    def success(self):
        self.consecutive_successes += 1
        self.consecutive_failures = 0
        self.leapiness_difficulty = min(1, self.leapiness_difficulty + 0.15)
        if(random.random() < 0.30):
            self.length_difficulty += 1
            if(self.length_difficulty > 8):
                self.length_difficulty = 8

        print(f'leapiness_difficulty: {self.leapiness_difficulty}. length_difficulty: {self.length_difficulty}')
        self.total_successes += 1
        self.update_difficulty()


    def failure(self):
        self.consecutive_failures += 1
        self.consecutive_successes = 0
        self.leapiness_difficulty = max(0, self.leapiness_difficulty - 0.15)
        if(random.random() < 0.60):
            self.length_difficulty -= 1
            if(self.length_difficulty < 1):
                self.length_difficulty = 1
        print(f'leapiness_difficulty: {self.leapiness_difficulty}. length_difficulty: {self.length_difficulty}')
        self.total_failures += 1
        self.update_difficulty()