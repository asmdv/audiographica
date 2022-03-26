from NoteExtractor import NoteExtractor

filename = 'music_samples/simple_piano.wav'
ne = NoteExtractor(filename)

a = ne.get_all_estimated_freqs()
notes = [l[0] for l in a]
print(notes)