from midi_ports import open_midi_ports, close_midi_ports
from game import game_loop



if __name__ == "__main__":
    # list_midi_ports()

    open_midi_ports()

    # Run the game loop with the opened ports
    game_loop()

    close_midi_ports()

