import os
import subprocess

working_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'working')

# Check if the working directory exists
if os.path.isdir(working_dir):
    # Get a list of files in the working directory
    files = os.listdir(working_dir)

    # Iterate over the files
    for file in files:
        file_path = os.path.join(working_dir, file)
        if os.path.isfile(file_path):
            # Transcode the file using HandBrake CLI
            transcoded_file = os.path.splitext(file)[0] + '_transcoded.mp4'
            transcoded_file_path = os.path.join(working_dir, transcoded_file)
            handbrake_command = f'HandBrakeCLI -i "{file_path}" -o "{transcoded_file_path}" -e x264 -q20 -B 160'

            # Run HandBrake CLI command
            subprocess.run(handbrake_command, shell=True)
            os.remove(file_path)

    print("All files transcoded and moved successfully.")
else:
    print("Working directory not found.")