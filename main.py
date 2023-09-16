import os
import sys
import glob


def concatenate_connlu(src_folder, pattern):
    # Initialize variable to store total length
    total_length = 0

    # Create the output file path
    output_file_path = os.path.join(src_folder, "output_file.txt")

    # Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # Loop through each file with the specific pattern in the directory
        for file_path in glob.glob(os.path.join(src_folder, pattern)):
            with open(file_path, 'r') as input_file:
                content = input_file.read()
                total_length += len(content)
                output_file.write(content)

    # Get the length of the merged file
    with open(output_file_path, 'r') as merged_file:
        merged_length = len(merged_file.read())

    # Check if the lengths are equal
    if total_length == merged_length:
        print("The lengths match.")
    else:
        print("The lengths do not match.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_folder> <file_pattern> <output_file>")
        print("Example: python script.py ./files *.txt output_file.txt")
    else:
        src_folder = sys.argv[1]
        pattern = sys.argv[2]
        outfile = sys.argv[3]
        concatenate_connlu(src_folder, pattern, outfile)
