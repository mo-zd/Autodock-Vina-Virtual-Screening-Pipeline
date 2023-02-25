import os

# ask for user inputs
ligand_path = input("Enter the path of ligands in PDBQT format: ")
protein_path = input("Enter the path of protein in PDBQT format: ")
box_size = input("Enter the size of the box: ")
center = input("Enter the center of the box: ")

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
        result_file = os.path.join(ligand_path, file.split(".")[0] + "_result.pdbqt")
        command = "vina --config config.txt --ligand {} --out {}".format(ligand_file, result_file)
        print("Running: ", command)
        os.system(command)

# read result files and extract VINA RESULT
with open("results.csv", "w") as f:
    f.write("Ligand Name, VINA RESULT\n")
    for file in os.listdir(ligand_path):
        if file.endswith("_result.pdbqt"):
            ligand_name = file.split("_result.pdbqt")[0]
            result_file = os.path.join(ligand_path, file)
            with open(result_file, "r") as r:
                lines = r.readlines()
                vina_result = ""
                for line in lines:
                    if line.startswith("REMARK VINA RESULT:"):
                        vina_result = line.split(":")[1].strip()
                        break
            f.write("{}, {}\n".format(ligand_name, vina_result))

print("Virtual screening completed!")
