# Autodock Vina Virtual Screening Pipeline

This Python code performs virtual screening of ligands against a receptor using Autodock Vina. It takes as input an SDF file containing ligand structures and a PDBQT file containing the receptor structure, and outputs a CSV file containing the binding energies of the ligands sorted in ascending order, an SDF file containing the top 10 conformers ranked by binding energy, and generates a protein-ligand complex for the top 10 conformers ranked by binding energy.


## Prerequisites

    Python 3.x
    Pandas library (pip install pandas)
    RDKit library (conda install -c conda-forge rdkit)
    Autodock Vina executable


## Installation

To use this pipeline, you must have Python 3 installed on your system, as well as the following libraries:

    Pandas
    RDKit

You must also have Autodock Vina installed on your system and its path specified in the vina_path variable in the Python code.

To install Pandas and RDKit, you can use the following commands:

    pip install pandas
    pip install rdkit


## Usage

1.  Put the Autodock Vina executable in the same directory as the Python script.

2.  Put the ligand file (in SDF format) and receptor file (in PDBQT format) in the same directory as the Python script.

3.  Set the parameters in the script:


```python

# ask for user inputs
ligand_path = "Enter the path of ligands in PDBQT format: "
protein_path = "Enter the path of protein in PDBQT format: "
box_size = "Enter the size of the box: "
center = "Enter the center of the box: "

```


.   vina_path: the path to the Autodock Vina executable
.   ligand_path: the directory of the ligand files in PDBQT format
.   protein_path: the directory of the receptor file in PDBQT format
.   box_center: the center of the search box in x, y, z coordinates
.   box_size: the size of the search box in x, y, z dimensions



Run the script using the following command:

```bash

    python virtual_screening.py

```
4.  The script will run Autodock Vina for ligand-receptor docking, and save the results to the results.csv file.

5.  The script will sort the results by binding energy score and save the top conformers to the top_conformers.sdf file.

 6.  The script will generate protein-ligand complexes for the top conformers and save them as PDB files in the complexes directory.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
