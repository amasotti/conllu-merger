import argparse
from merger import concatenate_conllu, download_from_github


def main():
    parser = argparse.ArgumentParser(description="Concatenate Conllu files.")
    parser.add_argument("--src_folder", help="Source folder containing Conllu files.")
    parser.add_argument("--pattern", help="File pattern to match.")
    parser.add_argument("--outfile", help="Output file name.")
    parser.add_argument("--github_url", help="GitHub URL for remote files.")
    args = parser.parse_args()

    if args.github_url:
        download_from_github(args.github_url, args.src_folder)

    concatenate_conllu(args.src_folder, args.pattern, args.outfile)


if __name__ == "__main__":
    main()
