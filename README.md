# MAPSHB_Ligand
The Machine Learning Assisted Prediction of Protein-Ligand Short Hydrogen Bonds (MAPSHB-Ligand)

MAPSHB-Ligand allows effective predictions of SHBs from a given protein structure. The MAPSHB-Ligand model is designed for SHBs that are formed from the side chain of an amino acids and a small molecule ligand. This repository is a supplementary material of the paper "<a href="https://www.researchsquare.com/article/rs-2895170/v1">Chemical Features and Machine Learning Assisted Predictions of Protein-Ligand Short Hydrogen Bonds</a>" and we encourage you to read it before using this pipeline.

**Colab notebook** <a href="https://colab.research.google.com/drive/1CJS0pDvSaKibSigDWAxkVTif_uQKZ2cX?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> - `Using this Colab notebook to run MAPSHB-Ligand prediction`

Before using this model, please make sure read the introduction on our website (https://wanggroup.rutgers.edu/mapshb-model/the-mapshb-model).

### Installation
1. Clone the repo
```bash
git clone https://github.com/shengminz/MAPSHB.git
```
2. Install AmberTools23  
```bash
conda create --name AmberTools23
conda activate AmberTools23
conda install -c conda-forge ambertools=23
```
3. Install R
```bash
conda install -c r r
conda install -c conda-forge r-gbm
```
4. Install Fortran
```bash
conda install -c conda-forge gfortran
```

### Run Prediction
1. Copy input PDB file into working directory
```bash
cd /path/to/MAPSHB #Replace /path/to/MAPSHB into the path of the working directory "MAPSHB"
cp /path/to/input/pdb/file input.pdb #Replace /path/to/input/pdb/file intp the path of the input PDB file
```
2. Prediction
```bash
chmod +x run_mapshb
./run_mapshb
```
3. Output file

File "predict_result.csv" is the output file.
