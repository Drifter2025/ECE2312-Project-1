from scipy.io import wavfile
import numpy as np
from scipy.io.wavfile import write

# Example usage
wav_file = "Spectro_1.wav"  # Change to your .wav file

# Read the .wav file
sample_rate, audio_data = wavfile.read(wav_file)

# Create separate copies for left and right channels
audio_data_L = audio_data.copy()
audio_data_R = audio_data.copy()

# Add delay to the right channel
delay = 4410  # Number of samples to delay (0 for 0ms, 21 for avg(.476ms), 44 for 1ms, 441 for 10ms, 4410 for 100ms)
audio_data_R = np.concatenate((np.zeros(delay), audio_data_R[:-delay]))

# Combine the audio data vectors to create a stereo signal
stereo_signal = np.vstack((audio_data_L, audio_data_R)).T  # Transpose to make it (samples, channels)

# Write the stereo signal to a .wav file
write("Shifted_100ms_right_delay.wav", sample_rate, stereo_signal)