import mido

def open_midi_output_port(port_name):
    try:
        output_port = mido.open_output(port_name)
        print(f"Successfully opened MIDI output port: {port_name}")
        return output_port
    except Exception as e:
        print(f"Error opening MIDI output port: {e}")
        return None


def open_midi_input_port(port_name):
    try:
        input_port = mido.open_input(port_name)
        print(f"Successfully opened MIDI input port: {port_name}")
        return input_port
    except Exception as e:
        print(f"Error opening MIDI input port: {e}")
        return None
