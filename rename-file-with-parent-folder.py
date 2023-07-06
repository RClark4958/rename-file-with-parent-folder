import os
import re
import logging

# The directory where all the folders are
base_dir = r'C:\path\to\directory'  # Replace with your actual directory

# Regular expression pattern to match the folders' names
pattern = re.compile(r'^\d{4} - (.*)')

# Set up logging
logging.basicConfig(filename='script.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

for dirpath, dirnames, filenames in os.walk(base_dir):
    for dirname in dirnames:
        match = pattern.match(dirname)
        if match:
            name_to_use = match.group(1)

            # Assume there's exactly one .3ds file in each directory
            for filename in os.listdir(os.path.join(dirpath, dirname)):
                if filename.endswith('.3ds'):
                    logging.info(f'Processing file {filename} in directory {dirname}')
                    new_name = f'{name_to_use}.3ds'
                    os.rename(
                        os.path.join(dirpath, dirname, filename), 
                        os.path.join(dirpath, dirname, new_name)
                    )
                    logging.info(f'Renamed file {filename} to {new_name} in directory {dirname}')
                    break  # Since we found the .3ds file, no need to keep looking
                else:
                    logging.warning(f'No .3ds file in directory {dirname}')
        else:
            logging.warning(f'Directory {dirname} does not match the pattern')
