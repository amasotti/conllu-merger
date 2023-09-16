import os


def validate_path(src_folder: str, outfile: str) -> tuple:
    """
    Validate paths and return absolute paths
    :param src_folder: The source folder containing Conllu files
    :param outfile: The output file name
    :return: A tuple containing the absolute paths of the source folder and the output file
    """
    src_folder = os.path.abspath(src_folder)
    outfile = os.path.abspath(outfile)
    # Add more validation here if needed
    return src_folder, outfile
