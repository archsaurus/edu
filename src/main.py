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
    match primer[i]:
        case 'A': primer[i] = 'T'
        case 'C': primer[i] = 'G'
        case 'T': primer[i] = 'A'
        case 'G': primer[i] = 'C'
        case 'K': primer[i] = 'M'
    """

print(primer[::-1], rep, sep='\n')
