# MRI parallel pre-processing pipeline

## What's that ?

Wrapper to run the SPM12 neuromorphometric pipeline in parallel over multiple subjects


## Prerequisites

* Python 2.x
* Matlab
* SPM12 deployed in /opt folder
* Matalb engine for Python must be installed (see: https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
* The input folder must contain nifti files organized according to the following directory tree: subject/visit/protocol/repetition/
* All protocol names must be listed in the <proto_def_file> (pipeline documentation)

## Usage

Run `./mri_parallel_prepricessing.py <input_folder> <output_folder> <proto_def_file>`

