import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import os

# Path to Autodock Vina executable
vina_path = '/path/to/vina'

# Input ligand and receptor files
ligand_file = 'ligands.sdf'
receptor_file = 'receptor.pdbqt'

# Output files
result_file = 'results.csv'
top_conformers_file = 'top_conformers.sdf'
complex_dir = 'complexes'

# Search box parameters
box_center = (10, 10, 10)
box_size = (20, 20, 20)

# Number of top conformers to save
num_top_conformers = 10


# Function to generate protein-ligand complex
def generate_complex(ligand_file, receptor_file, output_file):
    # Read ligand and receptor files
    ligand = Chem.SDMolSupplier(ligand_file)[0]
    receptor = Chem.MolFromPDBFile(receptor_file)

    # Compute ligand conformation in complex with receptor
    AllChem.EmbedMolecule(ligand)
    complex = AllChem.CombineMols(receptor, ligand)
    AllChem.EmbedMolecule(complex)

    # Write complex to file
    writer = Chem.PDBWriter(output_file)
    writer.write(complex)
    writer.close()


# Run Autodock Vina for ligand-receptor docking
os.system(f'{vina_path} --receptor {receptor_file} --ligand {ligand_file} --center_x {box_center[0]} --center_y {box_center[1]} --center_z {box_center[2]} --size_x {box_size[0]} --size_y {box_size[1]} --size_z {box_size[2]} --out {result_file} --log log.txt')

# Read docking results from CSV file
results = pd.read_csv(result_file, header=None, names=['Ligand', 'Binding Energy'])

# Sort results by binding energy
results = results.sort_values(by=['Binding Energy'])

# Save top conformers to SDF file
top_conformers = Chem.SDMolSupplier(ligand_file)
writer = Chem.SDWriter(top_conformers_file)

if not os.path.exists(complex_dir):
    os.makedirs(complex_dir)

for i in range(num_top_conformers):
    conformer = top_conformers[i]
    if conformer is not None:
        writer.write(conformer)
        # Generate protein-ligand complex for top conformers
        ligand_file = f'{i+1}.sdf'
        writer_ligand = Chem.SDWriter(ligand_file)
        writer_ligand.write(conformer)
        writer_ligand.close()
        complex_file = os.path.join(complex_dir, f'{i+1}.pdb')
        generate_complex(ligand_file, receptor_file, complex_file)

writer.close()
