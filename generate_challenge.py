import random


def generate_challenge(sequence_length: int, note_options: list[str]) -> list[str]:
    target_sequence: list[str] = []

    # Generate and play the sequence
    for i in range(sequence_length):
        # Choose a random note
        target_note = random.choice(note_options)
        target_sequence.append(target_note)

    return target_sequence