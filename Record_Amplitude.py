import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import IPython.display as ipd

# Sampling Rate in Hz
sr = 44100

# Duration in seconds
duration = 5

# Start recording
recording = sd.rec(int(duration*sr), samplerate=sr, channels=1) # channels=1 for mono or 2 for stereo

# Indicate recording and wait the duration
print("recording...............")
sd.wait()

# Write recording to a wav file
write("Mono_Amplitude_3.wav",sr,recording) # Change name for sentences 1, 2 and 3