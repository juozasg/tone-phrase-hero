from midi_play import note_on, note_off, play_note
from midi_ports import get_input_port, get_output_port
from music import note_val
from notify import notify_correct_note, notify_sequence_success, notify_failure
import threading
import time
import random

def handle_midi_message(message):
    output_port = get_output_port()
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

def generate_challenge(sequence_length, note_options):
    """
    Generate a new sequence challenge and play it for the user.

    Args:
        sequence_length (int): The number of notes in the sequence
        note_options (list): List of possible note names to choose from

    Returns:
        tuple: (target_sequence, target_sequence_names) - Lists of note values and names
    """
    target_sequence = []
    target_sequence_names = []

    print("\n=== NEW CHALLENGE ===")
    print(f'Listen to this sequence of {sequence_length} notes:')

    # Generate and play the sequence
    for i in range(sequence_length):
        # Choose a random note
        target_note_name = random.choice(note_options)
        target_note = note_val(target_note_name)

        target_sequence.append(target_note)
        target_sequence_names.append(target_note_name)

        # Play the note
        play_note(target_note, 64, 0.7)
        time.sleep(0.5)  # Brief pause between notes

    print("\nNow play back the sequence in order.")
    print(f"Note 1 of {sequence_length}:")

    return target_sequence, target_sequence_names


# For the sequence challenge
sequence_length = 3
current_position = 0
target_sequence = []
target_sequence_names = []
note_options = ['C4', 'D4']


def reset():
    global target_sequence
    global target_sequence_names
    global current_position
    global sequence_length

    # Randomize sequence length from 2 to 4
    sequence_length = random.randint(2, 4)

    # Generate a new sequence of notes to guess
    target_sequence, target_sequence_names = generate_challenge(sequence_length, note_options)
    current_position = 0


def reset_position():
    global current_position
    current_position = 0
    
    # Replay the sequence to remind the player
    print("\n=== REPLAYING SEQUENCE ===")
    print(f'Listen to this sequence of {sequence_length} notes again:')
    
    for i in range(sequence_length):
        play_note(target_sequence[i], 64, 0.7)
        time.sleep(0.5)
        
    print("\nNow play back the sequence in order.")
    print(f"Note 1 of {sequence_length}:")


def game_loop():
    global target_sequence
    global target_sequence_names
    global current_position

    input_port = get_input_port()

    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C or E1 to exit")
    print("C1 to restart the sequence")

    try:
        reset()
        # Wait for user input
        for message in input_port:
            result = handle_midi_message(message)
            if result:
                if result['type'] == 'note_off':
                    played_note = result['note']

                    # Exit game if E1 was played
                    if played_note == note_val('E1'):
                        print("\nExiting!")
                        return

                    # If C1 was played, reset position but keep the same sequence
                    if played_note == note_val('C1'):
                        print("\nRestarting the same sequence...")
                        time.sleep(0.5)
                        reset_position()
                        continue

                    # Check if the played note matches the current position in the sequence
                    if played_note == target_sequence[current_position]:
                        notify_correct_note(target_sequence_names[current_position])
                        current_position += 1

                        if current_position == sequence_length:
                            time.sleep(0.4)
                            notify_sequence_success()
                            time.sleep(2)
                            reset()

                        else:
                            print(f"Note {current_position + 1} of {sequence_length}:")
                    else:
                        time.sleep(0.4)
                        notify_failure(target_sequence_names[current_position])
                        time.sleep(1)
                        reset()



    except KeyboardInterrupt:
        print("\nExiting!")
