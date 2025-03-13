import unittest
import time
import sys
import os

# Add the parent directory to the Python path so we can import modules from there
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from midi_ports import open_midi_ports, close_midi_ports
from notify import play_success_sound

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

if __name__ == "__main__":
    unittest.main()
