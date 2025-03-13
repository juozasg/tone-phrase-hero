from music import note_val
import threading
import time
from midi_play import note_on, note_off

def notify_correct_note(note_name):
    print(f"Correct! That was {note_name}")

def notify_sequence_success():
    print("\n🎉 CONGRATULATIONS! You played the entire sequence correctly! 🎉")


def notify_failure(correct_note_name):
    print(f"\n❌ INCORRECT. That should have been {correct_note_name}.")

    # Play the failure sound in a separate thread to not block the game
    # sound_thread = threading.Thread(target=play_failure_sound)
    # sound_thread.daemon = True
    # sound_thread.start()

    play_failure_sound(1)
    time.sleep(0.4)
    play_failure_sound(0)
    time.sleep(0.5)

    print("Let's try a new sequence.")

def play_failure_sound(transpose = 0):
    # failure_notes = ['C2', 'D2', 'E2', 'F2', 'G2']
    failure_notes = ['C2', 'G2']
    for note_name in failure_notes:
        note = note_val(note_name) + transpose
        note_on(note, 64)
        # time.sleep(0.05)  # Stagger by 50ms

    # Wait a bit before turning off all notes
    time.sleep(0.4)

    # Turn off all notes
    for note_name in failure_notes:
        note = note_val(note_name) + transpose
        note_off(note, 64)

# add play_success_sound that plays an arpegio C2 G2 C3 G3 AI!