import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import librosa


if __name__ == '__main__':
    # Define Sampling Rate or Frequency in Hz
    sr = 44100

    # Record duration in seconds
    duration = 5

    recording = sd.rec(int(duration*sr), samplerate=sr, channels=2) # we will record with a  mono or stereo channel microphone

    print("recording...............")
    sd.wait()
    write("sound.wav",sr,recording)


    x, sr = librosa.load('sound.wav')
    print("recording shape", x.shape)
    print("sampling rate", sr)

    plt.figure(figsize=(14, 5))
    librosa.display.waveshow(x, sr=sr)  