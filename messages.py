def show_success_message(note_name):
    print(f"Correct! That was {note_name}")

def show_sequence_complete_message():
    print("\n🎉 CONGRATULATIONS! You played the entire sequence correctly! 🎉")

def show_failure_message(correct_note_name):
    print(f"\n❌ INCORRECT. That should have been {correct_note_name}.")
    print("Let's try a new sequence.")
