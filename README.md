# Autodock Vina Virtual Screening Pipeline

This Python code performs virtual screening of ligands against a receptor using Autodock Vina. It takes as input an SDF file containing ligand structures and a PDBQT file containing the receptor structure, and outputs a CSV file containing the binding energies of the ligands sorted in ascending order, and an SDF file containing the top 10 conformers ranked by binding energy.

## Installation

To use this pipeline, you must have Python 3 installed on your system, as well as the following libraries:

    Pandas
    RDKit

You must also have Autodock Vina installed on your system and its path specified in the vina_path variable in the Python code.

To install Pandas and RDKit, you can use the following commands:

    pip install pandas
    pip install rdkit

## Usage

To use the pipeline, simply run the autodock_vina_virtual_screening.py Python script, and specify the input and output files and parameters as necessary. The following parameters can be customized in the Python code:

    ligand_file: Path to the input SDF file containing the ligand structures.
    receptor_file: Path to the input PDBQT file containing the receptor structure.
    vina_path: Path to the Autodock Vina executable on your system.
    box_center: X, Y, and Z coordinates of the center of the search box in Angstroms.
    box_size: X, Y, and Z dimensions of the search box in Angstroms.
    result_file: Path to the output CSV file containing the binding energies of the ligands sorted by ascending order.
    top_conformers_file: Path to the output SDF file containing the top 10 conformers ranked by binding energy.

## Example usage:


    python autodock_vina_virtual_screening.py --ligand_file ligands.sdf --receptor_file receptor.pdbqt --vina_path /path/to/vina --box_center 10 10 10 --box_size 20 20 20 --result_file results.csv --top_conformers_file top_conformers.sdf

## Output

The pipeline outputs a CSV file containing the binding energies of the ligands sorted by ascending order, and an SDF file containing the top 10 conformers ranked by binding energy. The CSV file has two columns: "Ligand" and "Binding Energy". The SDF file contains the ligand conformations ranked by binding energy, and can be visualized using a molecular viewer such as PyMOL.

## License

This pipeline is released under the MIT License. Feel free to use, modify, and distribute the code as needed. If you use this code in your research, please cite this repository.
