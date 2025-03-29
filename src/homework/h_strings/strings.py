def get_hamming_distance(dna1, dna2):
    distance = 0
    if len(dna1) == len(dna2):
        for i in range(len(dna1)):
            if dna1[i] != dna2[1]:
                distance += 1
    return distance

def get_dna_complement(dna):
    complement = ""
    for nucleotide in dna:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
    return complement 