import unittest
import time

# running this file with python says no module named midi_ports. the module is located in the parent folder. fix this AI!
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
