import mido
import time

from midi_ports import get_output_port


def note_on(note=60, velocity=64):
    output_port = get_output_port()
    if output_port is None:
        print("Cannot play note: No valid MIDI output port provided")
        return

    try:
        # Send note on message
        note_on_msg = mido.Message('note_on', note=note, velocity=velocity)
        output_port.send(note_on_msg)
        print(f"ON {note} ({velocity})")
    except Exception as e:
        print(f"Error sending note_on: {e}")


def note_off(note=60, velocity=64):
    output_port = get_output_port()
    if output_port is None:
        print("Cannot release note: No valid MIDI output port provided")
        return

    try:
        # Send note off message
        note_off_msg = mido.Message('note_off', note=note, velocity=velocity)
        output_port.send(note_off_msg)
        print(f"OFF {note} ({velocity})")
    except Exception as e:
        print(f"Error sending note_off: {e}")


def play_note(note=60, velocity=64, duration=1.0):
    output_port = get_output_port()
    if output_port is None:
        print("Cannot play note: No valid MIDI output port provided")
        return

    try:
        note_on(note, velocity)

        # Hold for the specified duration
        time.sleep(duration)

        note_off(note, velocity)
    except Exception as e:
        print(f"Error playing note: {e}")

