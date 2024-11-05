import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras as k
import h5py

def main():
    file_path = '0000_generation_per_timestep.h5'
    # read_h5_sets(file_path)

    generation = read_h5_format(file_path)

    prognose = pd.read_csv('000_Aeroport_min10_D1_f.csv', skiprows=57, sep=';')

    print(prognose)
    print(generation)


def read_h5_sets(file_path):
    with h5py.File(file_path, 'r') as file:
        print("Inhalt der Datei:")

        # Alle Gruppen und Datasets auflisten
        def print_name(name):
            print(name)

        file.visit(print_name)


def read_h5_format(file_path):
    with h5py.File(file_path, 'r') as file:
        if 'data/table' in file:
            data = file['data/table'][:]
            df = pd.DataFrame(data)

    return df


if __name__ == '__main__':
    main()