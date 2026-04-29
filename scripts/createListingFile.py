import os
import sys

print('GenBank_ID\tGTDB_Genus\tGTDB_Species')
with open(sys.argv[1]) as of:
    for i, line in enumerate(of):
        if i == 0: continue
        line = line.strip('\n')
        ls = line.split('\t')
        gca = ls[57]
        gtdb_genus = ls[19].split(';g__')[1].split(';')[0]
        gtdb_species = ls[19].split(';s__')[1]
        print('\t'.join([gca, gtdb_genus, gtdb_species]))

