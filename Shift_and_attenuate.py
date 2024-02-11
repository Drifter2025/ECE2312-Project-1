from scipy.io import wavfile
import numpy as np
from scipy.io.wavfile import write

# Using first sentence recording from spectrogram section
wav_file = "Spectro_1.wav"

# Read the .wav file
sample_rate, audio_data = wavfile.read(wav_file)

# Create separate copies for left and right channels
audio_data_L = audio_data.copy()
audio_data_R = audio_data.copy()

# Convert attenuation in dB to linear scale
attenuation_db = -6  # Attenuation in decibels
attenuation_linear = 10 ** (attenuation_db / 20)

# Attenuate the rigth channel
audio_data_R = audio_data_R * attenuation_linear

# Add delay to the right channel
delay = 4410  # Number of samples to delay (0 for 0ms, 21 for avg(.476ms), 44 for 1ms, 441 for 10ms, 4410 for 100ms)
audio_data_R = np.concatenate((np.zeros(delay), audio_data_R[:-delay]))

# Combine the audio data vectors to create a stereo signal
stereo_signal = np.vstack((audio_data_L, audio_data_R)).T  # Transpose to make it (samples, channels)

# Write the stereo signal to a .wav file
write("100ms_-6.wav", sample_rate, stereo_signal)