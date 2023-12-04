# Karaoke

This repository contains two Python scripts for audio setup and real-time audio looping.

## Contents

1. **get_device_settings.py**

   - Use this script to check the supported settings for your audio input and output devices.
   - Helps in fine-tuning your audio processing parameters.

2. **in_ear_microphone.py**

   - This script creates a real-time audio loop, allowing your computer to take your voice as input and play it back through your headphones.
   - Ideal for scenarios like karaoke or in-ear monitoring.

## Usage

### get_device_settings.py

1. Run the script:

    ```bash
    python get_device_settings.py
    ```

2. Review the displayed information about your default input and output devices, including supported sample rates, channels, and more.

### in_ear_microphone.py

1. Run the script:

    ```bash
    python in_ear_microphone.py
    ```

2. Experience real-time audio looping where your voice is captured as input and played back through your headphones.

## Requirements

- Python 3.x
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) library

## Setup

1. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the scripts as described in the "Usage" section.

## Notes

- Fine-tune the audio processing parameters based on your preferences and hardware capabilities.
- Monitor the console output for information about supported device settings and potential errors.

## License

This project is licensed under the [MIT License](LICENSE).

