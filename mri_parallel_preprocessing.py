#!/usr/bin/env python

import argparse
import os
import multiprocessing


def main():
    argparser = argparse.ArgumentParser(description='Run SPM12 neuromorphometric pipeline')
    argparser.add_argument('input_folder')
    args = argparser.parse_args()

    subjects_list = gen_subjects_list(args.input_folder)
    pool = multiprocessing.Pool()
    print(pool.map(run_nmp, subjects_list))


def gen_subjects_list(root_folder):
    return os.listdir(root_folder)


def run_nmp(subject_id):
    print "processing subject " + subject_id
    return "Completed"


if __name__ == "__main__":
    main()

