from midi_utils import note_on, note_off
from music import note_val
import threading
import time

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

    try:
        # Set up callback for incoming MIDI messages
        for message in input_port:
            played_note = handle_midi_message(message, output_port)
            if played_note:
                if played_note == note_val('C4'):
                    print("\nWIN")
                else:
                    print("\nLOSE")
    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
