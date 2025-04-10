import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, hilbert

# Step 1: Read and normalize the modulated audio
Fs, signal = wavfile.read("modulated_noisy_audio.wav")
signal = signal / np.max(np.abs(signal))  # Normalize to -1 to 1

# Step 2: Bandpass Filter around fc
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

fc = 9999.68  # Carrier frequency
bandwidth = 2000  # +/- 2kHz
filtered = bandpass_filter(signal, fc - bandwidth, fc + bandwidth, Fs)

# Plot the filtered signal
plt.figure(figsize=(10, 4))
plt.plot(filtered)
plt.title('Bandpass Filtered Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

# Step 3: Demodulate using Hilbert Transform (envelope detection)
analytic_signal = hilbert(filtered)
envelope = np.abs(analytic_signal)

# Plot demodulated audio signal
plt.figure(figsize=(10, 4))
plt.plot(envelope)
plt.title('Demodulated Signal (Envelope)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

# Step 4: Save the cleaned audio
envelope = envelope / np.max(np.abs(envelope))  # Normalize
audio_out = np.int16(envelope * 32767)  # Convert to 16-bit PCM
wavfile.write("recovered_audio.wav", Fs, audio_out)

print("✅ Demodulation complete! File saved as 'recovered_audio.wav'")
