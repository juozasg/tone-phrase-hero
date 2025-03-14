from game.game_state import GameState
from game.midi.note_play import midi_through_capture_off
from game.midi.ports import get_input_port
from game.music import note_val
from game.notify import notify_correct_note, notify_sequence_success, notify_failure
import time

def print_note_prompt(game_state: GameState):
    print(f"{game_state.current_position + 1} of {len(game_state.target_sequence)}")
    # instead of printing new lines for each note, it should print them on the same line with greyed out question marks for the notes that have not been played yet AI!



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
