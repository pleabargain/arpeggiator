from datetime import datetime

import mido
from mido import MidiFile, MidiTrack, Message


harmonic_voyage_arpeggio = {
    "right_hand": [
        # Ascend through the Circle of Fifths
        (60, 0.5), (64, 0.5), (67, 0.5), # C Major
        (67, 0.5), (71, 0.5), (74, 0.5), # G Major
        (62, 0.5), (66, 0.5), (69, 0.5), # D Major
        (69, 0.5), (73, 0.5), (76, 0.5), # A Major
        (64, 0.5), (68, 0.5), (71, 0.5), # E Major
        (71, 0.5), (75, 0.5), (78, 0.5), # B Major
        (66, 0.5), (70, 0.5), (73, 0.5), # F# Major
        (73, 0.5), (77, 0.5), (80, 0.5), # C# Major
        (68, 0.5), (72, 0.5), (75, 0.5), # G# Minor
        (75, 0.5), (79, 0.5), (82, 0.5), # D# Minor
        (70, 0.5), (74, 0.5), (77, 0.5), # A# Minor
        (77, 0.5), (81, 0.5), (84, 0.5), # F Minor
        (72, 0.5), (76, 0.5), (79, 0.5), # C Minor
        (79, 0.5), (83, 0.5), (86, 0.5), # G Minor
        (74, 0.5), (78, 0.5), (81, 0.5), # D Minor
        (81, 0.5), (85, 0.5), (88, 0.5), # A Minor

        # Descend back through the Circle of Fifths
        (85, 0.5), (81, 0.5), (78, 0.5), # D Minor
        (83, 0.5), (79, 0.5), (76, 0.5), # G Minor
        (81, 0.5), (77, 0.5), (74, 0.5), # C Minor
        (84, 0.5), (80, 0.5), (77, 0.5), # F Minor
        (74, 0.5), (70, 0.5), (67, 0.5), # A# Minor
        (82, 0.5), (78, 0.5), (75, 0.5), # D# Minor
        (75, 0.5), (71, 0.5), (68, 0.5), # G# Minor
        (80, 0.5), (76, 0.5), (73, 0.5), # C# Major
        (73, 0.5), (69, 0.5), (66, 0.5), # F# Major
        (78, 0.5), (74, 0.5), (71, 0.5), # B Major
        (71, 0.5), (67, 0.5), (64, 0.5), # E Major
        (76, 0.5), (72, 0.5), (69, 0.5), # A Major
        (69, 0.5), (65, 0.5), (62, 0.5), # D Major
        (74, 0.5), (71, 0.5), (67, 0.5), # G Major
        (67, 0.5), (64, 0.5), (60, 0.5), # C Major
    ],
    "left_hand": [
        # Ascend through the Circle of Fifths
        (48, 1.5), # C Major
        (55, 1.5), # G Major
        (50, 1.5), # D Major
        (57, 1.5), # A Major
        (52, 1.5), # E Major
        (59, 1.5), # B Major
        (54, 1.5), # F# Major
        (61, 1.5), # C# Major
        (56, 1.5), # G# Minor
        (63, 1.5), # D# Minor
        (58, 1.5), # A# Minor
        (65, 1.5), # F Minor
        (60, 1.5), # C Minor
        (67, 1.5), # G Minor
        (62, 1.5), # D Minor
        (69, 1.5), # A Minor

        # Descend back through the Circle of Fifths
        (62, 1.5), # D Minor
        (67, 1.5), # G Minor
        (60, 1.5), # C Minor
        (65, 1.5), # F Minor
        (58, 1.5), # A# Minor
        (63, 1.5), # D# Minor
        (56, 1.5), # G# Minor
        (61, 1.5), # C# Major
        (54, 1.5), # F# Major
        (59, 1.5), # B Major
        (52, 1.5), # E Major
        (57, 1.5), # A Major
        (50, 1.5), # D Major
        (55, 1.5), # G Major
        (48, 1.5), # C Major
    ]
}

f_major_progression = {
    "right_hand": [
        # (65, 0.5), (67, 0.5), (69, 0.5), (70, 0.5),  # F4, G4, A4, Bb4
        # (69, 0.5), (67, 0.5), (65, 0.5), (67, 0.5),  # A4, G4, F4, G4
        # (69, 0.5), (70, 0.5), (72, 1.0),             # A4, Bb4, C5
        # (72, 0.25), (70, 0.25), (69, 0.5), (67, 0.5), # C5, Bb4, A4, G4
        # (65, 1.0),                                    # F4
    ],
    "left_hand": [
        (53, 1.0), (60, 1.0), (57, 1.0),             # F Major chord: F3, C4, A3
        (53, 1.0), (60, 1.0), (57, 1.0),             # F Major chord: F3, C4, A3
        (53, 1.0), (60, 1.0), (57, 1.0),             # F Major chord: F3, C4, A3
        (52, 0.5), (60, 0.5), (57, 1.0),             # E Major chord: E3, B3, G#3
        (53, 1.0), (60, 1.0), (57, 1.0),             # F Major chord: F3, C4, A3
    ]
}



circle_of_fifths_arpeggio = {
    "right_hand": [
        # C Major
        (60, 0.5), (64, 0.5), (67, 0.5), 
        # G Major
        (67, 0.5), (71, 0.5), (74, 0.5),
        # D Major
        (62, 0.5), (66, 0.5), (69, 0.5),
        # A Major
        (69, 0.5), (73, 0.5), (76, 0.5),
        # E Major
        (64, 0.5), (68, 0.5), (71, 0.5),
        # B Major
        (71, 0.5), (75, 0.5), (78, 0.5),
        # F# Major
        (66, 0.5), (70, 0.5), (73, 0.5),
        # C# Major
        (73, 0.5), (77, 0.5), (80, 0.5),
        # G# Minor
        (68, 0.5), (72, 0.5), (75, 0.5),
        # D# Minor
        (75, 0.5), (79, 0.5), (82, 0.5),
        # A# Minor
        (70, 0.5), (74, 0.5), (77, 0.5),
        # F Minor
        (77, 0.5), (81, 0.5), (84, 0.5),
        # C Minor
        (72, 0.5), (76, 0.5), (79, 0.5),
        # G Minor
        (79, 0.5), (83, 0.5), (86, 0.5),
        # D Minor
        (74, 0.5), (78, 0.5), (81, 0.5),
        # A Minor
        (81, 0.5), (85, 0.5), (88, 0.5),
        # Return to C Major
        (60, 0.5), (64, 0.5), (67, 0.5),
    ],
    "left_hand": [
        # C Major
        (48, 1.5), 
        # G Major
        (55, 1.5),
        # D Major
        (50, 1.5),
        # A Major
        (57, 1.5),
        # E Major
        (52, 1.5),
        # B Major
        (59, 1.5),
        # F# Major
        (54, 1.5),
        # C# Major
        (61, 1.5),
        # G# Minor
        (56, 1.5),
        # D# Minor
        (63, 1.5),
        # A# Minor
        (58, 1.5),
        # F Minor
        (65, 1.5),
        # C Minor
        (60, 1.5),
        # G Minor
        (67, 1.5),
        # D Minor
        (62, 1.5),
        # A Minor
        (69, 1.5),
        # Return to C Major
        (48, 1.5),
    ]
}



bass_and_treble_piece = {
    "right_hand": [
        (60, 1.0), (64, 1.0), (67, 1.0), # C Major chord: C4, E4, G4
        (62, 1.0), (65, 1.0), (69, 1.0), # D minor chord: D4, F4, A4
        (64, 1.0), (67, 1.0), (71, 1.0), # E minor chord: E4, G4, B4
        (65, 1.0), (69, 1.0), (72, 1.0), # F Major chord: F4, A4, C5
        (67, 1.0), (71, 1.0), (74, 1.0), # G Major chord: G4, B4, D5
        (69, 1.0), (72, 1.0), (76, 1.0), # A minor chord: A4, C5, E5
        (71, 1.0), (74, 1.0), (77, 1.0), # B diminished chord: B4, D5, F5
        (60, 1.0), (64, 1.0), (67, 1.0), # Return to C Major chord: C4, E4, G4
    ],
    "left_hand": [
                (48, 3.0), # C Major root: C3
        (50, 3.0), # D minor root: D3
        (52, 3.0), # E minor root: E3
        (53, 3.0), # F Major root: F3
        (55, 3.0), # G Major root: G3
        (57, 3.0), # A minor root: A3
        (59, 3.0), # B diminished root: B3
        (48, 3.0), # Return to C Major root: C33
    ]
}

ascend_and_descend_bass_and_treble_piece = {
    "right_hand": [
        # Ascending part
        (60, 1.0), (64, 1.0), (67, 1.0), # C Major chord: C4, E4, G4
        (62, 1.0), (65, 1.0), (69, 1.0), # D minor chord: D4, F4, A4
        (64, 1.0), (67, 1.0), (71, 1.0), # E minor chord: E4, G4, B4
        (65, 1.0), (69, 1.0), (72, 1.0), # F Major chord: F4, A4, C5
        (67, 1.0), (71, 1.0), (74, 1.0), # G Major chord: G4, B4, D5
        (69, 1.0), (72, 1.0), (76, 1.0), # A minor chord: A4, C5, E5
        (71, 1.0), (74, 1.0), (77, 1.0), # B diminished chord: B4, D5, F5

        # Descending part
        (69, 1.0), (72, 1.0), (76, 1.0), # A minor chord: A4, C5, E5
        (67, 1.0), (71, 1.0), (74, 1.0), # G Major chord: G4, B4, D5
        (65, 1.0), (69, 1.0), (72, 1.0), # F Major chord: F4, A4, C5
        (64, 1.0), (67, 1.0), (71, 1.0), # E minor chord: E4, G4, B4
        (62, 1.0), (65, 1.0), (69, 1.0), # D minor chord: D4, F4, A4
        (60, 1.0), (64, 1.0), (67, 1.0), # Return to C Major chord: C4, E4, G4
    ],
    "left_hand": [
        # Ascending part
        (48, 3.0), # C Major root: C3
        (50, 3.0), # D minor root: D3
        (52, 3.0), # E minor root: E3
        (53, 3.0), # F Major root: F3
        (55, 3.0), # G Major root: G3
        (57, 3.0), # A minor root: A3
        (59, 3.0), # B diminished root: B3

        # Descending part
        (57, 3.0), # A minor root: A3
        (55, 3.0), # G Major root: G3
        (53, 3.0), # F Major root: F3
        (52, 3.0), # E minor root: E3
        (50, 3.0), # D minor root: D3
        (48, 3.0), # Return to C Major root: C3
    ]
}




# Define the melody
childish_melody_with_triads = {
    "right_hand": [
        (60, 0.5), (62, 0.5), (64, 0.5), (65, 0.5),  # C4, D4, E4, F4
        (64, 0.5), (62, 0.5), (60, 0.5), (62, 0.5),  # E4, D4, C4, D4
        (64, 0.5), (65, 0.5), (67, 1.0),             # E4, F4, G4
        (67, 0.25), (65, 0.25), (64, 0.5), (62, 0.5), # G4, F4, E4, D4
        (60, 1.0),                                    # C4
    ],
    "left_hand": [
        (48, 1.0), (55, 1.0), (52, 1.0),             # C Major chord: C3, G3, E3
        (48, 1.0), (55, 1.0), (52, 1.0),             # C Major chord: C3, G3, E3
        (48, 1.0), (55, 1.0), (52, 1.0),             # C Major chord: C3, G3, E3
        (47, 0.5), (55, 0.5), (52, 1.0),             # G Major chord: B2, G3, D3
        (48, 1.0), (55, 1.0), (52, 1.0),             # C Major chord: C3, G3, E3
    ]
}

moody_piano_piece = {
    "right_hand": [
        (60, 0.75), (58, 0.25), (60, 0.5), (63, 0.5),  # A minor motif: A3, G3, A3, D4
        (62, 0.5), (60, 0.5), (58, 0.5), (57, 0.5),  # Descending line: C4, A3, G3, F#3
        (55, 0.5), (57, 0.5), (58, 1.0),             # Climbing back up: E3, F#3, G3
        (58, 0.25), (57, 0.25), (55, 0.5), (53, 0.5), # G3, F#3, E3, D3
        (52, 1.5), (55, 0.5),                        # C3, E3 - leading back
    ],
    "left_hand": [
        (45, 1.0), (52, 1.0), (57, 1.0),             # A Minor chord: A2, E3, A3
        (44, 1.0), (51, 1.0), (55, 1.0),             # G Major chord: G2, D3, G3
        (43, 1.0), (50, 1.0), (55, 1.0),             # F Major chord: F2, C3, F3
        (42, 0.5), (49, 0.5), (54, 1.0),             # E Minor chord: E2, B2, E3
        (45, 2.0),                                   # A Minor chord: A2 - longer hold for resolution
    ]
}


def list_and_select_melodies():
    # List of available dictionaries
    melodies = {
        "circle_of_fifths_arpeggio": circle_of_fifths_arpeggio,
        "bass_and_treble_piece": bass_and_treble_piece,
        "ascend_and_descend_bass_and_treble_piece": ascend_and_descend_bass_and_treble_piece,
        "childish_melody_with_triads": childish_melody_with_triads,
        "moody_piano_piece": moody_piano_piece,
        "harmonic_voyage_arpeggio": harmonic_voyage_arpeggio,
        "f_major_progression": f_major_progression,
    }

    # Show the list of dictionaries to the user
    print("Available melodies:")
    for i, melody_name in enumerate(melodies.keys(), start=1):
        print(f"{i}. {melody_name}")

    # Allow user to select multiple dictionaries
    selections = input("Enter the numbers of the melodies you want to select (comma separated): ")
    selected_indices = [int(x.strip()) - 1 for x in selections.split(',')]
    selected_melodies = {list(melodies.keys())[i]: melodies[list(melodies.keys())[i]] for i in selected_indices}

    # Combine selected melodies
    combined_melody = {
        "right_hand": [],
        "left_hand": []
    }
    for melody in selected_melodies.values():
        combined_melody["right_hand"].extend(melody["right_hand"])
        combined_melody["left_hand"].extend(melody["left_hand"])

    # Generate file name using the first five letters of each selected dictionary
    selected_melody_names = [''.join([name[:5] for name in selected_melodies.keys()])]
    combined_melody_name = '_'.join(selected_melody_names)

    print(f"You have selected: {', '.join(selected_melodies.keys())}")
    # Return the combined melody and its generated name
    return combined_melody, combined_melody_name

# Replace the original list_and_select_melody function call with the new one
if __name__ == "__main__":
    selected_melody, selected_melody_name = list_and_select_melodies()
    create_midi_from_melody(selected_melody, selected_melody_name)