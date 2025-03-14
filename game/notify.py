from game.music import note_val
import threading
import time
from game.midi.note_play import note_on, note_off, play_note

def notify_correct_note(game_state):
    note_name = game_state.current_target_note()
    print(f"✅ {note_name}")

def notify_sequence_success():
    # print("\n🎉 CONGRATULATIONS! 🎉")
    print("\n🎉 🎉 🎉")

    # Play success sound in a separate thread
    sound_thread = threading.Thread(target=play_success_sound)
    sound_thread.daemon = True
    sound_thread.start()


def notify_failure(game_state):
    correct_note_name = game_state.current_target_note()
    print(f"\n❌ INCORRECT. That should have been {correct_note_name}.")

    correct_seq = game_state.target_sequence[:game_state.current_position]

    play_note_list(correct_seq)

    play_note(note_val(correct_note_name), 64, 1.5)
    time.sleep(0.4)


    # Play the failure sound in a separate thread to not block the game
    # sound_thread = threading.Thread(target=play_failure_sound)
    # sound_thread.daemon = True
    # sound_thread.start()

    play_failure_sound(1)
    time.sleep(0.4)
    play_failure_sound(0)
    time.sleep(0.5)

    # print("Let's try a new sequence.")

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
    success_notes = ['C2', 'G2', 'C3']
    velocity = 50  # Slightly louder for celebration

    # Play each note in sequence with a slight delay
    for note_name in success_notes:
        velocity += 15
        note = note_val(note_name)
        note_on(note, velocity)
        time.sleep(0.08)  # Short delay between notes for arpeggio effect
        note_off(note, velocity)
        time.sleep(0.03)

    # # Hold the final chord briefly
    # time.sleep(0.25)

    # # Turn off all notes in reverse order for a nice effect
    # for note_name in reversed(success_notes):
    #     note = note_val(note_name)

    #     time.sleep(0.1)

def play_note_list(sequence: list[str]):
    length = len(sequence)
    for i in range(length):
        play_note(note_val(sequence[i]), 64, 0.7)
        time.sleep(0.5)

    # print("\nNow play back the sequence in order.")
    # print(f"Note 1 of {length}:")
