from generate_challenge import generate_challenge
from notify import play_challenge

import random

class GameState:
    def __init__(self):
        self.current_position = 0
        self.target_sequence = []
        self.note_options = ['C4', 'D4']

        self.notes_difficulty_tiers: list[list[str]] = [
            ['A3', 'B3', 'E4'], # 1, M2, P5
            ['Bb3'], # m2
            ['C4'], # m3
            ['Db4'], # M3
            ['D4'], # P4
            ['Eb4'], # TT
            ['F4'], # m6
            ['Gb4'], # M6
            ['G4'], # m7
            ['Ab4'], # M7
        ]

    def new_challenge(self):
        # Randomize sequence length from 2 to 4
        sequence_length = random.randint(2, 4)

        # Generate a new sequence of notes to guess
        self.target_sequence = generate_challenge(sequence_length, self.note_options)
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
        pass

    def failure(self):
        pass