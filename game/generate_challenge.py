import random
from enum import Enum

class MelodyShape(Enum):
    UP = 1
    DOWN = 2
    UPDOWN = 3
    RANDOM = 4

def generate_challenge(sequence_length: int, note_options: list[str], shape: MelodyShape = MelodyShape.UP, leapiness: float = 0.2) -> list[str]:
    target_sequence: list[str] = []

    # first note in sequence should always be first note from note_options AI!

    # Generate and play the sequence
    for i in range(sequence_length):
        # Choose a random note
        target_note = random.choice(note_options)
        target_sequence.append(target_note)

    return target_sequence