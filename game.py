from game_state import GameState
from midi_play import midi_receive_and_play
from midi_ports import get_input_port
from music import note_val
from notify import notify_correct_note, notify_sequence_success, notify_failure
import time

def print_note_prompt(game_state: GameState):
    print(f"Note {game_state.current_position + 1} of {len(game_state.target_sequence)}:")


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
            result = midi_receive_and_play(message)
            if result and result['type'] == 'note_off':
                played_note = result['note']
                assert type(played_note) is int

                # Exit game if E1 was played
                if played_note == note_val('E1'):
                    print("\nExiting!")
                    time.sleep(0.1)
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
                    notify_correct_note(game_state.current_target_note())
                    game_state.current_position += 1

                    # SEQUENCE SUCCESS
                    if game_state.current_position == len(game_state.target_sequence):
                        time.sleep(0.4)
                        notify_sequence_success()
                        time.sleep(2)
                        game_state.new_challenge()
                # SEQUENCE FAILURE
                else:
                    time.sleep(0.4)
                    notify_failure(game_state.current_target_note())
                    time.sleep(1)
                    game_state.new_challenge()

                print_note_prompt(game_state)

    except KeyboardInterrupt:
        print("\nExiting!")
        time.sleep(0.1)
