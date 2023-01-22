import subprocess
import csv
from doctest import OutputChecker
from operator import gt, truediv
from re import sub
from tabnanny import check
import numpy as np
import time
import ast
from ntpath import join
import os

from codes.utils.file import create_file_abs, create_parent_dir, dir_exists_abs, file_exists_absolute, join_dir
from codes.parameters import ASTRAL, NUMPY_EXTENSION, QUARTETS, SCRIPT_FOLDER, STATS_FOLDER, TRUE_FOLDER, WQFM, \
    COMPLETE, GENE_TREE, QUARTETS, INCOMPLETE, IMPUTED_LIST, OUTPUT_FOLDER, NUMPY_ARRAY, REMOVED_TAXA_RANGE, INPUT_FOLDER, \
    QUARTETS_EXTENSION, MODES_LIST, WORKING_FOLDER, METHODS, TERRACE_OUTPUT_FOLDER

def calculate_RF_distance_for_terrace(terrace_file_path, true_tree):
    csv_out_list = []
    with open(terrace_file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) <=2:
            return None
        for i, line in enumerate(lines):
            if i!=0:
                tmp_file = open("tmp.txt", "w")
                print(line, file=tmp_file)
                tmp_file.close()
                file_abs = join_dir("tmp.txt")
                # get RF distance
                result = ast.literal_eval(
                    subprocess.check_output(['getFpFn.py', '-t', true_tree, '-e', file_abs], encoding='UTF-8'))
                assert result[0] == result[1] == result[2]
                dist = str(result[0])
                # print(est, mode, range, file_, dist)
                csv_out_list += [("Terrace ST no. ", i, "", line, dist)]
    return csv_out_list


def calculate_RF_distance():
    true_tree = join_dir(TRUE_FOLDER, 'true-species.out.tree')
    out_dir = STATS_FOLDER

    csv_out_list = []

    for mode in MODES_LIST:
        for est in METHODS:
            RR = [''] if mode == COMPLETE else REMOVED_TAXA_RANGE
            for range in RR:
                in_dir = join_dir(OUTPUT_FOLDER, mode, range, est)
                # print(range, in_dir)
                for file_ in os.listdir(in_dir):
                    if (file_.endswith('.tre' if est == WQFM else '.out.tre')):
                        file_abs = join_dir(in_dir, file_)
                        result = ast.literal_eval(
                            subprocess.check_output(['getFpFn.py', '-t', true_tree, '-e', file_abs], encoding='UTF-8'))
                        assert result[0] == result[1] == result[2]
                        dist = str(result[0])
                        print(est, mode, range, file_, dist)
                        csv_out_list += [(est, mode, range, file_, dist)]

                        terrace_file_name = range + ".txt"
                        terrace_file_path = join_dir(TERRACE_OUTPUT_FOLDER, terrace_file_name)
                        if not file_exists_absolute(terrace_file_path):
                            print("!!!!!!!!!!!!!!!!!! File does not exist: " + terrace_file_path)
                            continue
                        output = calculate_RF_distance_for_terrace(terrace_file_path, true_tree)
                        if output is not None:
                            csv_out_list += output
                        

    stat_fl = 'stats/RF.csv'
    with open(stat_fl, 'w') as stat_file:
        csv.writer(stat_file).writerows(csv_out_list)


def main():
    calculate_RF_distance()

if __name__ == '__main__':
    main()