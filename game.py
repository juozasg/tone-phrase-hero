from midi_utils import play_note

def game_loop(input_port, output_port):
    if not input_port or not output_port:
        print("Cannot run game loop: Missing input or output port")
        return
        
    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C to exit")
    
    try:
        # Set up callback for incoming MIDI messages
        for message in input_port:
            if message.type == 'note_on':
                # When a note is pressed, play it on the output port
                if message.velocity > 0:
                    print(f"Received note: {message.note}, velocity: {message.velocity}")
                    play_note(output_port, note=message.note, velocity=message.velocity, duration=0.5)
    except KeyboardInterrupt:
        print("\nGame loop stopped by user")
