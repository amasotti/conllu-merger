import argparse
from merger import concatenate_conllu, download_from_github, rm_tmp_files


def main():
    parser = argparse.ArgumentParser(description="Concatenate Conllu files.")
    parser.add_argument("--source", "-s", help="Source folder containing Conllu files.", type=str, required=False)
    parser.add_argument("--pattern", "-p", help="File pattern to match.", type=str, default="*.conllu", required=False)
    parser.add_argument("--outfile", "-o", help="Output file name.", type=str, default="./merged.conllu", required=False)
    parser.add_argument("--github_url", "-g", help="GitHub URL for remote files.", type=str, required=False)
    args = parser.parse_args()

    # Check correct arguments
    if args.source is None and args.github_url is None:
        parser.error("Either --source or --github_url must be provided.")

    if args.github_url:
        tmp_dir = download_from_github(args.github_url)
        concatenate_conllu(tmp_dir, args.pattern, args.outfile)

        rm_tmp_files(tmp_dir)

    else:
        concatenate_conllu(args.source, args.pattern, args.outfile)


if __name__ == "__main__":
    main()
