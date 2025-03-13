import mido

def list_midi_ports():
    """
    Lists all available MIDI input and output ports.

    Returns:
        tuple: Two lists containing (input_ports, output_ports)
    """
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

if __name__ == "__main__":
    list_midi_ports()
