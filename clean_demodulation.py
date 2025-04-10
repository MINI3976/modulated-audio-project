import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, hilbert

# Load audio and normalize
Fs, signal = wavfile.read("modulated_noisy_audio.wav")
signal = signal / np.max(np.abs(signal))

def bandpass_filter(data, lowcut, highcut, fs, order=6):
    nyq = 0.5 * fs
    b, a = butter(order, [lowcut / nyq, highcut / nyq], btype='band')
    return filtfilt(b, a, data)

def lowpass_filter(data, cutoff, fs, order=6):
    nyq = 0.5 * fs
    b, a = butter(order, cutoff / nyq, btype='low')
    return filtfilt(b, a, data)

# Carrier frequency and filtering
fc = 10000
bandwidth = 2000
filtered = bandpass_filter(signal, fc - bandwidth, fc + bandwidth, Fs)

# Demodulate using Hilbert transform
envelope = np.abs(hilbert(filtered))
cleaned = lowpass_filter(envelope, cutoff=4000, fs=Fs)

# Plot envelopes
plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(envelope)
plt.title('Envelope Before Low-pass')

plt.subplot(2, 1, 2)
plt.plot(cleaned, color='green')
plt.title('Envelope After Low-pass')
plt.tight_layout()
plt.show()

# Save the cleaned audio
cleaned = cleaned / np.max(np.abs(cleaned))
final_audio = np.int16(cleaned * 32767)
wavfile.write("recovered_audio_clean.wav", Fs, final_audio)

print("Clean audio saved as 'recovered_audio_clean.wav'")
