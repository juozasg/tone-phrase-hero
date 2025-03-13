from midi_utils import note_on, note_off, play_note
from music import note_val
import threading
import time
import random

def handle_midi_message(message, output_port):
    if message.type == 'note_on':
        # When a note is pressed, play it on the output port
        if message.velocity > 0:
            print(f"Received note: {message.note}, velocity: {message.velocity}")
            # Start a new thread to play the note asynchronously
            note_thread = threading.Thread(target=lambda: note_on(output_port, message.note, message.velocity))
            note_thread.daemon = True  # Thread will exit when main program exits
            note_thread.start()
            return {'type': 'note_on', 'note': message.note}
    elif message.type == 'note_off':
        # When a note is released, send note off
        print(f"Received note off: {message.note}")
        note_thread = threading.Thread(target=lambda: note_off(output_port, message.note, message.velocity))
        note_thread.daemon = True
        note_thread.start()
        return {'type': 'note_off', 'note': message.note}

    return False

def game_loop(input_port, output_port):
    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C to exit")

    note_options = ['C4', 'D4']
    waiting_for_note_off = False
    last_played_note = None

    # For the sequence challenge
    sequence_length = 2
    current_position = 0

    try:
        # Set up callback for incoming MIDI messages
        while True:
            if not waiting_for_note_off and current_position == 0:
                # Generate a new sequence of notes to guess
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
                    play_note(output_port, target_note, 64, 0.7)
                    time.sleep(0.5)  # Brief pause between notes

                print("\nNow play back the sequence in order.")
                print(f"Note 1 of {sequence_length}:")

            # Wait for user input
            for message in input_port:
                result = handle_midi_message(message, output_port)
                if result:
                    if result['type'] == 'note_on':
                        played_note = result['note']
                        last_played_note = played_note

                        # Check if the played note matches the current position in the sequence
                        if played_note == target_sequence[current_position]:
                            print(f"Correct! That was {target_sequence_names[current_position]}")
                            current_position += 1

                            if current_position == sequence_length:
                                print("\n🎉 CONGRATULATIONS! You played the entire sequence correctly! 🎉")
                                current_position = 0  # Reset for a new sequence
                            else:
                                print(f"Note {current_position + 1} of {sequence_length}:")
                        else:
                            print(f"\n❌ INCORRECT. That should have been {target_sequence_names[current_position]}.")
                            print("Let's try a new sequence.")
                            current_position = 0  # Reset for a new sequence

                        waiting_for_note_off = True

                    elif result['type'] == 'note_off' and waiting_for_note_off and result['note'] == last_played_note:
                        waiting_for_note_off = False
                        last_played_note = None

                        # If we need to start a new sequence, break out of the inner loop
                        if current_position == 0:
                            time.sleep(1)  # Wait for 1 second before starting a new sequence
                            break

    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
