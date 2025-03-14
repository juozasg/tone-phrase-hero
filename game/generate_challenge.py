import random
from enum import Enum

class MelodyShape(Enum):
    UP = 1
    DOWN = 2
    UPDOWN = 3
    RANDOM = 4

def generate_challenge(sequence_length: int, note_options: list[str], shape: MelodyShape = MelodyShape.UP, leapiness: float = 0.2) -> list[str]:
    target_sequence: list[str] = []

    # Always start with the first note from note_options
    if note_options and sequence_length > 0:
        target_sequence.append(note_options[0])
    
    # Generate the rest of the sequence
    for i in range(1, sequence_length):
        # Choose a random note
        target_note = random.choice(note_options)
        target_sequence.append(target_note)

    return target_sequence
