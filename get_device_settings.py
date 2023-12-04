import pyaudio

# Initialize PyAudio
p = pyaudio.PyAudio()

# Get default input device info
input_device_info = p.get_default_input_device_info()
input_chunk_size_frames = int(input_device_info["defaultLowInputLatency"] * input_device_info["defaultSampleRate"])

print("Default Input Device Sample Rates:", input_device_info["defaultSampleRate"])
print("Default Input Device Supported Chunk Sizes:", input_device_info["defaultLowInputLatency"], "-", input_device_info["defaultHighInputLatency"])
print("Default Input Device Supported Chunk Size (frames):", input_chunk_size_frames)

# Get default output device info
output_device_info = p.get_default_output_device_info()
output_chunk_size_frames = int(output_device_info["defaultLowOutputLatency"] * output_device_info["defaultSampleRate"])

print("Default Output Device Sample Rates:", output_device_info["defaultSampleRate"])
print("Default Output Device Supported Chunk Sizes:", output_device_info["defaultLowOutputLatency"], "-", output_device_info["defaultHighOutputLatency"])
print("Default Output Device Supported Chunk Size (frames):", output_chunk_size_frames)

p.terminate()