import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def plot_wav_amplitude(wav_file):
    # Read the .wav file
    sample_rate, amplitude = wavfile.read(wav_file)
    
    # Normalize amplitude to [-1, 1]
    amplitude = amplitude / (2**15)
    
    # Calculate duration
    duration = len(amplitude) / sample_rate
    
    # Create time axis
    time = np.linspace(0, duration, len(amplitude))
    
    # Plot amplitude over time
    plt.figure(figsize=(10, 4))
    plt.plot(time, amplitude)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Amplitude over Time')
    plt.show()

# Example usage
wav_file = "Mono_Amplitude_3.wav"  # Change name for sentences 1, 2 and 3
plot_wav_amplitude(wav_file)
