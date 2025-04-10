# 🎧 Audio Signal Recovery Project

## What's the goal?

I was given a messy, noisy audio file where the actual message was hidden inside a modulated signal — kind of like trying to listen to a song playing from a radio in the middle of a thunderstorm. The challenge was to dig through all the chaos using signal processing and bring back the clean audio.

---

## How I approached it 🚀

This is the general breakdown of how I tackled the problem:

1. **Looked at the signal** – Plotted it in the time domain to get an idea of what we’re dealing with.
2. **Did an FFT (Frequency analysis)** – To figure out the carrier frequency and where the important parts of the signal are.
3. **Bandpass filtered it** – Focused only on the frequency range around the carrier so we can isolate the real message.
4. **Demodulated it** – Used a Hilbert transform to extract the audio envelope (the actual sound).
5. **Cleaned it up further** – Applied a low-pass filter to remove leftover noise and smooth out the signal.
6. **Saved the result** – Exported both the basic demodulated version and the cleaned version as audio files.

---

## Files included in this repo 📁

- `modulated_noisy_audio.wav` – the original noisy signal
- `recovered_audio.wav` – first demodulated version
- `recovered_audio_clean.wav` – final cleaned-up audio
- `analyze_and_filter.py` – for plotting the time domain and FFT of the original signal
- `demodulate_audio.py` – handles the bandpass filtering and envelope detection
- `clean_demodulation.py` – applies low-pass filtering for extra noise reduction

---

## Plots you’ll see 🖼️

Inside the `/plots` folder, you'll find:
- `fft_spectrum.png` – shows the frequency content of the noisy signal
- `bandpass_filtered.png` – the signal after filtering around the carrier frequency
- `demodulated_signal.png` – raw envelope after Hilbert transform
- `envelope_raw_vs_clean.png` – shows the difference before and after low-pass filtering

---

## Tools Used 🧰

- Python
- NumPy, SciPy, Matplotlib

Python made it really convenient to explore, process, and visualize the signal step-by-step.

---

## Final thoughts 💭

This felt more like detective work than coding — searching for the actual message hidden in noise. It was super satisfying to go from a chaotic waveform to a clear audio signal. Also a good reminder of how useful signal processing is in the real world.

Give the cleaned audio a listen — it’s pretty cool to hear it come back to life!
