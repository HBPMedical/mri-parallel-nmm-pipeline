#!/usr/bin/env python2

import logging
import argparse
import os
import multiprocessing
import matlab.engine


NMP_TEMPLATE = 'TPM.nii'
OUTPUT_FORMAT = 'csv'
SPM12_PATH = '/opt/spm12'
NMP_PATH = '/home/barinjaka/mri-preprocessing-pipeline'  # TODO: get rid of this shit !!!
LOG_FILE = 'mri_pipeline.log'


def main():
    argparser = argparse.ArgumentParser(description='Run SPM12 neuromorphometric pipeline')
    argparser.add_argument('input_folder')
    argparser.add_argument('output_folder')
    argparser.add_argument('proto_def_file')
    args = argparser.parse_args()

    logging.basicConfig(level=logging.INFO, filename=os.path.join(args.output_folder, LOG_FILE))

    subjects = gen_subjects_list(args.input_folder)
    pool = multiprocessing.Pool(min(4, multiprocessing.cpu_count()))  # Temporarily limit to 4
    cmd_list = prepare_cmd_list(subjects, args.input_folder, args.output_folder, args.proto_def_file)
    pool.map(run_matlab_cmd, cmd_list)
    logging.info("Completed")


def gen_subjects_list(root_folder):
    return os.listdir(root_folder)


def prepare_cmd_list(
        subjects, input_folder, output_folder, proto_def_file, output_format=OUTPUT_FORMAT, nmp_template=NMP_TEMPLATE):
    pre = "NeuroMorphometric_pipeline('"
    post = "','" + input_folder \
           + "','" + output_folder\
           + "','','" \
           + proto_def_file \
           + "','" \
           + output_format \
           + "','" \
           + nmp_template + "')"
    return [pre + s + post for s in subjects]


def run_matlab_cmd(matlab_cmd):
    logging.info("Running : " + matlab_cmd)
    try:
        eng = matlab.engine.start_matlab()
        eng.eval("addpath(genpath('"+SPM12_PATH+"'))")
        eng.eval("addpath(genpath('"+NMP_PATH+"'))")
        ret = eng.eval(matlab_cmd)
        logging.info("Successfully ran: " + matlab_cmd)
    except matlab.engine.MatlabExecutionError as e:
        logging.warning("Failed running " + matlab_cmd + ": " + str(e))
        ret = None
    return ret


if __name__ == "__main__":
    main()

