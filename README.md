# Pros-GNN

This repo contains the code for our paper " ProS-GNN: Predicting effects of mutations on protein stability using graph neural networks"

by Shuyu Wang*, Hongzhou Tang

Here we pioneered a deep graph neural network based method for predicting protein stability change upon mutation. After mutant part data extraction, the model encoded the molecular structure-property relationships using message passing and incorporated raw atom coordinates to enable spatial insights into the molecular systems. We trained the model using the S2648 and S3412 datasets, and tested on the Ssym and Myoglobin datasets. Compared to existing methods, our proposed method showed competitive high performance in data generalization and bias suppression with ultra-low time consumption.

![image](https://github.com/shuyu-wang/ProS-GNN/raw/main/fig1(A).png)

# Dependency

* Python 3.7
* Pytorch
* RDKit
* Rosetta
* numpy
* CUDA
* sklearn

# Installation

ProS-GNN ΔΔG  prediction is accomplished through a multi-step protocol. Each step relies on a specific third-party software that needs to be installed first. In the following, we outline the steps to install them.

### Clone ProS-GNN

Clone ProS-GNN to a local directory.

```
git clone https://github.com/HongzhouTang/Pros-GNN.git
```

### Install Rosetta 3

1. Go to https://els2.comotion.uw.edu/product/rosetta to get an academic license for Rosetta.
2. Download Rosetta 3.13 (source + binaries for Linux) from this site: https://www.rosettacommons.org/software/license-and-download
3. Extract the tarball to a local directory from which Rosetta binaries can be called by specifying their full path.

# Use the ProS-GNN

As previously mentioned, the ProS-GNN  method is a multi-step protocol. We outline the steps needed to make  predictions of a given variant or a list of variants in the following. Note that ProS-GNN requires that a protein structural model is available for the protein from which the variants are derived. In the case where an experimental structure is not available, in principle one can create a structual model through homology modeling. However, we did not test ProS-GNN under such scenario, thus, its performance when used with homology models is unknown.

1. Run the following fommand to refine the give protein structure xxxxx.pdb:

```
relax.static.linuxgccrelease -in:file:s XXXXX.pdb -relax:constrain_relax_to_start_coords -out:suffix _relaxed -out:no_nstruct_label -relax:ramp_constraints false
```
where relax.static.linuxgccrelease is the binary executable of the Rosetta FastRelax protocol for relaxing the given protein structure with the Rosetta energy function. This command will generate a PDB file named XXXXX_relaxed.pdb, which will be used in later steps.

2. Run the following command to create a structural model for each of the variants in the given list:

```
rosetta_relax.py --rosetta-bin relax.static.linuxgccrelease -l VARIANT_LIST --base-dir /path/to/where/all/XXXXX_relaxed.pdb/is/store
```

where VARIANT_LIST is a given file in which each line is a given variant in the format XXXXX POS WT MUT. For example, 1a5eA 37 L S. 
In order to better distinguish the mutation file from the wild file, we renamed the mutation file to XXXX_mutation.pdb and the wild file to XXXX_wild.pdb.Such as 1a5eA_L37S_mutation.pdb  and  1a5eA_L37S_wild.pdb

3. Run the following command to generated the PDB files containing only the structural information of the mutation:

```
cd mutation_pdb
```
```
python  mutation_pdb_preprocessing.py
```
```
cd ..
```
```
cd wild_pdb
```
```
python wild_pdb_preprocessing.py
```
4. Run the following command to train the model:

```
cd trian
```

```
python train.py
```

5. The model trained can be use to predict the Ssym dataset. Run the following comand to predict:

```
cd ..
```
```
cd predict
```
```
python predict.py
```

(You need to move the model trained to the predict floder.)
