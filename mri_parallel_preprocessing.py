#!/usr/bin/env python3.6

import logging
import io
import argparse
import os
import sys
from multiprocessing import get_context
from multiprocessing import cpu_count
import matlab.engine


NMP_TEMPLATE = 'TPM.nii'
OUTPUT_FORMAT = 'csv'
SPM12_PATH = '/opt/spm12'
NMP_PATH = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'mri-preprocessing-pipeline')
PROTO_DEF_FILE = 'Protocols_definition.txt'
LOG_FILE = 'mri_pipeline.log'


def main():
    argparser = argparse.ArgumentParser(description='Run SPM12 neuromorphometric pipeline')
    argparser.add_argument('input_folder')
    argparser.add_argument('output_folder')
    args = argparser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename=os.path.join(args.output_folder, LOG_FILE))

    subjects = gen_subjects_list(args.input_folder)
    my_pool = get_context("spawn").Pool(min(6, cpu_count()))  # temporarily limit to 6 cores
    cmd_list = prepare_cmd_list(subjects, args.input_folder, args.output_folder, PROTO_DEF_FILE)

    logging.info("Starting processing...")
    my_pool.map(run_matlab_cmd, cmd_list)
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
        future = matlab.engine.start_matlab(background=True)
        eng = future.result()
        out = io.StringIO()
        err = io.StringIO()
        eng.eval("addpath(genpath('"+SPM12_PATH+"'))", stdout=out, stderr=err)
        eng.eval("addpath(genpath('"+NMP_PATH+"'))", stdout=out, stderr=err)
        ret = eng.eval(matlab_cmd, stdout=out, stderr=err)
        logging.info("Successfully ran: " + matlab_cmd)
        eng.quit()
    except Exception as e:
        logging.warning("Failed running {0} : {1}".format(matlab_cmd, str(e)))
        ret = None
    finally:
        out.close()
        err.close()
    return ret


if __name__ == "__main__":
    main()

