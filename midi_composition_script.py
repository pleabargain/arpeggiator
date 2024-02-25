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

c_major_scale_progression = {
    "right_hand": [
        (48, 0.5), (50, 0.5), (52, 0.5), (53, 0.5),  # C3, D3, E3, F3
        (55, 0.5), (57, 0.5), (59, 0.5), (60, 0.5),  # G3, A3, B3, C4
        # Somber melody at the top of C4
        (62, 0.25), (60, 0.25), (59, 0.25), (57, 0.25), # D4, C4, B3, A3
        (55, 0.5), (57, 0.5), (59, 0.5), (60, 0.5),  # G3, A3, B3, C4
        (62, 0.5), (64, 0.5), (65, 0.5), (67, 0.5),  # D4, E4, F4, G4
        (69, 0.5), (71, 0.5), (72, 0.5),             # A4, B4, C5
        # Continue to C6
        (74, 0.5), (76, 0.5), (77, 0.5), (79, 0.5),  # D5, E5, F5, G5
        (81, 0.5), (83, 0.5), (84, 0.5),             # A5, B5, C6
        # Reverse
        (83, 0.5), (81, 0.5), (79, 0.5), (77, 0.5),  # B5, A5, G5, F5
        (76, 0.5), (74, 0.5), (72, 0.5),             # E5, D5, C5
        # Happy melody with supporting chords
        (71, 0.25), (72, 0.25), (74, 0.25), (76, 0.25), # B4, C5, D5, E5
        (77, 0.5), (79, 0.5), (81, 0.5), (83, 0.5),  # F5, G5, A5, B5
        (84, 1.0),                                    # C6
    ],
    "left_hand": [
        (36, 0.5), (38, 0.5), (40, 0.5), (41, 0.5),  # C2, D2, E2, F2
        (43, 0.5), (45, 0.5), (47, 0.5), (48, 0.5),  # G2, A2, B2, C3
        (48, 0.5), (47, 0.5), (45, 0.5), (43, 0.5),  # C3, B2, A2, G2
        (41, 0.5), (40, 0.5), (38, 0.5), (36, 0.5),  # F2, E2, D2, C2
        (36, 0.5), (38, 0.5), (40, 0.5), (41, 0.5),  # C2, D2, E2, F2
        (43, 0.5), (45, 0.5), (47, 0.5), (48, 0.5),  # G2, A2, B2, C3
        (50, 0.5), (52, 0.5), (53, 0.5), (55, 0.5),  # D3, E3, F3, G3
        (57, 0.5), (59, 0.5), (60, 0.5),             # A3, B3, C4
        # Happy melody chords
        (60, 0.25), (59, 0.25), (57, 0.25), (55, 0.25), # C4, B3, A3, G3
        (53, 0.5), (52, 0.5), (50, 0.5), (48, 0.5),  # F3, E3, D3, C3
        (47, 0.5), (45, 0.5), (43, 0.5), (41, 0.5),  # B2, A2, G2, F2
        (40, 0.5), (38, 0.5), (36, 0.5),             # E2, D2, C2
    ]
}


g_major_progression = {
    "right_hand": [
        (67, 0.5), (69, 0.5), (71, 0.5), (72, 0.5),  # G4, A4, B4, C5
        (74, 0.5), (76, 0.5), (78, 0.5), (79, 0.5),  # D5, E5, F#5, G5
        (78, 0.5), (76, 0.5), (74, 0.5), (72, 0.5),  # F#5, E5, D5, C5
        (71, 0.5), (69, 0.5), (67, 0.5), (69, 0.5),  # B4, A4, G4, A4
        (71, 0.5), (72, 0.5), (74, 1.0),             # B4, C5, D5
        (74, 0.25), (72, 0.25), (71, 0.5), (69, 0.5), # D5, C5, B4, A4
        (67, 1.0),                                    # G4
    ],
    "left_hand": [
        (55, 1.0), (62, 1.0), (59, 1.0),             # G Major chord: G3, D4, B3
        (55, 1.0), (62, 1.0), (59, 1.0),             # G Major chord: G3, D4, B3
        (55, 1.0), (62, 1.0), (59, 1.0),             # G Major chord: G3, D4, B3
        (55, 1.0), (62, 1.0), (59, 1.0),             # G Major chord: G3, D4, B3
        (55, 1.0), (62, 1.0), (59, 1.0),             # G Major chord: G3, D4, B3
    ]
}







a_major_scale_progression = {
    "right_hand": [
        (69, 0.5), (71, 0.5), (73, 0.5), (74, 0.5),  # A4, B4, C#5, D5
        (76, 0.5), (78, 0.5), (80, 0.5), (81, 0.5),  # E5, F#5, G#5, A5
        # Playful melody at the top
        (83, 0.25), (81, 0.25), (80, 0.25), (78, 0.25), # B5, A5, G#5, F#5
        (76, 0.5), (74, 0.5), (73, 0.5), (71, 0.5),  # E5, D5, C#5, B4
        (69, 0.5),                                    # A4
        # Drop down two octaves
        (45, 0.5), (47, 0.5), (49, 0.5), (50, 0.5),  # A2, B2, C#3, D3
        (52, 0.5), (54, 0.5), (56, 0.5), (57, 0.5),  # E3, F#3, G#3, A3
        # Go up the scale
        (59, 0.5), (61, 0.5), (63, 0.5), (64, 0.5),  # B3, C#4, D4, E4
        (66, 0.5), (68, 0.5), (69, 0.5),             # F#4, G#4, A4
        # Playful melody at the top
        (71, 0.25), (69, 0.25), (68, 0.25), (66, 0.25), # B4, A4, G#4, F#4
        # Go down the scale
        (64, 0.5), (63, 0.5), (61, 0.5), (59, 0.5),  # E4, D4, C#4, B3
        (57, 0.5), (56, 0.5), (54, 0.5), (52, 0.5),  # A3, G#3, F#3, E3
        (50, 0.5), (49, 0.5), (47, 0.5), (45, 0.5),  # D3, C#3, B2, A2
        # Repeat playful melody at the bottom
        (47, 0.25), (49, 0.25), (50, 0.25), (52, 0.25), # B2, C#3, D3, E3
    ],
    "left_hand": [
        (45, 0.5), (47, 0.5), (49, 0.5), (50, 0.5),  # A2, B2, C#3, D3
        (52, 0.5), (54, 0.5), (56, 0.5), (57, 0.5),  # E3, F#3, G#3, A3
        (57, 0.5), (56, 0.5), (54, 0.5), (52, 0.5),  # A3, G#3, F#3, E3
        (50, 0.5), (49, 0.5), (47, 0.5), (45, 0.5),  # D3, C#3, B2, A2
        (33, 0.5), (35, 0.5), (37, 0.5), (38, 0.5),  # A1, B1, C#2, D2
        (40, 0.5), (42, 0.5), (44, 0.5), (45, 0.5),  # E2, F#2, G#2, A2
        (45, 0.5), (44, 0.5), (42, 0.5), (40, 0.5),  # A2, G#2, F#2, E2
        (38, 0.5), (37, 0.5), (35, 0.5), (33, 0.5),  # D2, C#2, B1, A1
        (33, 0.5),                                    # A1 - End note to align with right hand
    ]
}


e_major_scale_progression = {
    "right_hand": [
        (52, 0.5), (54, 0.5), (56, 0.5), (57, 0.5),  # E3, F#3, G#3, A3
        (59, 0.5), (61, 0.5), (63, 0.5), (64, 0.5),  # B3, C#4, D#4, E4
        # Somber melody at the top of E4
        (65, 0.25), (64, 0.25), (63, 0.25), (61, 0.25), # F4, E4, D#4, C#4
        (59, 0.5), (61, 0.5), (63, 0.5), (64, 0.5),  # B3, C#4, D#4, E4
        (66, 0.5), (68, 0.5), (70, 0.5), (71, 0.5),  # F#4, G#4, A4, B4
        (73, 0.5), (75, 0.5), (76, 0.5),             # C#5, D#5, E5
        # Continue to E6
        (78, 0.5), (80, 0.5), (82, 0.5), (83, 0.5),  # F#5, G#5, A5, B5
        (85, 0.5), (87, 0.5), (88, 0.5),             # C#6, D#6, E6
        # Reverse
        (87, 0.5), (85, 0.5), (83, 0.5), (82, 0.5),  # D#6, C#6, B5, A5
        (80, 0.5), (78, 0.5), (76, 0.5),             # G#5, F#5, E5
        # Happy melody with supporting chords
        (75, 0.25), (76, 0.25), (78, 0.25), (80, 0.25), # D#5, E5, F#5, G#5
        (82, 0.5), (83, 0.5), (85, 0.5), (87, 0.5),  # A5, B5, C#6, D#6
        (88, 1.0),                                    # E6
    ],
    "left_hand": [
        (28, 0.5), (30, 0.5), (32, 0.5), (33, 0.5),  # E2, F#2, G#2, A2
        (35, 0.5), (37, 0.5), (39, 0.5), (40, 0.5),  # B2, C#3, D#3, E3
        (40, 0.5), (39, 0.5), (37, 0.5), (35, 0.5),  # E3, D#3, C#3, B2
        (33, 0.5), (32, 0.5), (30, 0.5), (28, 0.5),  # A2, G#2, F#2, E2
        (28, 0.5), (30, 0.5), (32, 0.5), (33, 0.5),  # E2, F#2, G#2, A2
        (35, 0.5), (37, 0.5), (39, 0.5), (40, 0.5),  # B2, C#3, D#3, E3
        (42, 0.5), (44, 0.5), (46, 0.5), (47, 0.5),  # F#3, G#3, A3, B3
        (49, 0.5), (51, 0.5), (52, 0.5),             # C#4, D#4, E4
        # Happy melody chords
        (52, 0.25), (51, 0.25), (49, 0.25), (47, 0.25), # E4, D#4, C#4, B3
        (46, 0.5), (44, 0.5), (42, 0.5), (40, 0.5),  # A3, G#3, F#3, E3
        (39, 0.5), (37, 0.5), (35, 0.5), (33, 0.5),  # D#3, C#3, B2, A2
        (32, 0.5), (30, 0.5), (28, 0.5),             # G#2, F#2, E2
    ]
}



b_major_scale_progression = {
    "right_hand": [
        (59, 0.5), (61, 0.5), (63, 0.5), (65, 0.5),  # B3, C#4, D#4, E4
        (66, 0.5), (68, 0.5), (70, 0.5), (71, 0.5),  # F#4, G#4, A#4, B4
        # Somber melody at the top of B4
        (73, 0.25), (71, 0.25), (70, 0.25), (68, 0.25), # C#5, B4, A#4, G#4
        (66, 0.5), (68, 0.5), (70, 0.5), (71, 0.5),  # F#4, G#4, A#4, B4
        (73, 0.5), (75, 0.5), (77, 0.5), (78, 0.5),  # C#5, D#5, E5, F#5
        (80, 0.5), (82, 0.5), (83, 0.5),             # G#5, A#5, B5
        # Continue to B6
        (85, 0.5), (87, 0.5), (89, 0.5), (90, 0.5),  # C#6, D#6, E6, F#6
        (92, 0.5), (94, 0.5), (95, 0.5),             # G#6, A#6, B6
        # Reverse
        (94, 0.5), (92, 0.5), (90, 0.5), (89, 0.5),  # A#6, G#6, F#6, E6
        (87, 0.5), (85, 0.5), (83, 0.5),             # D#6, C#6, B5
        # Happy melody with supporting chords
        (82, 0.25), (83, 0.25), (85, 0.25), (87, 0.25), # A#5, B5, C#6, D#6
        (89, 0.5), (90, 0.5), (92, 0.5), (94, 0.5),  # E6, F#6, G#6, A#6
        (95, 1.0),                                    # B6
    ],
    "left_hand": [
        (35, 0.5), (37, 0.5), (39, 0.5), (41, 0.5),  # B2, C#3, D#3, E3
        (42, 0.5), (44, 0.5), (46, 0.5), (47, 0.5),  # F#3, G#3, A#3, B3
        (47, 0.5), (46, 0.5), (44, 0.5), (42, 0.5),  # B3, A#3, G#3, F#3
        (41, 0.5), (39, 0.5), (37, 0.5), (35, 0.5),  # E3, D#3, C#3, B2
        (35, 0.5), (37, 0.5), (39, 0.5), (41, 0.5),  # B2, C#3, D#3, E3
        (42, 0.5), (44, 0.5), (46, 0.5), (47, 0.5),  # F#3, G#3, A#3, B3
        (49, 0.5), (51, 0.5), (53, 0.5), (54, 0.5),  # C#4, D#4, E4, F#4
        (56, 0.5), (58, 0.5), (59, 0.5),             # G#4, A#4, B4
        # Happy melody chords
        (59, 0.25), (58, 0.25), (56, 0.25), (54, 0.25), # B4, A#4, G#4, F#4
        (53, 0.5), (51, 0.5), (49, 0.5), (47, 0.5),  # E4, D#4, C#4, B3
        (46, 0.5), (44, 0.5), (42, 0.5), (41, 0.5),  # A#3, G#3, F#3, E3
        (39, 0.5), (37, 0.5), (35, 0.5),             # D#3, C#3, B2
    ]
}

g_flat_major_scale_progression = {
    "right_hand": [
        (42, 0.5), (43, 0.5), (45, 0.5), (47, 0.5),  # Gb3, Ab3, Bb3, Cb4
        (49, 0.5), (50, 0.5), (52, 0.5), (54, 0.5),  # Db4, Eb4, F4, Gb4
        # Somber melody at the top of Gb4
        (55, 0.25), (54, 0.25), (52, 0.25), (50, 0.25), # G4, Gb4, F4, Eb4
        (49, 0.5), (50, 0.5), (52, 0.5), (54, 0.5),  # Db4, Eb4, F4, Gb4
        (55, 0.5), (57, 0.5), (59, 0.5), (61, 0.5),  # G4, Ab4, Bb4, Cb5
        (62, 0.5), (64, 0.5), (66, 0.5),             # Db5, Eb5, F5, Gb5
        # Continue to Gb6
        (67, 0.5), (69, 0.5), (71, 0.5), (73, 0.5),  # G5, Ab5, Bb5, Cb6
        (74, 0.5), (76, 0.5), (78, 0.5),             # Db6, Eb6, F6, Gb6
        # Reverse
        (76, 0.5), (74, 0.5), (73, 0.5), (71, 0.5),  # Eb6, Db6, Cb6, Bb5
        (69, 0.5), (67, 0.5), (66, 0.5),             # Ab5, G5, F5
        # Happy melody with supporting chords
        (64, 0.25), (66, 0.25), (67, 0.25), (69, 0.25), # Eb5, F5, G5, Ab5
        (71, 0.5), (73, 0.5), (74, 0.5), (76, 0.5),  # Bb5, Cb6, Db6, Eb6
        (78, 1.0),                                    # Gb6
    ],
    "left_hand": [
        (30, 0.5), (31, 0.5), (33, 0.5), (35, 0.5),  # Gb2, Ab2, Bb2, Cb3
        (37, 0.5), (38, 0.5), (40, 0.5), (42, 0.5),  # Db3, Eb3, F3, Gb3
        (42, 0.5), (40, 0.5), (38, 0.5), (37, 0.5),  # Gb3, F3, Eb3, Db3
        (35, 0.5), (33, 0.5), (31, 0.5), (30, 0.5),  # Cb3, Bb2, Ab2, Gb2
        (30, 0.5), (31, 0.5), (33, 0.5), (35, 0.5),  # Gb2, Ab2, Bb2, Cb3
        (37, 0.5), (38, 0.5), (40, 0.5), (42, 0.5),  # Db3, Eb3, F3, Gb3
        (43, 0.5), (45, 0.5), (47, 0.5), (49, 0.5),  # G3, Ab3, Bb3, Cb4
        (50, 0.5), (52, 0.5), (54, 0.5),             # Db4, Eb4, F4, Gb4
        # Happy melody chords
        (54, 0.25), (52, 0.25), (50, 0.25), (49, 0.25), # Gb4, F4, Eb4, Db4
        (47, 0.5), (45, 0.5), (43, 0.5), (42, 0.5),  # Cb4, Bb3, Ab3, G3
        (40, 0.5), (38, 0.5), (37, 0.5), (35, 0.5),  # F3, Eb3, Db3, Cb3
        (33, 0.5), (31, 0.5), (30, 0.5),             # Bb2, Ab2, Gb2
    ]
}


d_flat_major_scale_progression = {
    "right_hand": [
        (49, 0.5), (51, 0.5), (52, 0.5), (54, 0.5),  # Db3, Eb3, F3, Gb3
        (56, 0.5), (58, 0.5), (59, 0.5), (61, 0.5),  # Ab3, Bb3, C4, Db4
        # Somber melody at the top of Db4
        (62, 0.25), (61, 0.25), (59, 0.25), (58, 0.25), # D4, Db4, C4, Bb3
        (56, 0.5), (58, 0.5), (59, 0.5), (61, 0.5),  # Ab3, Bb3, C4, Db4
        (62, 0.5), (64, 0.5), (66, 0.5), (67, 0.5),  # D4, Eb4, F4, Gb4
        (69, 0.5), (71, 0.5), (72, 0.5),             # Ab4, Bb4, C5, Db5
        # Continue to Db6
        (73, 0.5), (75, 0.5), (76, 0.5), (78, 0.5),  # D5, Eb5, F5, Gb5
        (80, 0.5), (82, 0.5), (83, 0.5),             # Ab5, Bb5, C6, Db6
        # Reverse
        (82, 0.5), (80, 0.5), (78, 0.5), (76, 0.5),  # Bb5, Ab5, Gb5, F5
        (75, 0.5), (73, 0.5), (72, 0.5),             # Eb5, D5, C5
        # Happy melody with supporting chords
        (71, 0.25), (72, 0.25), (73, 0.25), (75, 0.25), # Bb4, C5, D5, Eb5
        (76, 0.5), (78, 0.5), (80, 0.5), (82, 0.5),  # F5, Gb5, Ab5, Bb5
        (83, 1.0),                                    # C6
    ],
    "left_hand": [
        (25, 0.5), (27, 0.5), (28, 0.5), (30, 0.5),  # Db2, Eb2, F2, Gb2
        (32, 0.5), (34, 0.5), (35, 0.5), (37, 0.5),  # Ab2, Bb2, C3, Db3
        (37, 0.5), (35, 0.5), (34, 0.5), (32, 0.5),  # Db3, C3, Bb2, Ab2
        (30, 0.5), (28, 0.5), (27, 0.5), (25, 0.5),  # Gb2, F2, Eb2, Db2
        (25, 0.5), (27, 0.5), (28, 0.5), (30, 0.5),  # Db2, Eb2, F2, Gb2
        (32, 0.5), (34, 0.5), (35, 0.5), (37, 0.5),  # Ab2, Bb2, C3, Db3
        (38, 0.5), (40, 0.5), (42, 0.5), (43, 0.5),  # D3, Eb3, F3, Gb3
        (45, 0.5), (47, 0.5), (48, 0.5),             # Ab3, Bb3, C4, Db4
        # Happy melody chords
        (48, 0.25), (47, 0.25), (45, 0.25), (43, 0.25), # Db4, C4, Bb3, Ab3
        (42, 0.5), (40, 0.5), (38, 0.5), (37, 0.5),  # F3, Eb3, D3, Db3
        (35, 0.5), (34, 0.5), (32, 0.5), (30, 0.5),  # C3, Bb2, Ab2, Gb2
        (28, 0.5), (27, 0.5), (25, 0.5),             # F2, Eb2, Db2
    ]
}


a_flat_major_scale_progression = {
    "right_hand": [
        (56, 0.5), (58, 0.5), (60, 0.5), (61, 0.5),  # Ab3, Bb3, C4, Db4
        (63, 0.5), (65, 0.5), (67, 0.5), (68, 0.5),  # Eb4, F4, G4, Ab4
        # Somber melody at the top of Ab4
        (70, 0.25), (68, 0.25), (67, 0.25), (65, 0.25), # Bb4, Ab4, G4, F4
        (63, 0.5), (65, 0.5), (67, 0.5), (68, 0.5),  # Eb4, F4, G4, Ab4
        (70, 0.5), (72, 0.5), (74, 0.5), (75, 0.5),  # Bb4, C5, Db5, Eb5
        (77, 0.5), (79, 0.5), (80, 0.5),             # F5, G5, Ab5
        # Continue to Ab6
        (82, 0.5), (84, 0.5), (86, 0.5), (87, 0.5),  # Bb5, C6, Db6, Eb6
        (89, 0.5), (91, 0.5), (92, 0.5),             # F6, G6, Ab6
        # Reverse
        (91, 0.5), (89, 0.5), (87, 0.5), (86, 0.5),  # G6, F6, Eb6, Db6
        (84, 0.5), (82, 0.5), (80, 0.5),             # C6, Bb5, Ab5
        # Happy melody with supporting chords
        (79, 0.25), (80, 0.25), (82, 0.25), (84, 0.25), # G5, Ab5, Bb5, C6
        (86, 0.5), (87, 0.5), (89, 0.5), (91, 0.5),  # Db6, Eb6, F6, G6
        (92, 1.0),                                    # Ab6
    ],
    "left_hand": [
        (32, 0.5), (34, 0.5), (36, 0.5), (37, 0.5),  # Ab2, Bb2, C3, Db3
        (39, 0.5), (41, 0.5), (43, 0.5), (44, 0.5),  # Eb3, F3, G3, Ab3
        (44, 0.5), (43, 0.5), (41, 0.5), (39, 0.5),  # Ab3, G3, F3, Eb3
        (37, 0.5), (36, 0.5), (34, 0.5), (32, 0.5),  # Db3, C3, Bb2, Ab2
        (32, 0.5), (34, 0.5), (36, 0.5), (37, 0.5),  # Ab2, Bb2, C3, Db3
        (39, 0.5), (41, 0.5), (43, 0.5), (44, 0.5),  # Eb3, F3, G3, Ab3
        (46, 0.5), (48, 0.5), (50, 0.5), (51, 0.5),  # Bb3, C4, Db4, Eb4
        (53, 0.5), (55, 0.5), (56, 0.5),             # F4, G4, Ab4
        # Happy melody chords
        (56, 0.25), (55, 0.25), (53, 0.25), (51, 0.25), # Ab4, G4, F4, Eb4
        (50, 0.5), (48, 0.5), (46, 0.5), (44, 0.5),  # Db4, C4, Bb3, Ab3
        (43, 0.5), (41, 0.5), (39, 0.5), (37, 0.5),  # G3, F3, Eb3, Db3
        (36, 0.5), (34, 0.5), (32, 0.5),             # C3, Bb2, Ab2
    ]
}


e_flat_major_scale_progression = {
    "right_hand": [
        (52, 0.5), (53, 0.5), (55, 0.5), (57, 0.5),  # Eb3, F3, G3, Ab3
        (59, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),  # Bb3, C4, D4, Eb4
        # Somber melody at the top of Eb4
        (65, 0.25), (64, 0.25), (62, 0.25), (60, 0.25), # F4, Eb4, D4, C4
        (59, 0.5), (60, 0.5), (62, 0.5), (64, 0.5),  # Bb3, C4, D4, Eb4
        (65, 0.5), (67, 0.5), (69, 0.5), (71, 0.5),  # F4, G4, Ab4, Bb4
        (72, 0.5), (74, 0.5), (76, 0.5),             # C5, D5, Eb5
        # Continue to Eb6
        (77, 0.5), (79, 0.5), (81, 0.5), (83, 0.5),  # F5, G5, Ab5, Bb5
        (84, 0.5), (86, 0.5), (88, 0.5),             # C6, D6, Eb6
        # Reverse
        (86, 0.5), (84, 0.5), (83, 0.5), (81, 0.5),  # D6, C6, Bb5, Ab5
        (79, 0.5), (77, 0.5), (76, 0.5),             # G5, F5, Eb5
        # Happy melody with supporting chords
        (74, 0.25), (76, 0.25), (77, 0.25), (79, 0.25), # D5, Eb5, F5, G5
        (81, 0.5), (83, 0.5), (84, 0.5), (86, 0.5),  # Ab5, Bb5, C6, D6
        (88, 1.0),                                    # Eb6
    ],
    "left_hand": [
        (40, 0.5), (41, 0.5), (43, 0.5), (45, 0.5),  # Eb2, F2, G2, Ab2
        (47, 0.5), (48, 0.5), (50, 0.5), (52, 0.5),  # Bb2, C3, D3, Eb3
        (52, 0.5), (50, 0.5), (48, 0.5), (47, 0.5),  # Eb3, D3, C3, Bb2
        (45, 0.5), (43, 0.5), (41, 0.5), (40, 0.5),  # Ab2, G2, F2, Eb2
        (40, 0.5), (41, 0.5), (43, 0.5), (45, 0.5),  # Eb2, F2, G2, Ab2
        (47, 0.5), (48, 0.5), (50, 0.5), (52, 0.5),  # Bb2, C3, D3, Eb3
        (53, 0.5), (55, 0.5), (57, 0.5), (59, 0.5),  # F3, G3, Ab3, Bb3
        (60, 0.5), (62, 0.5), (64, 0.5),             # C4, D4, Eb4
        # Happy melody chords
        (64, 0.25), (62, 0.25), (60, 0.25), (59, 0.25), # Eb4, D4, C4, Bb3
        (57, 0.5), (55, 0.5), (53, 0.5), (52, 0.5),  # Ab3, G3, F3, Eb3
        (50, 0.5), (48, 0.5), (47, 0.5), (45, 0.5),  # D3, C3, Bb2, Ab2
        (43, 0.5), (41, 0.5), (40, 0.5),             # G2, F2, Eb2
    ]
}


b_flat_major_scale_progression = {
    "right_hand": [
        (53, 0.5), (55, 0.5), (57, 0.5), (58, 0.5),  # Bb3, C4, D4, Eb4
        (60, 0.5), (62, 0.5), (63, 0.5), (65, 0.5),  # F4, G4, A4, Bb4
        # Somber melody at the top of Bb4
        (67, 0.25), (65, 0.25), (63, 0.25), (62, 0.25), # C5, Bb4, A4, G4
        (60, 0.5), (62, 0.5), (63, 0.5), (65, 0.5),  # F4, G4, A4, Bb4
        (67, 0.5), (69, 0.5), (71, 0.5), (72, 0.5),  # C5, D5, Eb5, F5
        (74, 0.5), (76, 0.5), (77, 0.5),             # G5, A5, Bb5
        # Continue to Bb6
        (79, 0.5), (81, 0.5), (82, 0.5), (84, 0.5),  # C6, D6, Eb6, F6
        (86, 0.5), (88, 0.5), (89, 0.5),             # G6, A6, Bb6
        # Reverse
        (88, 0.5), (86, 0.5), (84, 0.5), (82, 0.5),  # A6, G6, F6, Eb6
        (81, 0.5), (79, 0.5), (77, 0.5),             # D6, C6, Bb5
        # Happy melody with supporting chords
        (76, 0.25), (77, 0.25), (79, 0.25), (81, 0.25), # G5, A5, Bb5, C6
        (82, 0.5), (84, 0.5), (86, 0.5), (88, 0.5),  # Eb6, F6, G6, A6
        (89, 1.0),                                    # Bb6
    ],
    "left_hand": [
        (41, 0.5), (43, 0.5), (45, 0.5), (46, 0.5),  # Bb2, C3, D3, Eb3
        (48, 0.5), (50, 0.5), (51, 0.5), (53, 0.5),  # F3, G3, A3, Bb3
        (53, 0.5), (51, 0.5), (50, 0.5), (48, 0.5),  # Bb3, A3, G3, F3
        (46, 0.5), (45, 0.5), (43, 0.5), (41, 0.5),  # Eb3, D3, C3, Bb2
        (41, 0.5), (43, 0.5), (45, 0.5), (46, 0.5),  # Bb2, C3, D3, Eb3
        (48, 0.5), (50, 0.5), (51, 0.5), (53, 0.5),  # F3, G3, A3, Bb3
        (55, 0.5), (57, 0.5), (58, 0.5), (60, 0.5),  # C4, D4, Eb4, F4
        (62, 0.5), (63, 0.5), (65, 0.5),             # G4, A4, Bb4
        # Happy melody chords
        (65, 0.25), (63, 0.25), (62, 0.25), (60, 0.25), # Bb4, A4, G4, F4
        (58, 0.5), (57, 0.5), (55, 0.5), (53, 0.5),  # Eb4, D4, C4, Bb3
        (51, 0.5), (50, 0.5), (48, 0.5), (46, 0.5),  # A3, G3, F3, Eb3
        (45, 0.5), (43, 0.5), (41, 0.5),             # D3, C3, Bb2
    ]
}



a_natural_minor_melody = {
    "right_hand": [
        # C2 to C3 progression with supporting chords
        (48, 0.5), (52, 0.5), (55, 0.5), (60, 0.5),  # C Major chord: C3, E3, G3, C4
        (60, 0.5), (55, 0.5), (52, 0.5), (48, 0.5),  # Reverse: C4, G3, E3, C3
        # C3 to C4 progression with supporting chords
        (60, 0.5), (64, 0.5), (67, 0.5), (72, 0.5),  # A Minor chord: C4, E4, A4, C5
        (72, 0.5), (67, 0.5), (64, 0.5), (60, 0.5),  # Reverse: C5, A4, E4, C4
        # C4 to C5 progression with supporting chords
        (72, 0.5), (76, 0.5), (79, 0.5), (84, 0.5),  # F Major chord: C5, F5, A5, C6
        (84, 0.5), (79, 0.5), (76, 0.5), (72, 0.5),  # Reverse: C6, A5, F5, C5
        # C5 to C6 progression with supporting chords
        (84, 0.5), (88, 0.5), (91, 0.5), (96, 0.5),  # G Major chord: C6, E6, G6, C7
        (96, 0.5), (91, 0.5), (88, 0.5), (84, 0.5),  # Reverse: C7, G6, E6, C6
    ],
    "left_hand": [
        # Improvised melody in A natural minor
        (36, 0.5), (38, 0.5), (40, 0.5), (43, 0.5),  # C2, D2, E2, G2
        (45, 0.5), (43, 0.5), (40, 0.5), (38, 0.5),  # A2, G2, E2, D2
        (48, 0.5), (50, 0.5), (52, 0.5), (55, 0.5),  # C3, D3, E3, G3
        (57, 0.5), (55, 0.5), (52, 0.5), (50, 0.5),  # A3, G3, E3, D3
        (60, 0.5), (62, 0.5), (64, 0.5), (67, 0.5),  # C4, D4, E4, G4
        (69, 0.5), (67, 0.5), (64, 0.5), (62, 0.5),  # A4, G4, E4, D4
        (72, 0.5), (74, 0.5), (76, 0.5), (79, 0.5),  # C5, D5, E5, G5
        (81, 0.5), (79, 0.5), (76, 0.5), (74, 0.5),  # A5, G5, E5, D5
    ]
}

e_natural_minor_melody = {
    "right_hand": [
        # C2 to C3 progression with supporting chords
        (40, 0.5), (43, 0.5), (47, 0.5), (52, 0.5),  # E Minor chord: E2, G2, B2, E3
        (52, 0.5), (47, 0.5), (43, 0.5), (40, 0.5),  # Reverse: E3, B2, G2, E2
        # C3 to C4 progression with supporting chords
        (52, 0.5), (55, 0.5), (59, 0.5), (64, 0.5),  # A Minor chord: A3, C4, E4, A4
        (64, 0.5), (59, 0.5), (55, 0.5), (52, 0.5),  # Reverse: A4, E4, C4, A3
        # C4 to C5 progression with supporting chords
        (64, 0.5), (67, 0.5), (71, 0.5), (76, 0.5),  # E Minor chord: E4, G4, B4, E5
        (76, 0.5), (71, 0.5), (67, 0.5), (64, 0.5),  # Reverse: E5, B4, G4, E4
        # C5 to C6 progression with supporting chords
        (76, 0.5), (79, 0.5), (83, 0.5), (88, 0.5),  # A Minor chord: A5, C6, E6, A6
        (88, 0.5), (83, 0.5), (79, 0.5), (76, 0.5),  # Reverse: A6, E6, C6, A5
    ],
    "left_hand": [
        # Improvised jazzy melody at C4
        (60, 0.5), (62, 0.5), (64, 0.5), (67, 0.5),  # C4, D4, E4, G4
        (69, 0.5), (67, 0.5), (64, 0.5), (62, 0.5),  # A4, G4, E4, D4
        # Improvised somber melody at C3
        (48, 0.5), (50, 0.5), (52, 0.5), (55, 0.5),  # C3, D3, E3, G3
        (57, 0.5), (55, 0.5), (52, 0.5), (50, 0.5),  # A3, G3, E3, D3
        # Repeat pattern alternating jazz and somber melodies
        # Jazzy melody at C5
        (72, 0.5), (74, 0.5), (76, 0.5), (79, 0.5),  # C5, D5, E5, G5
        (81, 0.5), (79, 0.5), (76, 0.5), (74, 0.5),  # A5, G5, E5, D5
        # Somber melody at C6
        (84, 0.5), (86, 0.5), (88, 0.5), (91, 0.5),  # C6, D6, E6, G6
        (93, 0.5), (91, 0.5), (88, 0.5), (86, 0.5),  # A6, G6, E6, D6
    ]
}


jazz_piano_251_progression_in_c_major = {
    "right_hand": [
        # 2-5-1 Progression in C Major
        (50, 0.5), (53, 0.5), (57, 0.5), (60, 0.5),  # Dm7: D3, F3, A3, C4
        (47, 0.5), (50, 0.5), (53, 0.5), (58, 0.5),  # G7: G3, B3, D4, F4
        (48, 0.5), (52, 0.5), (55, 0.5), (60, 0.5),  # CM7: C3, E3, G3, C4
        # Following the circle of fifths
        (45, 0.5), (48, 0.5), (52, 0.5), (57, 0.5),  # Fm7: F3, Ab3, C4, Eb4
        (42, 0.5), (45, 0.5), (49, 0.5), (54, 0.5),  # Bb7: Bb2, D3, F3, Ab3
        (41, 0.5), (45, 0.5), (48, 0.5), (53, 0.5),  # EbM7: Eb3, G3, Bb3, D4
    ],
    "left_hand": [
        # Dm7
        (38, 0.5), (45, 0.5), (50, 0.5), (53, 0.5),  # D2, A2, D3, F3
        # Gm7
        (43, 0.5), (47, 0.5), (50, 0.5), (53, 0.5),  # G2, D3, G3, Bb3
        # Cm7
        (48, 0.5), (52, 0.5), (55, 0.5), (58, 0.5),  # C3, G3, C4, Eb4
        # Fm7
        (41, 0.5), (45, 0.5), (48, 0.5), (52, 0.5),  # F2, C3, F3, Ab3
        # Bb7
        (46, 0.5), (50, 0.5), (53, 0.5), (56, 0.5),  # Bb2, F3, Bb3, D4
        # EbM7
        (39, 0.5), (43, 0.5), (46, 0.5), (50, 0.5),  # Eb2, Bb2, Eb3, G3
    ]
}


d_major_melody_balanced = {
    "right_hand": [
        (69, 0.5), (64, 0.5), (62, 0.5), (66, 0.5), (67, 0.5),  # A4, E4, D4, F#4, G4
        (69, 0.5), (67, 0.5), (66, 0.5), (64, 0.5), (62, 0.5),  # A4, G4, F#4, E4, D4
        (64, 0.5), (66, 0.5), (67, 0.5), (69, 0.5),             # E4, F#4, G4, A4
        (67, 0.5), (66, 0.5), (64, 0.5), (62, 0.5),             # G4, F#4, E4, D4
    ],
    "left_hand": [
        (50, 0.25), (54, 0.25), (57, 0.25), (62, 0.25),          # D Major chord: D3, F#3, A3, D4
        (50, 0.25), (54, 0.25), (57, 0.25), (62, 0.25),          # D Major chord: D3, F#3, A3, D4
        (45, 0.25), (52, 0.25), (57, 0.25), (64, 0.25),          # A Major chord: A2, E3, A3, E4
        (45, 0.25), (52, 0.25), (57, 0.25), (64, 0.25),          # A Major chord: A2, E3, A3, E4
        (42, 0.25), (47, 0.25), (50, 0.25), (55, 0.25),          # G Major chord: G2, D3, G3, D4
        (42, 0.25), (47, 0.25), (50, 0.25), (55, 0.25),          # G Major chord: G2, D3, G3, D4
        (50, 0.25), (54, 0.25), (57, 0.25), (62, 0.25),          # D Major chord: D3, F#3, A3, D4
        (50, 0.25), (54, 0.25), (57, 0.25), (62, 0.25),          # D Major chord: D3, F#3, A3, D4
        (45, 0.25), (52, 0.25), (57, 0.25), (64, 0.25),          # A Major chord: A2, E3, A3, E4
        (45, 0.25), (52, 0.25), (57, 0.25), (64, 0.25),          # A Major chord: A2, E3, A3, E4
        (42, 0.25), (47, 0.25), (50, 0.25), (55, 0.25),          # G Major chord: G2, D3, G3, D4
        (42, 0.25), (47, 0.25), (50, 0.25), (55, 0.25),          # G Major chord: G2, D3, G3, D4
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


# create a function that reverses the dictionary contents
def reverse_melody(melody):
    """
    Reverses the notes in the melody dictionary for both hands.
    """
    reversed_melody = {
        "right_hand": melody["right_hand"][::-1],
        "left_hand": melody["left_hand"][::-1]
    }
    return reversed_melody

def list_and_select_melody():
    # List of available dictionaries
    melodies = {
        "circle_of_fifths_arpeggio": circle_of_fifths_arpeggio,
        "bass_and_treble_piece": bass_and_treble_piece,
        "ascend_and_descend_bass_and_treble_piece": ascend_and_descend_bass_and_treble_piece,
        "childish_melody_with_triads": childish_melody_with_triads,
        "moody_piano_piece": moody_piano_piece,
        "harmonic_voyage_arpeggio": harmonic_voyage_arpeggio,
        "f_major_progression": f_major_progression,
        "c_major_scale_progression": c_major_scale_progression,
        "g_major_progression": g_major_progression,
        # "d_major_scale_progression": d_major_scale_progression_fixed,
        "a_major_scale_progression": a_major_scale_progression,
        "e_major_scale_progression": e_major_scale_progression,
        "b_major_scale_progression": b_major_scale_progression,
        "g_flat_major_scale_progression": g_flat_major_scale_progression,
        "a_flat_major_scale_progression": a_flat_major_scale_progression,
        "e_flat_major_scale_progression": e_flat_major_scale_progression,
        "b_flat_major_scale_progression": b_flat_major_scale_progression,
        "a_natural_minor_melody": a_natural_minor_melody,
        "e_natural_minor_melody": e_natural_minor_melody,
        "jazz_piano_251_progression_in_c_major": jazz_piano_251_progression_in_c_major,
        "d_major_melody_balanced": d_major_melody_balanced,
    }

    # Show the list of dictionaries to the user
    print("Available melodies:")
    for i, melody_name in enumerate(melodies.keys(), start=1):
        print(f"{i}. {melody_name}")

    # Allow user to select multiple melodies from the dictionary
    selections = input("Enter the numbers of the melodies you want to select, separated by commas: ")
    selected_indices = [int(index.strip()) - 1 for index in selections.split(',')]
    selected_melodies = {}
    for index in selected_indices:
        melody_name = list(melodies.keys())[index]
        selected_melodies[melody_name] = melodies[melody_name]
        print(f"You have selected: {melody_name}")

    # Return the selected melodies
    return selected_melodies


def count_notes_in_melody(melody):
    # Count the number of notes in both hands
    right_hand_notes = len(melody['right_hand'])
    left_hand_notes = len(melody['left_hand'])
    total_notes = right_hand_notes + left_hand_notes
    return total_notes



def create_midi_from_melody(melody, melody_name):
    mid = MidiFile()
    track_right = MidiTrack()
    track_left = MidiTrack()
    mid.tracks.append(track_right)
    mid.tracks.append(track_left)

    # Set tempo (microseconds per beat), assuming 120bpm for simplicity
    tempo = mido.bpm2tempo(120)
    track_right.append(mido.MetaMessage('set_tempo', tempo=tempo))

    # Convert beats to MIDI ticks. The default ticks per beat in MIDO is 480
    ticks_per_beat = mid.ticks_per_beat

    # Function to add notes to a track
    def add_notes_to_track(track, notes):
        time_elapsed = 0  # Time elapsed in ticks
        for note, duration in notes:
            # Convert duration from beats to ticks
            ticks = int(duration * ticks_per_beat)
            track.append(Message('note_on', note=note, velocity=64, time=time_elapsed))
            # For subsequent notes, the time should be 0 as we want simultaneous note off and next note on
            time_elapsed = 0
            track.append(Message('note_off', note=note, velocity=64, time=ticks))

    # Add right hand notes
    add_notes_to_track(track_right, melody['right_hand'])

    # Add left hand notes
    add_notes_to_track(track_left, melody['left_hand'])

    # Count the total number of notes in the melody
    total_notes = count_notes_in_melody(melody)

    # Save the MIDI file
    datestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Use the melody name and total note count in the file name
    midi_file_name = f"{datestamp}_{melody_name}_{total_notes}_notes.mid"
    mid.save(midi_file_name)
    print(f"MIDI file saved as {midi_file_name}")

# Existing code remains unchanged up to the end of the create_midi_from_melody function

def prompt_for_reversal(melody):
    """
    Prompts the user to decide if they want to reverse the melody.
    If yes, reverses and appends the reversed melody to the original.
    """
    reverse = input("Would you like to reverse the melody and append the reversal? (yes/no): ").strip().lower()
    if reverse == 'yes':
        reversed_melody = reverse_melody(melody)
        melody['right_hand'].extend(reversed_melody['right_hand'])
        melody['left_hand'].extend(reversed_melody['left_hand'])
        print("The melody has been reversed and appended.")
    return melody


if __name__ == "__main__":
    while True:  # Start of the loop
        selected_melodies = list_and_select_melody()
        for melody_name, melody in selected_melodies.items():
            melody = prompt_for_reversal(melody)
            create_midi_from_melody(melody, melody_name)
        
        # Check if the user wants to exit the program
        exit_program = input("Type 'exit' to quit the program, or press Enter to continue: ").strip().lower()
        if exit_program == "exit":
            break  # Exit the loop and end the program