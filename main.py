from midi_utils import open_midi_input_port, open_midi_output_port
from game import game_loop

# Global variable to store the current output port
_current_output_port = None

def get_current_output_port():
    return _current_output_port

if __name__ == "__main__":
    # list_midi_ports()

    # Open the specified MIDI output port
    out_port_name = 'Virtual Raw MIDI 6-0:VirMIDI 6-0 40:0'
    output_port = open_midi_output_port(out_port_name)
    
    # Store the output port in the global variable
    global _current_output_port
    _current_output_port = output_port

    # Open the specified MIDI input port
    in_port_name = 'KeyLab mkII 61:KeyLab mkII 61 MIDI 32:0'
    input_port = open_midi_input_port(in_port_name)

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
