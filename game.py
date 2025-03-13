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
            return message.note
    elif message.type == 'note_off':
        # When a note is released, send note off
        print(f"Received note off: {message.note}")
        note_thread = threading.Thread(target=lambda: note_off(output_port, message.note, message.velocity))
        note_thread.daemon = True
        note_thread.start()

    return False

def game_loop(input_port, output_port):
    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C to exit")

    note_options = ['C4', 'D4']

    try:
        # Set up callback for incoming MIDI messages
        while True:
            # Choose a random note to play
            target_note_name = random.choice(note_options)
            target_note = note_val(target_note_name)

            print(f"\nGuess this note:")
            # Play the note for the user to guess
            play_note(output_port, target_note, 64, 1.0)

            # Wait for user input
            for message in input_port:
                played_note = handle_midi_message(message, output_port)
                if played_note:
                    if played_note == target_note:
                        print("\n!!!CORRECT! You guessed the right note.")
                    else:
                        print(f"\n!!!!INCORRECT. The note was {target_note_name}.")

                    # Break out of the inner loop to play a new note
                    break
    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
