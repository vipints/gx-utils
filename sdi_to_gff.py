#!/usr/bin/env python 
"""
Write GFF file based on SNP/INsertion/DELetion data

Usage:
python sdi_to_gff.py fname.sdi strain_name
"""
import re, sys 

def ParseSDI(fname, sname):
    
    sfh = open(fname, 'rU')
    del_cnt, snp_cnt, ins_cnt = 1, 1, 1
    for line in sfh:
        line = line.strip("\n\r").split('\t')
        if int(line[2]) < 0: ## deletion 
            gline = [line[0],
                    sname,
                    'del',
                    line[1], 
                    str(int(line[1]) + 1),
                    line[2],
                    '.',
                    '.',
                    'ID=DEL_' + str(del_cnt).zfill(6) + ';Type=del;RS=' + line[3] + ';SS=' + line[4]]
            del_cnt += 1
            print '\t'.join(gline)
        elif int(line[2]) == 0:
            gline = [line[0],
                    sname,
                    'snp',
                    line[1], 
                    str(int(line[1]) + 1),
                    line[2],
                    '.',
                    '.',
                    'ID=SNP_' + str(snp_cnt).zfill(6) + ';Type=snp;RS=' + line[3] + ';SS=' + line[4]]
            snp_cnt += 1
            print '\t'.join(gline)
        else:
            gline = [line[0],
                    sname,
                    'ins',
                    line[1], 
                    str(int(line[1]) + 1),
                    line[2],
                    '.',
                    '.',
                    'ID=INS_' + str(ins_cnt).zfill(6) + ';Type=ins;RS=' + line[3] + ';SS=' + line[4]]
            ins_cnt += 1
            print '\t'.join(gline)
    sfh.close()

def __main__():

    try:
        sdi_fname = sys.argv[1]
        strain_name = sys.argv[2]
    except:
        print "Incorrect argument supplied"
        print __doc__
        sys.exit(-1)

    ParseSDI(sdi_fname, strain_name)

if __name__ == "__main__":__main__()
