import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from scipy.signal import spectrogram
from scipy.io.wavfile import write

def record_audio(sample_rate, duration, channels=1):
    print("Recording...")
    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, blocking=True)
    print("Recording finished.")
    return audio_data

def create_spectrogram(audio_data, sample_rate):
    # Calculate spectrogram
    f, t, Sxx = spectrogram(audio_data[:, 0], fs=sample_rate)
    
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


sample_rate = 44100  # Change to desired sample rate
duration = 5  # Change to desired duration in seconds

audio_data = record_audio(sample_rate, duration)
create_spectrogram(audio_data, sample_rate)

# Save spectrogram and close popup to allow program to finish and save as wav file

# Write recording to a wav file
write("Spectro_3.wav",sample_rate,audio_data) # Change name for sentences 1, 2 and 3