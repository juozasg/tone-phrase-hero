import mido
import rtmidi
import time

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


def open_midi_output_port(port_name):
    try:
        output_port = mido.open_output(port_name)
        print(f"Successfully opened MIDI output port: {port_name}")
        return output_port
    except Exception as e:
        print(f"Error opening MIDI output port: {e}")
        return None


def play_note(output_port, note=60, velocity=64, duration=1.0):
    if output_port is None:
        print("Cannot play note: No valid MIDI output port provided")
        return

    try:
        # Send note on message
        note_on = mido.Message('note_on', note=note, velocity=velocity)
        output_port.send(note_on)
        print(f"Playing note {note} with velocity {velocity}...")

        # Hold for the specified duration
        time.sleep(duration)

        # Send note off message
        note_off = mido.Message('note_off', note=note, velocity=velocity)
        output_port.send(note_off)
        print("Note released")
    except Exception as e:
        print(f"Error playing note: {e}")


def open_midi_input_port(port_name):
    """
    Opens a MIDI input port with the specified name.
    
    Args:
        port_name (str): The name of the MIDI input port to open
        
    Returns:
        mido.ports.BaseInput: The opened MIDI input port or None if an error occurred
    """
    try:
        input_port = mido.open_input(port_name)
        print(f"Successfully opened MIDI input port: {port_name}")
        return input_port
    except Exception as e:
        print(f"Error opening MIDI input port: {e}")
        return None


if __name__ == "__main__":
    # list_midi_ports()

    # Open the specified MIDI output port
    out_port_name = 'Virtual Raw MIDI 6-0:VirMIDI 6-0 40:0'
    output_port = open_midi_output_port(out_port_name)

    # Open the specified MIDI input port
    in_port_name = 'KeyLab mkII 61:KeyLab mkII 61 MIDI 32:0'
    input_port = open_midi_input_port(in_port_name)

    if output_port:
        # Play C4 note for 1 second
        play_note(output_port, note=60, velocity=64, duration=1.0)

        # Close the port
        output_port.close()
        print("MIDI output port closed")
    
    if input_port:
        # Close the input port
        input_port.close()
        print("MIDI input port closed")
