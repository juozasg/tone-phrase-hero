from music import note_val
import threading
import time
from midi_play import note_on, note_off

def notify_correct_note(note_name):
    print(f"Correct! That was {note_name}")

def notify_sequence_success():
    print("\n🎉 CONGRATULATIONS! You played the entire sequence correctly! 🎉")
    
    # Play success sound in a separate thread
    sound_thread = threading.Thread(target=play_success_sound)
    sound_thread.daemon = True
    sound_thread.start()


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

def play_success_sound():
    """
    Play a success sound as an arpeggio: C2 G2 C3 G3
    """
    success_notes = ['C2', 'G2', 'C3', 'G3']
    velocity = 80  # Slightly louder for celebration
    
    # Play each note in sequence with a slight delay
    for note_name in success_notes:
        note = note_val(note_name)
        note_on(note, velocity)
        time.sleep(0.15)  # Short delay between notes for arpeggio effect
    
    # Hold the final chord briefly
    time.sleep(0.5)
    
    # Turn off all notes in reverse order for a nice effect
    for note_name in reversed(success_notes):
        note = note_val(note_name)
        note_off(note, velocity)
        time.sleep(0.1)
