# Read the information
with open('info_hb', 'r') as file:
     info = [line.strip().split(":")[1] for line in file.readlines()]
res_aa = info[0]
res_num = int(info[1])
lig_name = info[2]
lig_num = int(info[3])
atom_ligand = info[4]
chrg_ligand = int(info[5])
pKa = info[6]
pKb = info[7]
logP = info[8]
ligand = info[9]

# Initialize empty lists to store the information
atom_num = []
atom_type = []
residue_type = []
chain = []
residue_num = []
x = []
y = []
z = []

# Read the "input.pdb" file line by line
with open('input.pdb', 'r') as file:
    for line in file:
        # Check if the line starts with "ATOM" or "HETATM" and skip lines with residue names "HOH" or "DOD"
        if (line.startswith('ATOM') or line.startswith('HETATM')) and not line[17:20].strip() in ['HOH', 'DOD']:
            # Extract information from columns
            atom_num.append(int(line[6:11].strip()))
            atom_type.append(line[12:16].strip())
            residue_type.append(line[17:20].strip())
            chain.append(line[21].strip())
            residue_num.append(int(line[22:26].strip()))
            x.append(float(line[30:38].strip()))
            y.append(float(line[38:46].strip()))
            z.append(float(line[46:54].strip()))

# Get the sequence information
for index in range(len(atom_num)):
    if residue_num[index] == res_num - 3:
       res_aa_n3 = residue_type[index]
    if residue_num[index] == res_num - 2:
       res_aa_n2 = residue_type[index]
    if residue_num[index] == res_num - 1:
       res_aa_n1 = residue_type[index]
    if residue_num[index] == res_num + 1:
       res_aa_1 = residue_type[index]
    if residue_num[index] == res_num + 2:
       res_aa_2 = residue_type[index]
    if residue_num[index] == res_num + 3:
       res_aa_3 = residue_type[index]

atom = []
atom_aa = []
chrg_aa = []
for index in range(len(atom_num)):
  if residue_num[index] == lig_num and residue_type[index] == lig_name and atom_type[index] == atom_ligand:
    coord = [x[index], y[index], z[index]]
    coord_lig = np.array(coord)
  if residue_num[index] == res_num:
    if res_aa == 'TYR' and atom_type[index] == 'OH':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(0)
    if res_aa == 'TRP' and atom_type[index] == 'NE1':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'THR' and atom_type[index] == 'OG1':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(0)
    if res_aa == 'SER' and atom_type[index] == 'OG':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(0)
    if res_aa == 'LYS' and atom_type[index] == 'NZ':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(1)
    if res_aa == 'GLU' and atom_type[index] == 'OE1':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(-1)
    if res_aa == 'GLU' and atom_type[index] == 'OE2':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(-1)
    if res_aa == 'ASP' and atom_type[index] == 'OD1':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(-1)
    if res_aa == 'ASP' and atom_type[index] == 'OD2':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(-1)
    if res_aa == 'ARG' and atom_type[index] == 'NE':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(1)
    if res_aa == 'ARG' and atom_type[index] == 'NH1':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(1)
    if res_aa == 'ARG' and atom_type[index] == 'NH2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(1)
    if res_aa == 'GLN' and atom_type[index] == 'OE1':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(0)
    if res_aa == 'GLN' and atom_type[index] == 'NE2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'ALN' and atom_type[index] == 'OD1':
      atom.append(index)
      atom_aa.append('O')
      chrg_aa.append(0)
    if res_aa == 'ALN' and atom_type[index] == 'ND2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HIS' and atom_type[index] == 'ND1':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HIS' and atom_type[index] == 'NE2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HID' and atom_type[index] == 'ND1':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HID' and atom_type[index] == 'NE2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HIE' and atom_type[index] == 'ND1':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HIE' and atom_type[index] == 'NE2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(0)
    if res_aa == 'HIP' and atom_type[index] == 'ND1':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(1)
    if res_aa == 'HIP' and atom_type[index] == 'NE2':
      atom.append(index)
      atom_aa.append('N')
      chrg_aa.append(1)

distances = []
count = 0
dist_min = 999.9
n_min = -1
with open('temp', 'w') as output:
    for index in range(len(atom)):
        coord_aa = [x[atom[index]], y[atom[index]], z[atom[index]]]
        coord_aa = np.array(coord_aa)
        distance = np.linalg.norm(coord_lig - coord_aa)
        distances.append(distance)
        if distance <= 3.2:
            output.write("{:3} {:1} {:4} {:2d} {:2d} {:3} {:3} {:3} {:3} {:3} {:3} {:6.2f} {:6.2f} {:6.2f} {:1} {:4d} {:3} {:4} {:4d} {:6.4f}\n".format(res_aa, atom_aa[index], ligand, chrg_aa[index], chrg_ligand, res_aa_n3, res_aa_n2, res_aa_n1, res_aa_1, res_aa_2, res_aa_3, pKa, pKb, logP, atom_aa[index], res_num, lig_name, atom_ligand, lig_num, distance))
            count += 1
        if distance <= dist_min:
            dist_min = distance
            n_min = index
    if count == 0:
       output.write("{:3} {:1} {:4} {:2d} {:2d} {:3} {:3} {:3} {:3} {:3} {:3} {:6.2f} {:6.2f} {:6.2f} {:1} {:4d} {:3} {:4} {:4d} {:6.4f}\n".format(res_aa, atom_aa[n_min], ligand, chrg_aa[n_min], chrg_ligand, res_aa_n3, res_aa_n2, res_aa_n1, res_aa_1, res_aa_2, res_aa_3, pKa, pKb, logP, atom_aa[n_min], res_num, lig_name, atom_ligand, lig_num, distance))
