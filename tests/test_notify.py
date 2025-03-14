import unittest
import time
import sys
import os

# Add the parent directory to the Python path so we can import modules from there
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.midi.ports import open_midi_ports, close_midi_ports
from game.notify import play_success_sound, play_failure_sound

class TestNotify(unittest.TestCase):
    def setUp(self):
        open_midi_ports()

    def tearDown(self):
        close_midi_ports()

    def test_play_success_sound(self):
        # Test that the function runs without errors
        play_success_sound()
        # Add a small delay to ensure sound completes
        time.sleep(1)

    def test_play_failure_sound(self):
        # Test with default transpose value
        play_failure_sound()
        time.sleep(0.4)

        # Test with transpose value of 1
        play_failure_sound(1)
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()
