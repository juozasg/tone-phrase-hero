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


if __name__ == "__main__":
    list_midi_ports()
    
    # Open the specified MIDI output port
    try:
        port_name = 'Virtual Raw MIDI 6-0:VirMIDI 6-0 40:0'
        output_port = mido.open_output(port_name)
        print(f"Successfully opened MIDI output port: {port_name}")
        
        # Play C4 note (MIDI note number 60)
        note_on = mido.Message('note_on', note=60, velocity=64)
        output_port.send(note_on)
        print("Playing C4 note...")
        
        # Hold for 1 second
        time.sleep(1)
        
        # Release the note
        note_off = mido.Message('note_off', note=60, velocity=64)
        output_port.send(note_off)
        print("Note released")
        
        # Close the port
        output_port.close()
        print("MIDI port closed")
    except Exception as e:
        print(f"Error: {e}")
