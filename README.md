# Bioinformatics-Assignement

## Folder Structure
    .
    ├── Data              # Contains species genome indexes and Fast files
    ├── Output            # Generated Phylogenetic Trees
    ├── Src               # Source files
    ├── Supporting_Documents    # Assignemnt Documents
    ├── Clustalo-1.2.4          # Clustal Omega multiple Sequence Alignment Program
    ├── makefile                # Make script to execute tree generation script
    └── README.md


## Requirements
* pandas == 1.0.5
* biopython == 1.78
* matplotlib == 3.2.2

## How to obtain data

1. Place downloaded fasta files in data folder.
2. Find common bacteria set considering the common protein set.
3. For each bacteria find the starting and ending indexes of each protein to be cropped considering the genome as specified in the protein_tables.csv.
4. Run src/CSV_reformatter.py script and obtain *.csv files containing starting and ending indexes for common protein set of each bacteria.

## How to run program for available data

1. Place all formatted csv files and fasta files inside /data directory.
2. Run make file using `make` command.
3. Phylogenetic trees will be created in output directory as *png format as well as in *nex format
4. Multiple sequence allignment files will be created in output directory as <protein_name>_allignment.fasta which had been utilized for tree generation.
5. To obtain Robinson flouds distances between each pair of trees, run `Robinson_foulds_distance_calculator.py` script.
