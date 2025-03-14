import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.music import note_val, note_name

class TestNoteVal(unittest.TestCase):
    def test_middle_c(self):
        self.assertEqual(note_val("C4"), 60)

    def test_octaves(self):
        self.assertEqual(note_val("C3"), 48)
        self.assertEqual(note_val("C5"), 72)

    def test_notes_in_octave(self):
        self.assertEqual(note_val("C4"), 60)
        self.assertEqual(note_val("D4"), 62)
        self.assertEqual(note_val("E4"), 64)
        self.assertEqual(note_val("F4"), 65)
        self.assertEqual(note_val("G4"), 67)
        self.assertEqual(note_val("A4"), 69)
        self.assertEqual(note_val("B4"), 71)

    def test_accidentals(self):
        self.assertEqual(note_val("C#4"), 61)
        self.assertEqual(note_val("Db4"), 61)
        self.assertEqual(note_val("F#4"), 66)
        self.assertEqual(note_val("Gb4"), 66)

    def test_edge_cases(self):
        self.assertEqual(note_val("C0"), 12)  # Lowest C
        self.assertEqual(note_val("G9"), 127)  # Highest valid note
        self.assertIsNone(note_val("C10"))  # Too high
        self.assertIsNone(note_val(""))  # Empty string
        self.assertIsNone(note_val("X4"))  # Invalid note letter
        self.assertIsNone(note_val("C"))  # Missing octave

class TestNoteName(unittest.TestCase):
    def test_middle_c(self):
        self.assertEqual(note_name(60), "C4")

    def test_octaves(self):
        self.assertEqual(note_name(48), "C3")
        self.assertEqual(note_name(72), "C5")

    def test_notes_in_octave(self):
        self.assertEqual(note_name(60), "C4")
        self.assertEqual(note_name(62), "D4")
        self.assertEqual(note_name(64), "E4")
        self.assertEqual(note_name(65), "F4")
        self.assertEqual(note_name(67), "G4")
        self.assertEqual(note_name(69), "A4")
        self.assertEqual(note_name(71), "B4")

    def test_accidentals(self):
        self.assertEqual(note_name(61), "Db4")
        self.assertEqual(note_name(66), "Gb4")

    def test_edge_cases(self):
        self.assertEqual(note_name(12), "C0")  # Lowest C
        self.assertEqual(note_name(127), "G9")  # Highest valid note
        self.assertIsNone(note_name(-1))  # Too low
        self.assertIsNone(note_name(128))  # Too high

if __name__ == "__main__":
    unittest.main()
