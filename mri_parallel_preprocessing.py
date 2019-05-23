#!/usr/bin/env python

import argparse
import os
import multiprocessing
import matlab.engine

def main():
    argparser = argparse.ArgumentParser(description='Run SPM12 neuromorphometric pipeline')
    argparser.add_argument('input_folder')
    args = argparser.parse_args()

    subjects_list = gen_subjects_list(args.input_folder)
    pool = multiprocessing.Pool(min(4, multiprocessing.cpu_count()))  # Temporarily limit to 4
    print(pool.map(run_nmp, subjects_list))


def gen_subjects_list(root_folder):
    return os.listdir(root_folder)


def run_nmp(subject_id):
    print "Starting preprocessing for subject " + subject_id
    eng = matlab.engine.start_matlab()
    return eng.isprime(37)


if __name__ == "__main__":
    main()

