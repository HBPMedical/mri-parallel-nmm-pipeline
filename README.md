# MRI parallel neuromorphometric pipeline

## Introduction

The MRI parallel neuromorphometric pipeline is a wrapper to run the SPM12 neuromorphometric pipeline in parallel over multiple CPU cores.


## Prerequisites

* Python 2.x (see: https://www.python.org/)
* Matlab (see: https://ch.mathworks.com/products/matlab.html)
* SPM12 deployed in /opt folder (see: https://www.fil.ion.ucl.ac.uk/spm/software/spm12/)
* Matalb engine for Python must be installed (see: https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
* The input folder must contain nifti files organized according to the following directory tree: subject/visit/protocol/repetition/ (see: https://github.com/HBPMedical/hierarchizer)
* If the protocol as per previous bullet-point is not T1, you'll have to update the protocol definition file from the mri-preprocessing-pipeline subproject (see: https://github.com/HBPMedical/mri-preprocessing-pipeline)


## Installation

Run: `git clone --recursive https://github.com/HBPMedical/mri-parallel-nmm-pipeline.git` or download the zipped source code at: https://github.com/HBPMedical/mri-parallel-nmm-pipeline/archive/master.zip


## Usage

Run (from the project directory): `./mri_parallel_prepricessing.py <input_folder> <output_folder>`
