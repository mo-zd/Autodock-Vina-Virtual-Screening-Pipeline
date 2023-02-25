import os
import pandas as pd


# ask for user inputs
ligand_path = input("Enter the path of ligands in PDBQT format: ")
protein_path = input("Enter the path of protein in PDBQT format: ")
box_size = input("Enter the size of the box: ")
center = input("Enter the center of the box: ")
output_path = input("Enter the output path for VINA results: ")

# Generate configuration file
config_file = open("config.txt", "w")
config_file.write(f"receptor = {protein_path}\n")
config_file.write(f"center_x = {center.split(',')[0]}\n")
config_file.write(f"center_y = {center.split(',')[1]}\n")
config_file.write(f"center_z = {center.split(',')[2]}\n")
config_file.write(f"size_x = {box_size.split(',')[0]}\n")
config_file.write(f"size_y = {box_size.split(',')[1]}\n")
config_file.write(f"size_z = {box_size.split(',')[2]}\n")
config_file.write("exhaustiveness = 8\n")
config_file.close()

# perform virtual screening with Vina
for file in os.listdir(ligand_path):
    if file.endswith(".pdbqt"):
        ligand_file = os.path.join(ligand_path, file)
        result_file = os.path.join(output_path, file.split(".")[0] + "_result.pdbqt")
        command = "vina --config config.txt --ligand {} --out {}".format(ligand_file, result_file)
        print("Running: ", command)
        os.system(command)

# read result files and extract VINA RESULT
with open("results.csv", "w") as f:
    f.write("Ligand Name, VINA RESULT\n")
    for file in os.listdir(output_path):
        if file.endswith("_result.pdbqt"):
            ligand_name = file.split("_result.pdbqt")[0]
            result_file = os.path.join(output_path, file)
            with open(result_file, "r") as r:
                lines = r.readlines()
                vina_result = ""
                for line in lines:
                    if line.startswith("REMARK VINA RESULT:"):
                        vina_result = line.split(":")[1].strip()
                        break
            f.write("{}, {}\n".format(ligand_name, vina_result))

print("Virtual screening completed!")

# read VINA results
results_df = pd.DataFrame(columns=["Ligand Name", "VINA RESULT"])
for file in os.listdir(output_path):
    if file.endswith("_result.pdbqt") or file.endswith("_out.pdbqt"):
        ligand_name = file.split("_result.pdbqt")[0].split("_out.pdbqt")[0]
        result_file = os.path.join(output_path, file)
        with open(result_file, "r") as r:
            lines = r.readlines()
            vina_result = ""
            for line in lines:
                if line.startswith("REMARK VINA RESULT:"):
                    vina_result = line.split(":")[1].strip()
                    break
        results_df = results_df.append({"Ligand Name": ligand_name, "VINA RESULT": vina_result}, ignore_index=True)

# sort results by VINA RESULT and find top 5 conformers
results_df = results_df.sort_values("VINA RESULT", ascending=False)
top_conformers = list(results_df["Ligand Name"].head(5))

# read protein PDBQT file and save protein information
with open(protein_path, "r") as p:
    protein_lines = p.readlines()
protein_info = [line for line in protein_lines if line.startswith("ATOM")]

# generate PDB file for protein and conformers
for conformer in top_conformers:
    # read conformer PDBQT file and save ligand information
    conformer_file = os.path.join(output_path, conformer + "_result.pdbqt")
    if not os.path.isfile(conformer_file):
        conformer_file = os.path.join(output_path, conformer + "_out.pdbqt")
    with open(conformer_file, "r") as c:
        conformer_lines = c.readlines()
        start_model = False
        ligand_info = []
        for line in conformer_lines:
            if "MODEL 1" in line:
                start_model = True
            elif "MODEL 2" in line:
                break
            elif start_model and line.startswith("ATOM"):
                ligand_info.append(line)

    # combine protein and ligand information and save to PDB file
    complex_info = protein_info + ligand_info
    complex_file = os.path.join(output_path, conformer + "_complex.pdb")
    with open(complex_file, "w") as f:
        f.write("HEADER COMPLEX OF {} AND {}\n".format(os.path.basename(protein_path), conformer))
        f.write("MODEL 1\n")
        for line in complex_info:
            f.write(line)
        f.write("ENDMDL\n")

print("Complex generation completed!")
