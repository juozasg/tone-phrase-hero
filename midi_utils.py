import mido
import time

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
