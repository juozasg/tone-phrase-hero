from generate_challenge import generate_challenge
from midi_play import midi_receive_and_play
from midi_ports import get_input_port
from music import note_val
from notify import notify_correct_note, notify_sequence_success, notify_failure, play_challenge
import time
import random

# For the sequence challenge
# refactor these globals into a class named GameState AI!
current_position = 0
target_sequence: list[str] = []
note_options = ['C4', 'D4']


def new_challenge():
    global target_sequence
    global current_position
    global note_options

    # Randomize sequence length from 2 to 4
    sequence_length = random.randint(2, 4)

    # Generate a new sequence of notes to guess
    target_sequence = generate_challenge(sequence_length, note_options)
    current_position = 0

    print("\n=== NEW CHALLENGE ===")
    print(f'Listen to this sequence of {len(target_sequence)} notes:')
    play_challenge(target_sequence)



def replay_challenge():
    global current_position
    global target_sequence

    current_position = 0

    # Replay the sequence to remind the player
    print("\n=== REPLAYING SEQUENCE ===")
    print(f'Listen to this sequence of {len(target_sequence)} notes again:')
    play_challenge(target_sequence)


def game_loop():
    global target_sequence
    global current_position

    input_port = get_input_port()

    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C or E1 to exit")
    print("C1 to restart the sequence")

    try:
        new_challenge()
        # Wait for user input
        for message in input_port:
            result = midi_receive_and_play(message)
            if result:
                if result['type'] == 'note_off':
                    played_note = result['note']
                    assert type(played_note) is int

                    # Exit game if E1 was played
                    if played_note == note_val('E1'):
                        print("\nExiting!")
                        return

                    # If C1 was played, reset position but keep the same sequence
                    if played_note == note_val('C1'):
                        print("\nRestarting the same sequence...")
                        time.sleep(0.5)
                        replay_challenge()
                        continue

                    # Check if the played note matches the current position in the sequence
                    if played_note == note_val(target_sequence[current_position]):
                        notify_correct_note(target_sequence[current_position])
                        current_position += 1

                        # SEQUENCE SUCCESS
                        if current_position == len(target_sequence):
                            time.sleep(0.4)
                            notify_sequence_success()
                            time.sleep(2)
                            new_challenge()

                        # Next note in the sequence
                        else:
                            print(f"Note {current_position + 1} of {len(target_sequence)}:")
                    # SEQUENCE FAILURE
                    else:
                        time.sleep(0.4)
                        notify_failure(target_sequence[current_position])
                        time.sleep(1)
                        new_challenge()



    except KeyboardInterrupt:
        print("\nExiting!")
