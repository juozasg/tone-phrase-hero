from midi_utils import note_on, note_off
import threading
import time

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
                    def play_async_note():
                        note_on(output_port, message.note, message.velocity)
                        time.sleep(0.5)  # Duration
                        note_off(output_port, message.note, message.velocity)
                    
                    note_thread = threading.Thread(target=play_async_note)
                    note_thread.daemon = True  # Thread will exit when main program exits
                    note_thread.start()
    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
