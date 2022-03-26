from NoteExtractor import NoteExtractor
from print_sheet_music2 import get_note_from_freq, get_list_of_notes, print_sheet_music, change_note_format

filename = 'music_samples/simple_piano.wav'
ne = NoteExtractor(filename)

a = ne.get_all_estimated_freqs()
notes = [round(l[0], 1) for l in a]
print(notes)
print_sheet_music(notes)