import subprocess
from filesystem import directory as dir

def separate(audio_file, output_dir, track="vocals", use_old_model=False):
    """
    # separate(audio_file, output_dir, track="vocals", use_old_model=False)

    ---
    
    ### Overview
    Separates audio tracks using Demucs, isolating specific components such as vocals, bass, or drums. By default, the function isolates vocals. Users can choose to use the old model (`mdx_extra_q`) or the new model (`htdemucs`).

    ### Parameters:
    - audio_file (str or list): The path to the audio file, or a list of paths to audio files.
    - output_dir (str): The path to the directory where the output files will be saved.
    - track (str, optional): The type of track to isolate. Options are "vocals", "bass", or "drums". Defaults to "vocals".
    - use_old_model (bool, optional): If True, uses the old model (`mdx_extra_q`). If False (default), uses the new model (`htdemucs`).

    ### Returns:
    None

    ### Raises:
    - TypeError: If `audio_file` is not a string or list of strings.

    ### Examples:
    - Separates vocals from an audio file and saves the result in the specified output directory using the new model.

    ```python
    separate('your_song.wav', 'path/to/output/directory')
    ```

    - Separates bass from multiple audio files and saves the results using the old model.

    ```python
    audio_files = ['song1.wav', 'song2.mp3']
    separate(audio_files, 'path/to/output/directory', track="bass", use_old_model=True)
    ```

    - Raises a TypeError if the `audio_file` parameter is not a string or a list of strings.

    ```python
    separate(12345, 'path/to/output/directory')
    # Output: TypeError: Invalid type for audio_file: expected list or str, but got int. Please provide a valid file path or a list of file paths.
    ```
    """
    model = "mdx_extra_q" if use_old_model else "htdemucs"

    if isinstance(audio_file, list):
        for f in audio_file:
            command = f"demucs -n {model} --two-stems={track} --out {output_dir} {f}" 
            subprocess.run(command, shell=True)
    elif isinstance(audio_file, str):
        command = f"demucs -n {model} --two-stems={track} --out {output_dir} {audio_file}" 
        subprocess.run(command, shell=True)
    else:
        raise TypeError(f'Invalid type for audio_file: expected list or str, but got {type(audio_file).__name__}. Please provide a valid file path or a list of file paths.')

    demucs_output_dir = dir.join(output_dir, "htdemucs")
    for directory in dir.get_directories(demucs_output_dir):
        dir.move(directory, output_dir)
    dir.delete(demucs_output_dir, True)