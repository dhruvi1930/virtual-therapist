import pyaudio
import wave

def record():

    pa = pyaudio.PyAudio()
    stream_in = pa.open(
        rate=48000,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        input_device_index=1,
        frames_per_buffer=1024
    )
    print("How are you feeling today??")
    # 6 sec input
    input_audio = stream_in.read(6 * 48000)
    print("Thanks for sharing your thoughts.")
    output_filename = 'recoutput.wav'
    wav_file = wave.open(output_filename, 'wb')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(48000)
    wav_file.writeframes(input_audio)



#record()