import wave
import numpy as np

def detect_formants(wav_file):
    # Read the .wav file and extract the audio data
    with wave.open(wav_file, 'r') as wav:
        sample_rate = wav.getframerate()
        num_samples = wav.getnframes()
        audio_data = wav.readframes(num_samples)
    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    # Apply a pre-emphasis filter to the audio data
    audio_data = np.append(audio_data[0], audio_data[1:] - 0.95 * audio_data[:-1])

    # Divide the audio data into overlapping frames
    frame_size = 0.025 # 25ms frame size
    frame_stride = 0.01 # 10ms frame stride
    num_frames = int(np.ceil((num_samples - frame_size * sample_rate) / (frame_stride * sample_rate)))
    frames = []
    for i in range(num_frames):
        start = int(i * frame_stride * sample_rate)
        end = int(start + frame_size * sample_rate)
        frame = audio_data[start:end]
        frames.append(frame)

    # Calculate the power spectrum of each frame using FFT
    formants = []
    for frame in frames:
        spectrum = np.fft.rfft(frame)
        power_spectrum = np.abs(spectrum)**2
        formants.append(power_spectrum)

    # Find the formant peaks in the power spectrum
    # (You can use a peak-finding algorithm or fit a curve to the power spectrum and find the peaks of the curve)

    # Output the formant frequencies F1 and F2
    return formants

f1f2 = detect_formants('/Users/leo/Downloads/josh/josh ah.wav')
print(f1f2);