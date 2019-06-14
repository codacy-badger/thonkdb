import json
import random
import os
import pickle
import pickle


class Thonk():
    def store(data, data_file):
        fw = open(data_file, 'wb')
        pickle.dump(data, fw)
        fw.close()

    def get_value(data_file, name):
        fd = open(data_file, 'rb')
        dataset = pickle.load(fd)
        return dataset[name]

thonk = Thonk()
