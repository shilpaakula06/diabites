import pytest
import nbformat
from hashlib import md5
import pandas as pd
import pickle
from fuzzywuzzy import fuzz
import pickle
import hashlib

def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def get_string():
    pickle_in = open("check.pickle","rb")
    ref_string = pickle.load(pickle_in)
    df = pd.read_csv('DiabetesNB/normalised_diabetes.csv')
    actual_string = ""
    for index, row in df.iterrows():
        actual_string += str(row[0])+str(row[1])+str(row[2])+str(row[3])+str(row[4])+str(row[5])+str(row[6])+str(row[7])+str(row[8])
    return ref_string,actual_string

class TestJupyter:
    @pytest.fixture(autouse=True)
    def get_notebook(self):
        with open('DiabetesNB/Diabetes.ipynb') as f:
            nb = nbformat.read(f, as_version=4)
        self.nb = nb
    

    def test_mean(self):
        t = get_pickle('DiabetesNB/q1.pickle')
        assert 'ad8908b474952b9fee0157676bf220c7'==t
    
    
    def test_median(self):
        t = get_pickle('DiabetesNB/q2.pickle')
        assert '36aa1c1c8c691c345544a76f5f8beacd'==t
    
    

    def test_mode(self):
        t = get_pickle('DiabetesNB/q3.pickle')
        assert '12b0300dc8a55da60d3ac3e9704f24e5'==t
    
    
    def test_normalised(self):
        ref, real = get_string()
        ratio = fuzz.ratio(real, ref)
        assert ratio > 95