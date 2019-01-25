#!/usr/bin/env python
# -*-coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import six
import sys
import codecs
import re
import os
import argparse
from collections import defaultdict
import logging

logger = logging.getLogger()

class WSCTask(object):
    def __init__(self, task_id, j_sentence, j_target, j_candidate_string, j_answer):
        self.task_id = task_id
        
        self.j_sentence = j_sentence
        self.j_target = j_target
        assert(self.j_target in self.j_sentence)
        
        self.j_candidate_string = j_candidate_string
        self.j_candidates = re.split(r"、　?", self.j_candidate_string)
        for candidate in self.j_candidates:
            assert(candidate in self.j_sentence)
        assert(len(self.j_candidates) == 2)
        
        self.j_answer = j_answer
        assert("、" not in self.j_answer)        
        assert(self.j_answer in self.j_candidates)
        
    def __str__(self):
        ret_str = ""
        ret_str = "Task ID: {}\n".format(self.task_id)
        ret_str += "{}\n".format(self.j_sentence)
        ret_str += "target:\t{}\n".format(self.j_target)
        ret_str += "cands:\t{}\n".format(",".join(self.j_candidates))
        ret_str += "answer:\t{}\n".format(self.j_answer)
        
        return ret_str
    
class WSCJaReader(object):
    def __init__(self):
        pass

    def read(self, file):
        # The bee landed on the flower because it had pollen.	ハチが花にとまった。それが花粉を持っていたからだ。		ハチは花粉があったので花にとまった。	（φに）花粉があったので、ハチは花にとまった。	ハチが花にとまった。Φが花粉を持っていたからだ。
        # it	それ				
        # "The bee,the flower"	ハチ、花				
        # the flower	花				

        tasks = []
        
        line_num = 1
        task_id = 1
        e_sentence, j_sentence = None, None
        e_target, j_target = None, None
        e_candidate_string, j_candidate_string = None, None
        e_answer, j_answer = None, None
        
        for line in codecs.open(file, 'r', 'utf-8'):
            line = line.strip() 
            remainder = line_num % 5
            if remainder == 1:
                e_sentence, j_sentence, *comment = line.split("\t")
            elif remainder == 2:
                e_target, j_target, *comment = line.split("\t")
            elif remainder == 3:
                e_candidate_string, j_candidate_string, *comment = line.split("\t")
            elif remainder == 4:
                e_answer, j_answer, *comment = line.split("\t")
            else:
                tasks.append(WSCTask(task_id, j_sentence, j_target, j_candidate_string, j_answer))
                task_id += 1
            line_num += 1

        return tasks
    
def main(args):
    wsc_ja_reader = WSCJaReader()
    
    if args.train_file is not None:
        train_set = wsc_ja_reader.read(args.train_file)
        print("Training Set:")
        for task in train_set:
            print("{}".format(task))

    if args.train_file is not None:
        test_set = wsc_ja_reader.read(args.test_file)
        print("Test Set:")
        for task in test_set:
            print("{}".format(task))

# usage: python winograd_schema_challenge_ja_reader.py --train_file train.txt --test_file test.txt
if __name__ == "__main__":
    if six.PY3:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    else:
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr)

    logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s')
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_file', dest='train_file', type=str, action='store', default=None)
    parser.add_argument('--test_file', dest='test_file', type=str, action='store', default=None)
    args = parser.parse_args()

    main(args)
