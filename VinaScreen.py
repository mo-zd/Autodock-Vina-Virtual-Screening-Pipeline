import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from config_generator import generate_config_file
from complex_generator import generate_complex
from result_parser import parse_vina_result
from vina_executor import run_vina
from tkinter import messagebox
import traceback

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Autodock Vina Virtual Screening")
        self.create_widgets()

    def create_widgets(self):
        # Ligand file selection
        self.ligand_label = tk.Label(self.master, text="Select Ligand File")
        self.ligand_label.pack()
        self.ligand_button = tk.Button(self.master, text="Browse", command=self.select_ligand_file)
        self.ligand_button.pack()

        # Protein file selection
        self.protein_label = tk.Label(self.master, text="Select Protein Folder")
        self.protein_label.pack()
        self.protein_button = tk.Button(self.master, text="Browse", command=self.select_protein_folder)
        self.protein_button.pack()

        # Box size input
        self.box_label = tk.Label(self.master, text="Enter Box Size")
        self.box_label.pack()
        self.box_entry = tk.Entry(self.master)
        self.box_entry.pack()

        # Box center input
        self.center_label = tk.Label(self.master, text="Enter Box Center")
        self.center_label.pack()
        self.center_entry = tk.Entry(self.master)
        self.center_entry.pack()

        # Output path selection
        self.output_label = tk.Label(self.master, text="Select Output Folder")
        self.output_label.pack()
        self.output_button = tk.Button(self.master, text="Browse", command=self.select_output_folder)
        self.output_button.pack()

        # Vina path input
        self.vina_label = tk.Label(self.master, text="Enter Vina Executable Path")
        self.vina_label.pack()
        self.vina_entry = tk.Entry(self.master)
        self.vina_entry.pack()

        # Run button
        self.run_button = tk.Button(self.master, text="Run Virtual Screening", command=self.run_virtual_screening)
        self.run_button.pack()

    def select_ligand_file(self):
        self.ligand_path = filedialog.askdirectory()

    def select_protein_folder(self):
        self.protein_path = filedialog.askdirectory()

    def select_output_folder(self):
        self.output_path = filedialog.askdirectory()

    def run_virtual_screening(self):
        try:
            # get user inputs
            ligand_path = self.ligand_path
            protein_path_folder = self.protein_path
            box_size = self.box_entry.get()
            center = self.center_entry.get()
            output_path = self.output_path
            vina_path = self.vina_entry.get()

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
                    
                    # generate complex files
                    generate_complex(protein_path, ligand_file, ligand_name, output_path)

            # show success message
            tk.messagebox.showinfo("Virtual Screening", "Virtual Screening completed successfully.")

        except Exception as e:
            # show error message
            error_message = str(e) + '\n\n' + traceback.format_exc()
            tk.messagebox.showerror("Error", error_message)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
