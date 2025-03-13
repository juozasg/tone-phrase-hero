def note_val(note_name):
    """
    Convert a note name (e.g., 'C4', 'F#5', 'Bb3') to its MIDI note value.
    
    Args:
        note_name (str): A string representing a musical note with format:
                         [note letter][accidental][octave]
                         where accidental is optional and can be # (sharp) or b (flat)
    
    Returns:
        int: The MIDI note value (0-127) or None if the note name is invalid
    """
    if not note_name or len(note_name) < 2:
        return None
    
    # Parse the note name
    note_letter = note_name[0].upper()
    
    # Check if there's an accidental
    idx = 1
    accidental = 0
    if idx < len(note_name) and (note_name[idx] == '#' or note_name[idx] == 'b'):
        if note_name[idx] == '#':
            accidental = 1
        else:  # flat
            accidental = -1
        idx += 1
    
    # Get the octave
    try:
        octave = int(note_name[idx:])
    except ValueError:
        return None
    
    # Base values for notes (C, D, E, F, G, A, B)
    base_values = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    
    if note_letter not in base_values:
        return None
    
    # Calculate MIDI note value
    # MIDI note 60 is middle C (C4)
    midi_value = 12 * (octave + 1) + base_values[note_letter] + accidental
    
    # Ensure the note is within MIDI range (0-127)
    if 0 <= midi_value <= 127:
        return midi_value
    else:
        return None
