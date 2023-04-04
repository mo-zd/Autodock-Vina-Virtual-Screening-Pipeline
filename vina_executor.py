import os

def run_vina(vina_path, config_file, ligand_file, result_file):
    command = "{} --config {} --ligand {} --out {}".format(os.path.join(vina_path, "vina"), config_file, ligand_file, result_file)
    print("Running: ", command)
    os.system(command)
