# VinaScreen 
## Autodock Vina Virtual Screening Pipeline

This code performs virtual screening using the Autodock Vina software. It takes user inputs for the path of ligands in PDBQT format, protein in PDBQT format, size and center of the box, and output path for VINA results. It generates a configuration file for Vina and performs virtual screening on all the ligands in the input directory. It saves the results in the specified output directory and extracts the vina score for each ligand. It then sorts the results by score and finds the top 5 conformers. Finally, it generates PDB files of protein-ligand complex for the top 5 ligands ranked by binding energy.

![vinascreen1](https://user-images.githubusercontent.com/91246296/221368511-cb45cf0c-50a8-4f84-9166-07e0f741006b.png)

## Prerequisites


    Python 3.x
    Pandas library (pip install pandas)
    Autodock Vina executable


## Installation

To use this pipeline, you must have Python 3 installed on your system, as well as the following libraries:

    Pandas

You must also have Autodock Vina installed on your system .

To install Pandas , you can use the following commands:

    pip install pandas


## How to use

1.   Run the script in your local environment
2.   Provide the path of ligands in PDBQT format, path of protein in PDBQT format, size and center of the box, and output path for Vina results when prompted.
3.   The script will generate a configuration file, perform virtual screening with Vina, and save the Vina results to a CSV file.
4.   The script will also generate PDB files for the top 5 conformers, which are sorted based on their Vina results.


```python

# ask for user inputs
Enter the path of ligands in PDBQT format: <ligand_path>
Enter the path of protein in PDBQT format: <protein_path>
Enter the size of the box: <box_size>
Enter the center of the box: <center>
Enter the output path for VINA results: <output_path>
Enter the path of Autodock Vina executable: <vina_path>

```


.   vina_path: Autodock Vina executable should be in directory

.   ligand_path: the directory of the ligand files in PDBQT format

.   protein_path: the directory of the receptor file in PDBQT format

.   center: the center of the search box in x, y, z coordinates

.   box_size: the size of the search box in x, y, z dimensions

.   output_path: Path to the directory where output files will be saved.

Run the script using the following command:

```bash

    python VinaScreen.py

```
5.  The script will run Autodock Vina for ligand-receptor docking, and save the results to the results.csv file.

6.  The script will generate protein-ligand complexes for the top conformers and save them as PDB files in the output directory.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
