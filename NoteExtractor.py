import librosa, librosa.display
import numpy as np
class NoteExtractor :
    def __init__(self, filename : str, hop_length: int=10):
        self.filename = filename
        self.hop_length = hop_length
        self.x, self.sample_rate = librosa.load(self.filename)
        self.onset_samples, self.onset_boundaries, self.onset_times = self.get_onset_values()
        self.synthetic = None

    def get_onset_values(self) -> list:
        onset_samples = librosa.onset.onset_detect(self.x,
                                                sr=self.sample_rate, units='samples', 
                                                hop_length=self.hop_length, 
                                                backtrack=False,
                                                pre_max=20,
                                                post_max=20,
                                                pre_avg=100,
                                                post_avg=100,
                                                delta=0.2,
                                                wait=0)
        onset_boundaries = np.concatenate([[0], onset_samples, [len(self.x)]])
        onset_times = librosa.samples_to_time(onset_boundaries, sr=self.sample_rate)
        return onset_samples, onset_boundaries, onset_times

    def estimate_note(self, segment: list, fmin: float=260.0, fmax: float=2000.0) -> float:
        '''
        returns 
        f0: note frequency 
        t:  note duration 
        '''
        # Find autocorrelation of a given segment
        r = librosa.autocorrelate(segment)
        
        # Define lower and upper limits for the autocorrelation argmax.
        i_min = self.sample_rate / fmax
        i_max = self.sample_rate / fmin
        r[:int(i_min)] = 0
        r[int(i_max):] = 0
        
        # Find the location of the maximum autocorrelation.
        i = r.argmax()
        f0 = float(self.sample_rate) / i
        t =  len(segment) / self.sample_rate
        return f0, t

    def get_all_estimated_freqs(self):
        '''
        returns 
        notes_list : list of occured notes in chronological order
            notes_list[0] : note frequency
            notes_list[1] : note duration
        '''
        notes_list = []
        for i in range(len(self.onset_boundaries) - 1):
            n0 = self.onset_boundaries[i]
            n1 = self.onset_boundaries[i+1]
            f0, t = self.estimate_note(self.x[n0:n1])
            notes_list.append([f0, t])
        return notes_list

    def generate_sine(self, f0: float, n_duration: int) -> list:
        n = np.arange(n_duration)
        return 0.2*np.sin(2*np.pi*f0*n/float(self.sample_rate))

    def estimate_note_and_generate_sine(self, i: int) -> list:
        n0 = self.onset_boundaries[i]
        n1 = self.onset_boundaries[i+1]
        f0, t = self.estimate_note(self.x[n0:n1])
        return self.generate_sine(f0, n1-n0)

    def get_synthetic(self):
        if self.synthetic is None:
            self.synthetic = np.concatenate([
                self.estimate_note_and_generate_sine(i)
                for i in range(len(self.onset_boundaries)-1)])
        return self.synthetic

    def set_synthetic(self, synthetic):
        self.synthetic = synthetic

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_hop_length(self):
        return self.hop_length
    
    def set_hop_length(self, hop_lenght):
        self.hop_length = hop_lenght

    def set_x(self, x):
        self.x = x

    def get_sample_rate(self):
        return self.sample_rate 

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_x(self):
        return self.x
        
    def get_onset_samples(self):
        return self.onset_samples
    
    def set_onset_samples(self, onset_samples):
        self.onset_samples = onset_samples
    
    def get_onset_boundaries(self):
        return self.onset_boundaries
    
    def set_onset_boundaries(self, onset_boundaries):
        self.onset_boundaries = onset_boundaries
    
    def get_onset_times(self):
        return self.onset_times
    
    def set_onset_times(self, onset_times):
        self.onset_times = onset_times

