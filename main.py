from midi_utils import open_midi_input_port, open_midi_output_port
from game import game_loop

# Global variables to store the current ports
_current_output_port = None
_current_input_port = None

def get_output_port():
    return _current_output_port

def get_input_port():
    return _current_input_port

if __name__ == "__main__":
    # list_midi_ports()

    # Open the specified MIDI output port
    out_port_name = 'Virtual Raw MIDI 6-0:VirMIDI 6-0 40:0'
    output_port = open_midi_output_port(out_port_name)

    # Store the output port in the global variable
    _current_output_port = output_port

    # Open the specified MIDI input port
    in_port_name = 'KeyLab mkII 61:KeyLab mkII 61 MIDI 32:0'
    input_port = open_midi_input_port(in_port_name)

    # Store the input port in the global variable
    _current_input_port = input_port

    # Run the game loop with the opened ports
    game_loop(input_port, output_port)

    if output_port:
        # Close the port
        output_port.close()
        print("MIDI output port closed")

    if input_port:
        # Close the input port
        input_port.close()
        print("MIDI input port closed")
