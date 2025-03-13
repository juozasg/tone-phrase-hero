from midi_utils import note_on, note_off
import threading
import time

def game_loop(input_port, output_port):
    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C to exit")

    try:
        # Set up callback for incoming MIDI messages
        for message in input_port:
            # move this inner loop to separate function AI!
            if message.type == 'note_on':
                # When a note is pressed, play it on the output port
                if message.velocity > 0:
                    print(f"Received note: {message.note}, velocity: {message.velocity}")
                    # Start a new thread to play the note asynchronously
                    note_thread = threading.Thread(target=lambda: note_on(output_port, message.note, message.velocity))
                    note_thread.daemon = True  # Thread will exit when main program exits
                    note_thread.start()
            elif message.type == 'note_off':
                # When a note is released, send note off
                print(f"Received note off: {message.note}")
                note_thread = threading.Thread(target=lambda: note_off(output_port, message.note, message.velocity))
                note_thread.daemon = True
                note_thread.start()
    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
