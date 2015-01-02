#!/usr/bin/env python
"""
Program to convert gene structure in mGene AGS format to GFF3.

Usage: python ags_to_gff_conv.py in.mat > out.gff  

Requirements:
    NumPy:- http://www.numpy.org/
    SciPy:- http://www.scipy.org/ 
"""

import sys
import numpy as NP  
import scipy.io as SIO

def ags_to_gff(fname):
    """
    read the mGene AGS data format. 

    @args fname: mat file stores the AGS structure 
    @type fname: str 
    """

    mat_info = SIO.loadmat(fname, squeeze_me=True, struct_as_record=False)
    gene_details = mat_info['genes'] #TODO automatically detect the struct identifier.
    
    for each_entry in gene_details: #Iterate over the matlab struct

        SOURCE = '.'
        #SOURCE = str(NP.atleast_1d(each_entry.strain)[0]) if each_entry.strain.size else SOURCE
        SOURCE = str(each_entry.gene_info.Source) if each_entry.gene_info.Source else SOURCE
        geneLine = [str(each_entry.chr), 
                    SOURCE,
                    str(each_entry.gene_type),
                    str(each_entry.start),
                    str(each_entry.stop),
                    '.',
                    str(each_entry.strand),
                    '.',
                    'ID=%s;Name=%s' % (each_entry.name, each_entry.name)]
        print '\t'.join(geneLine) ## gene line in GFF3 
        tidx = 0 
        for transcript in NP.atleast_1d(each_entry.transcripts):
            try:
                try:
                    start = int(NP.atleast_1d(each_entry.exons)[tidx][0][0])
                    stop = int(NP.atleast_1d(each_entry.exons)[tidx][-1][1])
                except:
                    start = int(NP.atleast_1d(each_entry.exons)[tidx][0])
                    stop = int(NP.atleast_1d(each_entry.exons)[tidx][1])
            except:
                try:
                    start = int(NP.atleast_1d(each_entry.exons)[0][0])
                    stop = int(NP.atleast_1d(each_entry.exons)[-1][1])
                except:
                    start = NP.atleast_1d(each_entry.exons)[0]
                    stop = NP.atleast_1d(each_entry.exons)[1]
            TYPE = '.'
            TYPE = str(NP.atleast_1d(each_entry.transcript_type)[tidx]) if each_entry.transcript_type.size else TYPE
            tLine = [str(each_entry.chr),
                    SOURCE,
                    TYPE,
                    str(start),
                    str(stop),
                    '.',
                    str(each_entry.strand),
                    '.',
                    'ID=%s;Parent=%s' % (transcript, each_entry.name)]
            print '\t'.join(tLine) ## 
            if each_entry.utr5_exons.size:## UTR5 
                try: 
                    try:
                        if len(NP.atleast_1d(each_entry.transcripts))==1:
                            for eidx in range(len(each_entry.utr5_exons)):
                                u5Line = [str(each_entry.chr),
                                    SOURCE,
                                    'five_prime_UTR',
                                    str(each_entry.utr5_exons[eidx][0]),
                                    str(each_entry.utr5_exons[eidx][1]),
                                    '.',
                                    str(each_entry.strand),
                                    '.',
                                    'Parent=%s' % transcript]
                                print '\t'.join(u5Line)
                        else:
                            u5_start = int(each_entry.utr5_exons[tidx][0])
                            u5_stop = int(each_entry.utr5_exons[tidx][1])
                            u5Line = [str(each_entry.chr),
                                    SOURCE,
                                    'five_prime_UTR',
                                    str(u5_start),
                                    str(u5_stop),
                                    '.',
                                    str(each_entry.strand),
                                    '.',
                                    'Parent=%s' % transcript]
                            print '\t'.join(u5Line)
                    except:
                        u5_start = int(each_entry.utr5_exons[0])
                        u5_stop = int(each_entry.utr5_exons[1])
                        u5Line = [str(each_entry.chr),
                                SOURCE,
                                'five_prime_UTR',
                                str(u5_start),
                                str(u5_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent=%s' % transcript]
                        print '\t'.join(u5Line)
                except:
                    for eidx in range(len(each_entry.utr5_exons[tidx])):
                        u5Line = [str(each_entry.chr),
                                SOURCE,
                                'five_prime_UTR',
                                str(each_entry.utr5_exons[tidx][eidx][0]),
                                str(each_entry.utr5_exons[tidx][eidx][1]),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent=%s' % transcript]
                        print '\t'.join(u5Line)
            if each_entry.cds_exons.size:## CDS 
                try:
                    try:
                        if len(NP.atleast_1d(each_entry.transcripts))==1:
                            for eidx in range(len(each_entry.cds_exons)):
                                cLine = [str(each_entry.chr),
                                    SOURCE,
                                    'CDS',
                                    str(each_entry.cds_exons[eidx][0]),
                                    str(each_entry.cds_exons[eidx][1]),
                                    '.',
                                    str(each_entry.strand),
                                    '.',
                                    'Parent='+str(transcript)]
                                print '\t'.join(cLine)
                        else:
                            c_start = int(each_entry.cds_exons[tidx][0])
                            c_stop = int(each_entry.cds_exons[tidx][1])
                            cLine = [str(each_entry.chr),
                                SOURCE,
                                'CDS',
                                str(c_start),
                                str(c_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                            print '\t'.join(cLine)
                    except:
                        c_start = int(each_entry.cds_exons[0])
                        c_stop = int(each_entry.cds_exons[1])
                        cLine = [str(each_entry.chr),
                                SOURCE,
                                'CDS',
                                str(c_start),
                                str(c_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                        print '\t'.join(cLine)
                except:
                    for eidx in range(len(each_entry.cds_exons[tidx])):
                        cLine = [str(each_entry.chr),
                                SOURCE,
                                'CDS',
                                str(each_entry.cds_exons[tidx][eidx][0]),
                                str(each_entry.cds_exons[tidx][eidx][1]),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                        print '\t'.join(cLine)
            if each_entry.utr3_exons.size: ## UTR3    
                try:
                    try:
                        if len(NP.atleast_1d(each_entry.transcripts))==1:
                            for eidx in range(len(each_entry.utr3_exons)):
                                u3Line = [str(each_entry.chr),
                                    SOURCE,
                                    'three_prime_UTR',
                                    str(each_entry.utr3_exons[eidx][0]),
                                    str(each_entry.utr3_exons[eidx][1]),
                                    '.',
                                    str(each_entry.strand),
                                    '.',
                                    'Parent='+str(transcript)]
                                print '\t'.join(u3Line)
                        else:
                            u3_start = int(each_entry.utr3_exons[tidx][0])
                            u3_stop = int(each_entry.utr3_exons[tidx][1])
                            u3Line = [str(each_entry.chr),
                                SOURCE,
                                'three_prime_UTR',
                                str(u3_start),
                                str(u3_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                            print '\t'.join(u3Line)
                    except:
                        u3_start = int(each_entry.utr3_exons[0])
                        u3_stop = int(each_entry.utr3_exons[1])
                        u3Line = [str(each_entry.chr),
                                SOURCE,
                                'three_prime_UTR',
                                str(u3_start),
                                str(u3_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                        print '\t'.join(u3Line)
                except:
                    for eidx in range(len(each_entry.utr3_exons[tidx])):
                        u3Line = [str(each_entry.chr),
                                SOURCE,
                                'three_prime_UTR',
                                str(each_entry.utr3_exons[tidx][eidx][0]),
                                str(each_entry.utr3_exons[tidx][eidx][1]),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                        print '\t'.join(u3Line)
            if each_entry.exons.size:## Exons 
                try: 
                    try:
                        if len(NP.atleast_1d(each_entry.transcripts))==1:
                            for eidx in range(len(each_entry.exons)):
                                eLine = [str(each_entry.chr),
                                    SOURCE,
                                    'exon',
                                    str(each_entry.exons[eidx][0]),
                                    str(each_entry.exons[eidx][1]),
                                    '.',
                                    str(each_entry.strand),
                                    '.',
                                    'Parent='+str(transcript)]
                                print '\t'.join(eLine)
                        else:    
                            e_start = int(each_entry.exons[tidx][0])
                            e_stop = int(each_entry.exons[tidx][1])
                            eLine = [str(each_entry.chr),
                                SOURCE,
                                'exon',
                                str(e_start),
                                str(e_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                            print '\t'.join(eLine)
                    except:
                        e_start = int(each_entry.exons[0])
                        e_stop = int(each_entry.exons[1])
                        eLine = [str(each_entry.chr),
                                SOURCE,
                                'exon',
                                str(e_start),
                                str(e_stop),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                        print '\t'.join(eLine)
                except:
                    for eidx in range(len(each_entry.exons[tidx])):
                        eLine = [str(each_entry.chr),
                                SOURCE,
                                'exon',
                                str(each_entry.exons[tidx][eidx][0]),
                                str(each_entry.exons[tidx][eidx][1]),
                                '.',
                                str(each_entry.strand),
                                '.',
                                'Parent='+str(transcript)]
                        print '\t'.join(eLine)
            tidx += 1


if __name__== "__main__":
    try:
        mat_fname = sys.argv[1]
    except:
        print __doc__
        sys.exit(-1)

    ags_to_gff(mat_fname)
