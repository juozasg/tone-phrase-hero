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


def create_virtual_midi_device(port_name):
    """
    Creates a virtual MIDI output port using rtmidi.

    Args:
        port_name (str): The name to give to the virtual MIDI port

    Returns:
        rtmidi.MidiOut: The created virtual MIDI output port object
    """
    try:
        # midi_out = rtmidi.MidiOut()
        rtmidi.MidiOut().open_virtual_port("virt midi out")
        rtmidi.MidiIn().open_virtual_port("virt midi in")
        # print(f"Created virtual MIDI output port: {port_name}")
        # return midi_out
    except Exception as e:
        print(f"Error creating virtual MIDI port: {e}")
        return None


# if __name__ == "__main__":
    #

create_virtual_midi_device("tone-phrase-hero")

list_midi_ports()

# Keep the program running for 30 seconds to maintain the virtual MIDI ports
print("Keeping virtual MIDI ports open for 30 seconds...")
time.sleep(30)
print("Done.")
