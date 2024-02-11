import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram

def read_wav_file(wav_file):
    # Read the .wav file
    sample_rate, audio_data = wavfile.read(wav_file)
    if len(audio_data.shape) > 1:  # If stereo, take only one channel
        audio_data = audio_data[:, 0]
    return sample_rate, audio_data

def create_spectrogram(audio_data, sample_rate):
    # Calculate spectrogram
    f, t, Sxx = spectrogram(audio_data, fs=sample_rate)
    
    # Limit frequency range to 8000Hz
    f_limit_index = np.where(f <= 8000)[0][-1]
    f = f[:f_limit_index + 1]
    Sxx = Sxx[:f_limit_index + 1, :]
    
    # Limit intensity to -100 dB
    threshold_db = -100
    Sxx = np.maximum(Sxx, 10**(threshold_db / 10))
    
    # Plot spectrogram
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud', cmap='viridis')
    plt.colorbar(label='Intensity (dB)')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.title('Spectrogram (up to 8000Hz)')
    plt.show()

# Example usage
wav_file = "Spectro_3.wav"  # Change for each sentence
sample_rate, audio_data = read_wav_file(wav_file)
create_spectrogram(audio_data, sample_rate)
