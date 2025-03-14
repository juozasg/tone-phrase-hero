from game.game_state import GameState
from game.midi.note_play import midi_through_capture_off
from game.midi.ports import get_input_port
from game.music import note_val
from game.notify import notify_correct_note, notify_sequence_success, notify_failure
import time

def print_note_prompt(game_state: GameState):
    # Create a visual representation of the sequence progress
    sequence_length = len(game_state.target_sequence)
    progress = []

    # Add completed notes in green
    for i in range(game_state.current_position):
        progress.append(f"\033[92m{game_state.target_sequence[i]}\033[0m")

    # Add current note indicator
    if game_state.current_position < sequence_length:
        progress.append("?")

    # Add greyed out question marks for remaining notes
    for i in range(game_state.current_position + 1, sequence_length):
        progress.append("\033[90m?\033[0m")  # Grey color in terminal

    # Print the progress on a single line
    print(' '.join(progress))


def game_loop():
    game_state = GameState()
    input_port = get_input_port()

    print("Game loop started. Press keys on your MIDI device...")
    print("Press Ctrl+C or E1 to exit")
    print("C1 to restart the sequence")

    try:
        game_state.new_challenge()
        print_note_prompt(game_state)

        # Wait for user input
        for message in input_port:
            played_note = midi_through_capture_off(message)
            if type(played_note) is int:
                # Exit game if E1 was played
                if played_note == note_val('E1'):
                    print("\nExiting!")
                    time.sleep(0.5 )
                    return

                # If C1 was played, reset position but keep the same sequence
                if played_note == note_val('C1'):
                    print("\nRestarting the same sequence...")
                    time.sleep(0.5)
                    game_state.replay_challenge()

                    print_note_prompt(game_state)
                    continue

                # Check if the played note matches the current position in the sequence
                if played_note == note_val(game_state.current_target_note()):
                    notify_correct_note(game_state)
                    game_state.current_position += 1

                    # SEQUENCE SUCCESS
                    if game_state.current_position == len(game_state.target_sequence):
                        time.sleep(0.4)
                        notify_sequence_success()
                        time.sleep(2)
                        game_state.success()
                        game_state.new_challenge()
                # SEQUENCE FAILURE
                else:
                    time.sleep(0.4)
                    notify_failure(game_state)
                    time.sleep(1)
                    game_state.failure()
                    game_state.new_challenge()

                print_note_prompt(game_state)

    except KeyboardInterrupt:
        print("\nExiting!")
        time.sleep(0.3)
