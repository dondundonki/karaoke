import pyaudio
import numpy as np

# Parameters
CHUNK=8
RATE=16000

# Initialize PyAudio
p=pyaudio.PyAudio()

# input stream setup
stream=p.open(
    format = pyaudio.paFloat32,
    rate=RATE,
    channels=1,
    input_device_index = 2, 
    input=True, 
    frames_per_buffer=CHUNK
)

# output stream setup
player=p.open(
    format = pyaudio.paFloat32,
    rate=RATE,
    channels=1, 
    output=True, 
    frames_per_buffer=CHUNK
)

try:
    while True:
        data=np.frombuffer(stream.read(CHUNK,exception_on_overflow = False),dtype=np.float32)
        player.write(data,CHUNK)
except KeyboardInterrupt:
    pass
finally:
    #closes streams
    stream.stop_stream()
    stream.close()
    p.terminate()