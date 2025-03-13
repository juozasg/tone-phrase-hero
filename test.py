import unittest
from music import note_val

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

if __name__ == "__main__":
    unittest.main()
