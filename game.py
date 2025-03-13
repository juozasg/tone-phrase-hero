from midi_utils import play_note
import threading

def game_loop(input_port, output_port):
    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C to exit")

    try:
        # Set up callback for incoming MIDI messages
        for message in input_port:
            if message.type == 'note_on':
                # When a note is pressed, play it on the output port
                if message.velocity > 0:
                    print(f"Received note: {message.note}, velocity: {message.velocity}")
                    # Start a new thread to play the note asynchronously
                    note_thread = threading.Thread(
                        target=play_note,
                        args=(output_port, message.note, message.velocity, 0.5)
                    )
                    note_thread.daemon = True  # Thread will exit when main program exits
                    note_thread.start()
    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
