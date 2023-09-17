# Conllu Merger utility

This repo contains a small utility designed to download and merge files in the CoNLL-U format. 
It allows users to either merge local CoNLL-U files or download and merge files from a GitHub repository. 

This utility can be useful for researchers and developers working with natural language processing tasks that 
require combining multiple annotated datasets.


## Features

- Merge local CoNLL-U files
- Download and merge CoNLL-U files from a GitHub repository


## Installation

1. Clone the repository
```bash
git clone <repo_url>
```

2. cd into the repository
```bash
cd conllu-merger
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

## Usage 

- **Download and Merge files from a github repo**

*As example I've taken here the collection of Sanskrit texts from the [OliverHellwig/sanskrit](https://github.com/OliverHellwig/sanskrit/tree/master/dcs/data/conllu/files)*

```bash
python main.py -g https://github.com/OliverHellwig/sanskrit/tree/master/dcs/data/conllu/files/Śatapathabrāhmaṇa -p "*.conllu" --outfile "./merged.conllu"
```

- **Merge local files**

```bash
python main.py -l "./data" -p "*.conllu" --outfile "./merged.conllu"
```

### Options:

`--source, -s`: Source folder containing CoNLL-U files (local usage).
`--github_url, -g`: GitHub URL for remote files (GitHub usage).
`--pattern, -p`: File pattern to match (default is *.conllu).
`--outfile, -o`: Output file name (default is ./merged.conllu).


## License

This project is licensed under the terms of the MIT license. See [LICENSE.md](LICENSE.md) for more details.