import MDAnalysis as mda
import numpy as np
import csv

x = mda.Universe('stripped.wt_801.prmtop', 'ligamd_strip.nc')

protein = x.select_atoms('protein')     
ligand = x.select_atoms('resname UNK')  

cutoff = 6.0

contact = np.zeros(len(protein.residues))

for ts in x.trajectory[:125000]:
    contacted_residues = set()  
    
    for residue in protein.residues:
        if any(mda.lib.distances.calc_bonds(atom.position, atom_l.position) < cutoff for atom in residue.atoms for atom_l in ligand):
            contacted_residues.add(residue.resnum) 
            
    for resnum in contacted_residues:  
        contact[resnum-1] += 1

total_contact = np.sum(contact)

with open('MD_cnt_801_d1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Protein Residue', 'MD Contact'])
    for i, cnt in enumerate(contact):
        writer.writerow([protein.residues[i].resnum, cnt])
    writer.writerow(['Total_contact', total_contact])


