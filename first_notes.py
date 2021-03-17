from music21 import note, instrument, stream
import random

def create_midi(song_notes):
    file_name = 'my_song.mid'
    midi_stream = stream.Stream(song_notes)
    midi_stream.write('midi', fp=file_name)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
song = []
offset = 0

for i in range(1000):
    new_note = note.Note(notes[random.randrange(0, 7)])
    new_note.offset = offset
    new_note.storedInstrument = instrument.Piano()

    song.append(new_note)
    offset += 0.25


create_midi(song)