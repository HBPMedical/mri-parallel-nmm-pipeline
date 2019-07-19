# MRI parallel neuromorphometric pipeline

## Introduction

The MRI parallel neuromorphometric pipeline is a wrapper to run the SPM12 neuromorphometric pipeline in parallel over multiple CPU cores.


## Prerequisites

* Python 2.x
* Matlab
* SPM12 deployed in /opt folder
* Matalb engine for Python must be installed (see: https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
* The input folder must contain nifti files organized according to the following directory tree: subject/visit/protocol/repetition/
* All protocol names must be listed in the <proto_def_file> (pipeline documentation)


## Installation

Run: `git clone --recursive https://github.com/HBPMedical/mri-parallel-nmm-pipeline.git`


## Usage

Run (from the project directory): `./mri_parallel_prepricessing.py <input_folder> <output_folder>`

