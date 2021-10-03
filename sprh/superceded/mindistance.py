import openpyxl as op
import math


def distance(alng, alat, blng, blat):
    dist = math.sqrt(math.pow(alng - blng, 2) + math.pow(alat - blat, 2))

