import os
import pandas as pd
from config_generator import generate_config_file
from complex_generator import generate_complex
from result_parser import parse_vina_result
from vina_executor import run_vina

try:
    # ask for user inputs
    ligand_path = input("Enter the path of ligands in PDBQT format: ")
    protein_path_folder = input("Enter the folder path of protein in PDBQT format: ")
    box_size = input("Enter the size of the box: ")
    center = input("Enter the center of the box: ")
    output_path = input("Enter the output path for VINA results: ")
    vina_path = input("Enter the path of Autodock Vina executable: ")

    # find protein file in the folder
    protein_path = None
    for file in os.listdir(protein_path_folder):
        if file.endswith(".pdbqt"):
            protein_path = os.path.join(protein_path_folder, file)
            break
    if protein_path is None:
        raise Exception("No protein file found in the provided folder.")

    # Generate configuration file
    generate_config_file(protein_path, box_size, center)

    # perform virtual screening with Vina
    for file in os.listdir(ligand_path):
        if file.endswith(".pdbqt"):
            ligand_file = os.path.join(ligand_path, file)
            result_file = os.path.join(output_path, file.split(".")[0] + "_result.pdbqt")
            run_vina(vina_path, "config.txt", ligand_file, result_file)

    # read VINA results
    results_df = pd.DataFrame(columns=["Ligand Name", "VINA RESULT"])
    for file in os.listdir(output_path):
        if file.endswith("_result.pdbqt") or file.endswith("_out.pdbqt"):
            ligand_name = file.split("_result.pdbqt")[0].split("_out.pdbqt")[0]
            result_file = os.path.join(output_path, file)
            vina_result = parse_vina_result(result_file)
            results_df = results_df.append({"Ligand Name": ligand_name, "VINA RESULT": vina_result}, ignore_index=True)

    # sort results by VINA RESULT and find top 5 conformers
    results_df = results_df.sort_values("VINA RESULT", ascending=False)
    top_conformers = list(results_df["Ligand Name"].head(5))

    # generate PDB file for protein and conformers
    for conformer in top_conformers:
        # generate complex file
        generate_complex(protein_path, os.path.join(ligand_path, conformer + ".pdbqt"), conformer, output_path)

except Exception as e:
    print("Error: ", e)
