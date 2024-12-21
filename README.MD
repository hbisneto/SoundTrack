# SoundTrack

**SoundTrack** is a powerful Python library designed to simplify audio processing tasks, specifically focusing on separating various audio tracks such as vocals, bass, and drums from music files. Leveraging advanced AI models like Demucs, SoundTrack offers a straightforward way to isolate different elements of a song with high precision.

>This guide will walk you through creating a virtual environment, updating pip, and installing the Demucs package for audio source separation.

## Features
- **Track Isolation**: Easily isolate vocals, bass, and drums from music tracks.
- **Model Flexibility**: Choose between the latest `htdemucs` model or the previous `mdx_extra_q` model for optimal results.
- **Batch Processing**: Process multiple audio files in a single function call.
- **Customizable Output**: Specify the output directory for the isolated tracks.


## Prerequisites

Ensure you have Python 3 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Step 1: Create a Virtual Environment

Creating a virtual environment helps isolate your project dependencies from your system's Python installation.

1. Open your terminal or command prompt.
2. Navigate to your project directory:

   ```sh
   cd /path/to/your/project
   ```

3. Create a virtual environment named `venv`:

   ```sh
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - **On Windows:**

     ```sh
     venv\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```sh
     source venv/bin/activate
     ```

   After activation, your terminal prompt should change to indicate the virtual environment is active.

## Step 2: Update pip

Make sure pip, the Python package installer, is up to date.

1. Run the following command to update pip:

   ```sh
   python -m pip install --upgrade pip
   ```

## Step 3: Install Dependencies

#### Using pip

1. Run the following command to install Demucs:

   ```sh
   python3 -m pip install -U demucs
   ```

	This command will install the latest version of Demucs and any dependencies it requires.

2. Run the following command to install Diffq

	```sh
	python3 -m pip install diffq
	```

	This command will install the latest version of Diffq and any dependencies it requires.

	> Note: A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.2 as it may crash. To support both 1.x and 2.x versions of NumPy, modules must be compiled with NumPy 2.0. Some modules may need to be rebuilt, e.g., with `pybind11>=2.12`. If you are a user of the module, the easiest solution is to downgrade to `numpy<2` or try to upgrade the affected module.

3. Run the following command to install FileSystemPro
	
	```sh
	python3 -m pip install filesystempro
	```

#### Using requirements.txt file
After activating your virtual environment, you can easily install all the required packages by using the `requirements.txt` file. This file contains a list of all the dependencies needed for the project. Simply run the following command:

```sh
pip install -r requirements.txt
```

This will automatically install all the specified packages, ensuring that your environment is set up correctly with all necessary dependencies.

## Additional Notes

- To deactivate the virtual environment, simply run:

  ```sh
  deactivate
  ```

- If you ever need to install additional packages, make sure to do so within your virtual environment to keep your project dependencies organized.

## Usage

### Basic Example
Separate vocals from a single audio file:

```python
import soundtrack

soundtrack.separate('your_song.wav', 'path/to/output/directory')
```

### Advanced Example
Separate bass from multiple audio files using the old model:

```python
import soundtrack

audio_files = ['song1.wav', 'song2.wav']
soundtrack.separate(audio_files, 'path/to/output/directory', track="bass", use_old_model=True)
```

## Contributing

We welcome contributions! If you have suggestions for new features, find a bug, or want to improve the library, please open an issue on our GitHub repository:

[SoundTrack on GitHub](https://github.com/Hbisneto/SoundTrack)

