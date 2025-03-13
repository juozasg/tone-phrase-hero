from midi_utils import play_note

def game_loop(input_port, output_port):
    if input_port and output_port:
        # Play C4 note for 1 second
        play_note(output_port, note=60, velocity=64, duration=1.0)
