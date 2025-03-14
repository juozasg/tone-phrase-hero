from midi_play import note_on, note_off, play_note
from midi_ports import get_input_port, get_output_port
from music import note_val
from notify import notify_correct_note, notify_sequence_success, notify_failure, play_challenge
import threading
import time
import random

def handle_midi_message(message):
    if message.type == 'note_on':
        # When a note is pressed, play it on the output port
        if message.velocity > 0:
            print(f"Received note: {message.note}, velocity: {message.velocity}")
            # Start a new thread to play the note asynchronously
            note_thread = threading.Thread(target=lambda: note_on(message.note, message.velocity))
            note_thread.daemon = True  # Thread will exit when main program exits
            note_thread.start()
            return {'type': 'note_on', 'note': message.note}
    elif message.type == 'note_off':
        # When a note is released, send note off
        print(f"Received note off: {message.note}")
        note_thread = threading.Thread(target=lambda: note_off(message.note, message.velocity))
        note_thread.daemon = True
        note_thread.start()
        return {'type': 'note_off', 'note': message.note}

    return False


# For the sequence challenge
current_position = 0
target_sequence: list[str] = []
note_options = ['C4', 'D4']



def generate_challenge(sequence_length: int, note_options: list[str]) -> list[str]:
    target_sequence: list[str] = []

    # Generate and play the sequence
    for i in range(sequence_length):
        # Choose a random note
        target_note = random.choice(note_options)
        target_sequence.append(target_note)

    return target_sequence

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
            result = handle_midi_message(message)
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
