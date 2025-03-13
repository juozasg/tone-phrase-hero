def notify_correct_note(note_name):
    print(f"Correct! That was {note_name}")

def notify_sequence_success():
    print("\n🎉 CONGRATULATIONS! You played the entire sequence correctly! 🎉")


def notify_failure(correct_note_name):
    print(f"\n❌ INCORRECT. That should have been {correct_note_name}.")
    # Import here to avoid circular imports
    from midi_utils import note_on, note_off
    from music import note_val
    import threading
    import time
    
    def play_failure_sound(output_port):
        failure_notes = ['C2', 'D2', 'E2', 'F2', 'G2']
        for note_name in failure_notes:
            note = note_val(note_name)
            note_on(output_port, note, 64)
            time.sleep(0.1)  # Stagger by 100ms
        
        # Wait a bit before turning off all notes
        time.sleep(0.5)
        
        # Turn off all notes
        for note_name in failure_notes:
            note = note_val(note_name)
            note_off(output_port, note, 64)
    
    # We need to get the output port from the main module
    from main import get_current_output_port
    output_port = get_current_output_port()
    
    if output_port:
        # Play the failure sound in a separate thread to not block the game
        sound_thread = threading.Thread(target=lambda: play_failure_sound(output_port))
        sound_thread.daemon = True
        sound_thread.start()
    
    print("Let's try a new sequence.")
