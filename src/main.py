from fuzzywuzzy import fuzz

primer = 'CAGGAGGGKCCGGAGTATTGG'
primer = primer[::-1]

rep = ''
for nuc in primer:
    if   nuc == 'A': rep += 'T'
    elif nuc == 'C': rep += 'G'
    elif nuc == 'T': rep += 'A'
    elif nuc == 'G': rep += 'C'
    elif nuc == 'K': rep += 'M'
    
    """
    match nuc:
        case 'A': rep += 'T'
        case 'C': rep += 'G'
        case 'T': rep += 'A'
        case 'G': rep += 'C'
        case 'K': rep += 'M'
    """

print(primer[::-1], rep, sep='\n')
