# VinaScreen 
## Autodock Vina Virtual Screening Pipeline

This is a graphical user interface (GUI) for running virtual screening with Autodock Vina. The GUI allows you to select a ligand file, a protein folder, an output folder, and specify the box size and center for the virtual screening. After running the virtual screening, the results are parsed and complex files are generated for the top-scoring ligands.

![vinascreen1](https://user-images.githubusercontent.com/91246296/221368511-cb45cf0c-50a8-4f84-9166-07e0f741006b.png)

## Prerequisites


    Python 3.x
    Pandas library (pip install pandas)
    Autodock Vina executable


## Installation

1.To use this pipeline, you must have Python 3 installed on your system, as well as the following libraries:

    Pandas

3.To install Pandas , you can use the following commands:

    pip install pandas

4.Download Autodock Vina executable from the official website: http://vina.scripps.edu/download.html

## Usage
To run the GUI, execute the following command from the root directory of the repository:
```bash

    python VinaScreen.py

```
The GUI will open, and you can select the ligand file, protein folder, output folder, and specify the box size and center for the virtual screening.

![Capture](https://user-images.githubusercontent.com/91246296/229913629-b1e9a5b8-e131-422b-9e2b-ae063a911cb3.JPG)


Click on the "Run Virtual Screening" button to start the virtual screening. The progress of the virtual screening will be displayed in the console.

After the virtual screening is complete, the top-scoring ligands will be displayed in the results table. You can select a ligand and click on the "View Complex" button to view the complex file generated for that ligand.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
