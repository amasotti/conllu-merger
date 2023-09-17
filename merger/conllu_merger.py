import os
import glob
from conllu import parse_incr
from .utils import validate_path
from tqdm import tqdm

def concatenate_conllu(src_folder: str, pattern: str, outfile: str) -> None:
    """
    Concatenate Conllu files using the conllu parser
    :param src_folder: (str) The source folder containing Conllu files
    :param pattern: (str) The file pattern to match
    :param outfile: (str) The output file name
    """
    src_folder, outfile = validate_path(src_folder, outfile)
    merged_tokens = []

    # Get the list of files to be processed
    files_to_process = glob.glob(os.path.join(src_folder, pattern))

    # Initialize the progress bar
    with tqdm(total=len(files_to_process), desc="Merging files") as pbar:
        for f in files_to_process:
            with open(f, "r", encoding="utf-8") as data:
                for tokenlist in parse_incr(data):
                    merged_tokens.append(tokenlist)
            pbar.update(1)  # Update the progress bar

    with open(outfile, "w", encoding="utf-8") as out:
        out.writelines([sentence.serialize() + "\n" for sentence in merged_tokens])
