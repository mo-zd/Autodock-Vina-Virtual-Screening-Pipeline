import os

def generate_complex(protein_path, ligand_path, conformer_name, output_path):
    # read protein PDBQT file and save protein information
    with open(protein_path, "r") as p:
        protein_lines = p.readlines()
        protein_info = [line for line in protein_lines if line.startswith("ATOM")]

    # read conformer PDBQT file and save ligand information
    conformer_file = os.path.join(output_path, conformer_name + "_result.pdbqt")
    if not os.path.isfile(conformer_file):
        conformer_file = os.path.join(output_path, conformer_name + "_out.pdbqt")
    with open(conformer_file, "r") as c:
        conformer_lines = c.readlines()
        start_model = False
        ligand_info = []
        for line in conformer_lines:
            if "MODEL 1" in line:
                start_model = True
            elif "MODEL 2" in line:
                break
            elif start_model and (line.startswith("ATOM") or line.startswith("HETATM")):
                ligand_info.append(line)

    # combine protein and ligand information and save to PDB file
    complex_info = protein_info + ligand_info
    complex_file = os.path.join(output_path, conformer_name + "_complex.pdb")
    with open(complex_file, "w") as f:
        f.write("HEADER COMPLEX OF {} AND {}\n".format(protein_path, ligand_path))
        for line in complex_info:
            f.write(line)
