# MIDI Composition Script

# code here




Ask GPT4 to create a melody for you:

https://chat.openai.com/g/g-5wHmAAefE-create-a-melody

Take the output as a dictionary

like this

```
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

```

And add it to script. You'll need to mess with the code a bit!


This script is designed to generate MIDI files based on predefined musical pieces. It utilizes the `mido` library for MIDI file creation and manipulation, offering users a selection of melodies to create MIDI files from. The script features compositions that navigate through various musical concepts, including the Circle of Fifths, chord progressions, and thematic melodies.

## Features

- Selection of predefined melodies, each with a unique musical character.
- Ability to count notes in each melody.
- Creation of MIDI files from selected melodies with timestamped filenames.
- Support for both right-hand and left-hand parts, simulating piano compositions.

## Predefined Melodies

The script includes several predefined melodies:
- `harmonic_voyage_arpeggio`: An exploration through the Circle of Fifths with ascending and descending arpeggios.
- `circle_of_fifths_arpeggio`: A concise journey through the Circle of Fifths.
- `bass_and_treble_piece`: A basic chord progression showcasing major and minor chords.
- `ascend_and_descend_bass_and_treble_piece`: A melody that ascends and descends through a series of chords.
- `childish_melody_with_triads`: A simple, catchy melody accompanied by triadic harmonies.
- `moody_piano_piece`: A piece with a melancholic mood, utilizing minor motifs and descending lines.

## Dependencies

- Python 3.x
- `mido`: A Python library for working with MIDI messages and files. Install via pip:

```bash
pip install mido
```

## How to Use
Ensure you have Python 3.x and mido installed.

Run the script. It will display a list of available melodies.

Enter the number corresponding to the melody you wish to generate as a MIDI file.

The script will create a MIDI file with the selected melody, saving it with a timestamped filename indicating the melody name and the total number of notes.

Example Usage

```
python midi_composition_script.py

```

Output
MIDI files are saved with names following this format: <timestamp>_<melody_name>_<total_notes>_notes.mid, where:

<timestamp> is the current date and time.
<melody_name> is the name of the selected melody.
<total_notes> is the total number of notes in the melody.


Enjoy creating and exploring the musical pieces provided in this script!

## License

This script is free to use for both personal and commercial purposes. Enjoy creating and exploring the musical pieces provided in this script!
