import mido
import time

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


def play_note(output_port, note=60, velocity=64, duration=1.0):
    if output_port is None:
        print("Cannot play note: No valid MIDI output port provided")
        return

    try:
        # Send note on message
        note_on = mido.Message('note_on', note=note, velocity=velocity)
        output_port.send(note_on)
        print(f"ON {note} ({velocity})")

        # Hold for the specified duration
        time.sleep(duration)

        # Send note off message
        note_off = mido.Message('note_off', note=note, velocity=velocity)
        output_port.send(note_off)
        print(f"OFF {note} ({velocity})")

    except Exception as e:
        print(f"Error playing note: {e}")


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