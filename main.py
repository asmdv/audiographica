import IPython
import IPython.display as ipd
from NoteExtractor import NoteExtractor

filename = 'music_samples/simple_piano.wav'
ne = NoteExtractor(filename)

print(ne.get_all_estimated_freqs())
