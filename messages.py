def notify_correct_note(note_name):
    print(f"Correct! That was {note_name}")

def notify_sequence_success():
    print("\n🎉 CONGRATULATIONS! You played the entire sequence correctly! 🎉")


def notify_failure(correct_note_name):
    print(f"\n❌ INCORRECT. That should have been {correct_note_name}.")
    # play notes C2, D2, E2, F2 and G2 together but staggered by 100ms to signal failure AI!
    print("Let's try a new sequence.")
