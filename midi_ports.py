import mido

def open_midi_output_port(port_name):
    try:
        output_port = mido.open_output(port_name)
        print(f"Opened MIDI output port: {port_name}")
        return output_port
    except Exception as e:
        print(f"Error opening MIDI output port: {e}")
        return None


def open_midi_input_port(port_name):
    try:
        input_port = mido.open_input(port_name)
        print(f"Opened MIDI input port: {port_name}")
        return input_port
    except Exception as e:
        print(f"Error opening MIDI input port: {e}")
        return None


def list_midi_ports():
    input_ports = mido.get_input_names()
    output_ports = mido.get_output_names()

    print("Available MIDI Input Ports:")
    if input_ports:
        for i, port in enumerate(input_ports):
            print(f"  {i}: {port}")
    else:
        print("  None found")

    print("\nAvailable MIDI Output Ports:")
    if output_ports:
        for i, port in enumerate(output_ports):
            print(f"  {i}: {port}")
    else:
        print("  None found")

    return input_ports, output_ports

