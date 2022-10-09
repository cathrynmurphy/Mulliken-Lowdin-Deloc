Input_file_name = input('Input file name: ')

#OUTPUT
file3_name = input('Output file name: ')
#clear output file
y = open(file3_name,'w')
y.write('')
y.close()

#####################
#READ INPUT FILE
y = open(Input_file_name,'rt')
content = y.readlines()
Group1 = ''
Group2 = ''
deloc_thresh = ''
atoms_of_int = ''
atom_thresh = ''
file_name = ''
file2_name = ''

for line in content:
    if 'FILE1' in line:
        file_name = line.replace('FILE1 = ','')
        file_name = file_name.replace('\n','')
    elif 'FILE2' in line:
        file2_name = line.replace('FILE2 = ','')
        file2_name = file2_name.replace('\n','')
#INSTEAD OF ATOMS OF INT, TWO GROUPS:
    elif 'GROUP1' in line:
        Group1 = line.replace('GROUP1 = ','')
        Group1 = Group1.replace('\n','')    
    elif 'GROUP2' in line:
        Group2 = line.replace('GROUP2 = ','')
        Group2 = Group2.replace('\n','')    
    elif 'DELOC_THRESH' in line:
        deloc_thresh = line.replace('DELOC_THRESH = ','')
        deloc_thresh = deloc_thresh.replace('\n','')    
    elif 'ATOM_THRESH' in line:
        atom_thresh = line.replace('ATOM_THRESH = ','')
        atom_thresh = atom_thresh.replace('\n','')    
    elif 'ATOMS_OF_INT' in line:
        atoms_of_int = line.replace('ATOMS_OF_INT = ','')
        atoms_of_int = atoms_of_int.replace('\n','')   
split_Group1 = Group1.split(',')
split_Group2 = Group2.split(',')
split_atoms_of_int = atoms_of_int.split(',')
#must cast each str element in list split_Group1, split_Group2 into an integer
y.close()


############
#CHECKING FOR VALIDITY OF INPUT FILE
if Group1 == '':
    print('**********************')
    print('**********************') 
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')
elif Group2 == '':
    print('**********************')
    print('**********************')
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')

elif deloc_thresh == '':
    print('**********************')
    print('**********************')
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')

elif atoms_of_int == '':
    print('**********************')
    print('**********************')
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')

elif file_name == '':
    print('**********************')
    print('**********************')    
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')

elif file2_name == '':
    print('**********************')
    print('**********************')
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')

elif atom_thresh == '':
    print('**********************')
    print('**********************')
    print('Invalid input file. Input file should include:')
    print('FILE1 = ')
    print('FILE2 = ')
    print('GROUP1 = ')
    print('GROUP2 = ')
    print('ATOMS_OF_INT = ')
    print('ATOM_THRESH = ')
    print('DELOC_THRESH = ')
    print('***********')
    print('FILE1 is the file name including the Lowdin and/or Mulliken population data for structure 1')
    print('FILE2 is the file name including the Lowdin and/or Mulliken population data for structure 2')
    print('GROUP1 is a list of atom numbers delimited by "," which constitutes delocalization group 1')
    print('GROUP2 is a list of atom numbers delimited by "," which constitutes delocalization group 2')
    print('ATOMS_OF_INT is a list of atom numbers delimited by "," which indicates which specific atom population sums should be starred')
    print('ATOM_THRESH a value from >= 0.0, <= 2.0 which indicates an individual population value of an atom within an orbital for it to be printed.')
    print('DELOC_THRESH a value from >= 0.0 which indicates an individual orbital delocalization value for it to be printed.')
    print('DELOC_THRESH, ATOMS_OF_INT, and ATOM_THRESH do not affect the overall index score.')
    print('**********************')
    print('**********************')
else:



    ####################
    #NUMBER ROWS
    y = open(file_name,'r')
    z = y.read()
    position = z.index('Partial Mulliken')

    start_position = position + 147
    y.seek(start_position,0)
    switch = 'F'
    rows = []
    while switch != '    ':
        switch = y.read(4)
        space = y.read(74)
        rows.append('#')
    no_rows = len(rows) - 1

    y.close()


    ####################
    #ORBITAL IDENTITIES

    y = open(file_name,'r')
    z = y.read()

    position = z.index('Partial Mulliken')

    start_position = position + 147
    y.seek(start_position,0)
    orb_identities = []
    for i in range(int(no_rows)):
        x = y.read(4)
        orb_identities.append(x)
        space = y.read(74)

    y.close()

    # x = no_rows
    # y = no_orbitals
    # 1*x [i, i, i, i...]
    #[[i, i, i, i...], [i, i, i, i, i...]]
    #ith item in each individual list corresponds to id i
    #if identity of b[n][i] = b[n][i+1], add together
    #if a[i] = a[i+1], add b[n][i] and b[n][i+1]

    #MULLIKEN POPULATION##################################

    ######################################################################
    ######################################################################
    # ISOMER 1


    y = open(file_name,'r')
    z = y.read()
    ORBITALNOposition = z.index('alpha and')
    position = z.index('Partial Mulliken')
    start_position2 = ORBITALNOposition + 16
    start_position = position + 158
    y.seek(start_position2,0)
    no_occ = int(y.read(2))
    y.seek(start_position,0)

    orb_data = []

    ####

    if no_occ % 6 == 0:
        orb_rows = no_occ / 6
        for i in range(int(orb_rows)):
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            pop = y.read(77)    

    elif no_occ % 6 == 1:
        orb_rows = (no_occ - 1) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(27)   
        occ_1 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)

    elif no_occ % 6 == 2:
        orb_rows = (no_occ - 2) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(37)   

        occ_1 = []
        occ_2 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)


    elif no_occ % 6 == 3:
        orb_rows = (no_occ - 3) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(47)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)


    elif no_occ % 6 == 4:
        orb_rows = (no_occ - 4) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1

            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(57)   
        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)


    elif no_occ % 6 == 5:
        orb_rows = (no_occ - 5) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(67)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        occ_5 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_5.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)
        orb_data.append(occ_5)

    condensed = []
    IDcondensed = []
    for n in range(no_occ):
        individual = []
        IDindividual = []
        for i in range(no_rows):
            element = 0
            end = no_rows - 1
            if i == 0 and orb_identities[i] == orb_identities[i+1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == 0 and orb_identities[i] != orb_identities[i+1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] != orb_identities[i-1]:
                element = float(orb_data[n][i])
                individual.append(element)
                IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] == orb_identities[i-1]:
                element = float(orb_data[n][i])
            elif orb_identities[i] == orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif orb_identities[i] != orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
        condensed.append(individual)
        if n == 0:
            IDcondensed.append(IDindividual)

    #condensed[i][n] is a list filled with smaller lists
    #each of the elements are individual populations corresponding to an atom n and an orbital i

    #################################
    #SUMMATION within orbital for SigmaA*SigmaB
    #Goal: SigmaA is a list of length no_occ with sum of populations per orbital, same for SigmaB
    SigmaA = []
    SigmaB = []

    for i in range(no_occ):
        ind_SigmaA = 0
        ind_SigmaB = 0
        for n in range(len(condensed[0])):
            number = n + 1
            number = str(number)
            if number in split_Group1:
                ind_SigmaA = condensed[i][n] + ind_SigmaA
            elif number in split_Group2:
                ind_SigmaB = condensed[i][n] + ind_SigmaB
        SigmaA.append(ind_SigmaA)
        SigmaB.append(ind_SigmaB)
    SigmaProd = []
    for i in range(len(SigmaA)):
        SigmaMult = SigmaA[i]*SigmaB[i]
        SigmaProd.append(SigmaMult)
    ###################################
    #Singular delocalization value for whole structure between Group A and Group B

    SigmaProdSum = 0
    for i in SigmaProd:
        SigmaProdSum = SigmaProdSum + i
        
    ########################################################
    #Printing relevant delocalized orbitals

    deloc_orbs = []
    deloc_atoms = []
    for i in range(len(SigmaProd)):
        if SigmaProd[i] > float(deloc_thresh):
            i_no = i + 1
            deloc_orbs.append(i_no)
            deloc_atoms_ind = ['#{}#:'.format(i_no)]
            for n in range(len(IDcondensed[0])):
                if condensed[i][n] > float(atom_thresh):
                    number = n + 1
                    number = str(number)
                    if number in split_atoms_of_int:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append('**{}**'.format(item_trim))
                    else:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append(item_trim)
            deloc_atoms.append(deloc_atoms_ind)

    y.close()

    ####################################
    ####################################
    #WRITING THE OUTPUT FILE

    y = open(Input_file_name,'r')
    inputfile_read = y.read()
    y.close()

    y = open(file3_name,'a')

    y.write('***************************\n')
    y.write('*       ***INPUT***       *')
    y.write('\n***************************\n\n')
    y.write(inputfile_read)

    y.write('\n\n****************************\n')
    y.write('*       ***OUTPUT***       *\n')
    y.write('****************************\n\n')

    y.write('### MULLIKEN POPULATIONS ###\n\n')
    y.write('# Delocalized Orbitals: Isomer 1 #\n')
    y.write('The following orbitals meet the indicated delocalization threshold of {}\n'.format(deloc_thresh))
    y.write('For each orbital the atoms are listed which meet the indicated atomic population threshold of {}\n'.format(atom_thresh))
    y.write('Atoms of indicated interest are **starred**\n\n')

    for i in range(len(deloc_atoms)):
        no = deloc_atoms[i][0]
        no = no.replace('#','')
        no = no.replace(':','')
        no = int(no)
        no = no - 1
        for n in deloc_atoms[i]:
            y.write(n)
            if n != deloc_atoms[i][0]:
                y.write(', ')
            else:
                y.write(' ')
        y.write('   Deloc Value: {}'.format(SigmaProd[no]))
        y.write('\n')
    y.write('\n')
    y.write('The total summed Mulliken delocalization value between Group A and Group B for isomer 1 is: {}'.format(SigmaProdSum))

    y.close()

    ####################################################################
    ####################################################################
    ## ISOMER 2 


    y = open(file2_name,'r')
    z = y.read()
    ORBITALNOposition = z.index('alpha and')
    position = z.index('Partial Mulliken')
    start_position2 = ORBITALNOposition + 16
    start_position = position + 158
    y.seek(start_position2,0)
    no_occ = int(y.read(2))
    y.seek(start_position,0)

    orb_data = []

    ####

    if no_occ % 6 == 0:
        orb_rows = no_occ / 6
        for i in range(int(orb_rows)):
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            pop = y.read(77)    

    elif no_occ % 6 == 1:
        orb_rows = (no_occ - 1) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(27)   
        occ_1 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)

    elif no_occ % 6 == 2:
        orb_rows = (no_occ - 2) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(37)   

        occ_1 = []
        occ_2 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)


    elif no_occ % 6 == 3:
        orb_rows = (no_occ - 3) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(47)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)


    elif no_occ % 6 == 4:
        orb_rows = (no_occ - 4) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1

            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(57)   
        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)


    elif no_occ % 6 == 5:
        orb_rows = (no_occ - 5) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(67)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        occ_5 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_5.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)
        orb_data.append(occ_5)

    condensed = []
    IDcondensed = []
    for n in range(no_occ):
        individual = []
        IDindividual = []
        for i in range(no_rows):
            element = 0
            end = no_rows - 1
            if i == 0 and orb_identities[i] == orb_identities[i+1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == 0 and orb_identities[i] != orb_identities[i+1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] != orb_identities[i-1]:
                element = float(orb_data[n][i])
                individual.append(element)
                IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] == orb_identities[i-1]:
                element = float(orb_data[n][i])
            elif orb_identities[i] == orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif orb_identities[i] != orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
        condensed.append(individual)
        if n == 0:
            IDcondensed.append(IDindividual)

    #condensed[i][n] is a list filled with smaller lists
    #each of the elements are individual populations corresponding to an atom n and an orbital i

    #################################
    #SUMMATION within orbital for SigmaA*SigmaB
    #Goal: SigmaA is a list of length no_occ with sum of populations per orbital, same for SigmaB
    SigmaA = []
    SigmaB = []

    for i in range(no_occ):
        ind_SigmaA = 0
        ind_SigmaB = 0
        for n in range(len(condensed[0])):
            number = n + 1
            number = str(number)
            if number in split_Group1:
                ind_SigmaA = condensed[i][n] + ind_SigmaA
            elif number in split_Group2:
                ind_SigmaB = condensed[i][n] + ind_SigmaB
        SigmaA.append(ind_SigmaA)
        SigmaB.append(ind_SigmaB)
    SigmaProd = []
    for i in range(len(SigmaA)):
        SigmaMult = SigmaA[i]*SigmaB[i]
        SigmaProd.append(SigmaMult)
    ###################################
    #Singular delocalization value for whole structure between Group A and Group B

    SigmaProdSum2 = 0
    for i in SigmaProd:
        SigmaProdSum2 = SigmaProdSum2 + i

    ########################################################
    #Printing relevant delocalized orbitals

    deloc_orbs = []
    deloc_atoms = []
    for i in range(len(SigmaProd)):
        if SigmaProd[i] > float(deloc_thresh):
            i_no = i + 1
            deloc_orbs.append(i_no)
            deloc_atoms_ind = ['#{}#:'.format(i_no)]
            for n in range(len(IDcondensed[0])):
                if condensed[i][n] > float(atom_thresh):
                    number = n + 1
                    number = str(number)
                    if number in split_atoms_of_int:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append('**{}**'.format(item_trim))
                    else:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append(item_trim)
            deloc_atoms.append(deloc_atoms_ind)

    y.close()

    ####################################
    ####################################
    #WRITING THE OUTPUT FILE

    y = open(file3_name,'a')

    y.write('\n\n\n')
    y.write('# Delocalized Orbitals: Isomer 2 #\n')
    y.write('The following orbitals meet the indicated delocalization threshold of {}\n'.format(deloc_thresh))
    y.write('For each orbital the atoms are listed which meet the indicated atomic population threshold of {}\n'.format(atom_thresh))
    y.write('Atoms of indicated interest are **starred**\n\n')

    for i in range(len(deloc_atoms)):
        no = deloc_atoms[i][0]
        no = no.replace('#','')
        no = no.replace(':','')
        no = int(no)
        no = no - 1
        for n in deloc_atoms[i]:
            y.write(n)
            if n != deloc_atoms[i][0]:
                y.write(', ')
            else:
                y.write(' ')
        y.write('   Deloc Value: {}'.format(SigmaProd[no]))
        y.write('\n')
    y.write('\n')
    y.write('The total summed Mulliken delocalization value between Group A and Group B for isomer 2 is: {}'.format(SigmaProdSum2))

    #######################
    #COMPARE THE TWO SIGMA PROD SUMS

    DifSigmaProdSum = SigmaProdSum - SigmaProdSum2

    y.write('\n\nThe difference in total summed Mulliken delocalization values between the two isomers is: {}'.format(DifSigmaProdSum))

    y.close()


    ###############################################################################
    ###############################################################################
    ###############################################################################
    # LOWDIN POPULATIONS


    #MULLIKEN POPULATION##################################

    ######################################################################
    ######################################################################
    # ISOMER 1


    y = open(file_name,'r')
    z = y.read()
    ORBITALNOposition = z.index('alpha and')
    position = z.index('Partial Lowdin')
    start_position2 = ORBITALNOposition + 16
    start_position = position + 158
    y.seek(start_position2,0)
    no_occ = int(y.read(2))
    y.seek(start_position,0)

    orb_data = []

    ####

    if no_occ % 6 == 0:
        orb_rows = no_occ / 6
        for i in range(int(orb_rows)):
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            pop = y.read(77)    

    elif no_occ % 6 == 1:
        orb_rows = (no_occ - 1) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(27)   
        occ_1 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)

    elif no_occ % 6 == 2:
        orb_rows = (no_occ - 2) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(37)   

        occ_1 = []
        occ_2 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)


    elif no_occ % 6 == 3:
        orb_rows = (no_occ - 3) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(47)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)


    elif no_occ % 6 == 4:
        orb_rows = (no_occ - 4) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1

            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(57)   
        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)


    elif no_occ % 6 == 5:
        orb_rows = (no_occ - 5) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(67)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        occ_5 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)


            pop = y.read(8)
            popstrip = pop.strip()
            occ_5.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)
        orb_data.append(occ_5)

    condensed = []
    IDcondensed = []
    for n in range(no_occ):
        individual = []
        IDindividual = []
        for i in range(no_rows):
            element = 0
            end = no_rows - 1
            if i == 0 and orb_identities[i] == orb_identities[i+1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == 0 and orb_identities[i] != orb_identities[i+1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] != orb_identities[i-1]:
                element = float(orb_data[n][i])
                individual.append(element)
                IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] == orb_identities[i-1]:
                element = float(orb_data[n][i])
            elif orb_identities[i] == orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif orb_identities[i] != orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
        condensed.append(individual)
        if n == 0:
            IDcondensed.append(IDindividual)

    #condensed[i][n] is a list filled with smaller lists
    #each of the elements are individual populations corresponding to an atom n and an orbital i

    #################################
    #SUMMATION within orbital for SigmaA*SigmaB
    #Goal: SigmaA is a list of length no_occ with sum of populations per orbital, same for SigmaB
    SigmaA = []
    SigmaB = []

    for i in range(no_occ):
        ind_SigmaA = 0
        ind_SigmaB = 0
        for n in range(len(condensed[0])):
            number = n + 1
            number = str(number)
            if number in split_Group1:
                ind_SigmaA = condensed[i][n] + ind_SigmaA
            elif number in split_Group2:
                ind_SigmaB = condensed[i][n] + ind_SigmaB
        SigmaA.append(ind_SigmaA)
        SigmaB.append(ind_SigmaB)
    SigmaProd = []
    for i in range(len(SigmaA)):
        SigmaMult = SigmaA[i]*SigmaB[i]
        SigmaProd.append(SigmaMult)
    ###################################
    #Singular delocalization value for whole structure between Group A and Group B

    SigmaProdSum = 0
    for i in SigmaProd:
        SigmaProdSum = SigmaProdSum + i

    ########################################################
    #Printing relevant delocalized orbitals

    deloc_orbs = []
    deloc_atoms = []
    for i in range(len(SigmaProd)):
        if SigmaProd[i] > float(deloc_thresh):
            i_no = i + 1
            deloc_orbs.append(i_no)
            deloc_atoms_ind = ['#{}#:'.format(i_no)]
            for n in range(len(IDcondensed[0])):
                if condensed[i][n] > float(atom_thresh):
                    number = n + 1
                    number = str(number)
                    if number in split_atoms_of_int:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append('**{}**'.format(item_trim))
                    else:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append(item_trim)
            deloc_atoms.append(deloc_atoms_ind)

    y.close()

    ####################################
    ####################################
    #WRITING THE OUTPUT FILE

    y = open(file3_name,'a')
    y.write('\n\n\n#######################################\n')
    y.write('#######################################\n\n')
    y.write('\n### LOWDIN POPULATIONS ###\n\n')
    y.write('# Delocalized Orbitals: Isomer 1 #\n')
    y.write('The following orbitals meet the indicated delocalization threshold of {}\n'.format(deloc_thresh))
    y.write('For each orbital the atoms are listed which meet the indicated atomic population threshold of {}\n'.format(atom_thresh))
    y.write('Atoms of indicated interest are **starred**\n\n')

    for i in range(len(deloc_atoms)):
        no = deloc_atoms[i][0]
        no = no.replace('#','')
        no = no.replace(':','')
        no = int(no)
        no = no - 1
        for n in deloc_atoms[i]:
            y.write(n)
            if n != deloc_atoms[i][0]:
                y.write(', ')
            else:
                y.write(' ')
        y.write('   Deloc Value: {}'.format(SigmaProd[no]))
        y.write('\n')
    y.write('\n')
    y.write('The total summed Lowdin delocalization value between Group A and Group B for isomer 1 is: {}'.format(SigmaProdSum))

    y.close()

    ####################################################################
    ####################################################################
    ## ISOMER 2 


    y = open(file2_name,'r')
    z = y.read()
    ORBITALNOposition = z.index('alpha and')
    position = z.index('Partial Lowdin')
    start_position2 = ORBITALNOposition + 16
    start_position = position + 158
    y.seek(start_position2,0)
    no_occ = int(y.read(2))
    y.seek(start_position,0)

    orb_data = []

    ####

    if no_occ % 6 == 0:
        orb_rows = no_occ / 6
        for i in range(int(orb_rows)):
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            pop = y.read(77)    

    elif no_occ % 6 == 1:
        orb_rows = (no_occ - 1) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(27)   
        occ_1 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)

    elif no_occ % 6 == 2:
        orb_rows = (no_occ - 2) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(37)   

        occ_1 = []
        occ_2 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)


    elif no_occ % 6 == 3:
        orb_rows = (no_occ - 3) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(47)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)


    elif no_occ % 6 == 4:
        orb_rows = (no_occ - 4) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1

            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(57)   
        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)


    elif no_occ % 6 == 5:
        orb_rows = (no_occ - 5) / 6
        for i in range(int(orb_rows)):
            no_i = i + 1
            
            occ_1 = []
            occ_2 = []
            occ_3 = []
            occ_4 = []
            occ_5 = []
            occ_6 = []
            for i in range(int(no_rows)):
                pop = y.read(8)
                popstrip = pop.strip()
                occ_1.append(popstrip)
                space = y.read(2)
                    
                pop = y.read(8)
                popstrip = pop.strip()
                occ_2.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_3.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_4.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_5.append(popstrip)
                space = y.read(2)

                pop = y.read(8)
                popstrip = pop.strip()
                occ_6.append(popstrip)
                space = y.read(2)

                pop = y.read(18)
            orb_data.append(occ_1)
            orb_data.append(occ_2)
            orb_data.append(occ_3)
            orb_data.append(occ_4)
            orb_data.append(occ_5)
            orb_data.append(occ_6)
            if no_i != int(orb_rows):
                pop = y.read(77) 
            else:
                pop = y.read(67)   

        occ_1 = []
        occ_2 = []
        occ_3 = []
        occ_4 = []
        occ_5 = []
        for i in range(int(no_rows)):
            pop = y.read(8)
            popstrip = pop.strip()
            occ_1.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_2.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_3.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_4.append(popstrip)
            space = y.read(2)

            pop = y.read(8)
            popstrip = pop.strip()
            occ_5.append(popstrip)
            space = y.read(2)

            pop = y.read(18)
        orb_data.append(occ_1)   
        orb_data.append(occ_2)
        orb_data.append(occ_3)
        orb_data.append(occ_4)
        orb_data.append(occ_5)

    condensed = []
    IDcondensed = []
    for n in range(no_occ):
        individual = []
        IDindividual = []
        for i in range(no_rows):
            element = 0
            end = no_rows - 1
            if i == 0 and orb_identities[i] == orb_identities[i+1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == 0 and orb_identities[i] != orb_identities[i+1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] != orb_identities[i-1]:
                element = float(orb_data[n][i])
                individual.append(element)
                IDindividual.append(orb_identities[i])
            elif i == end and orb_identities[i] == orb_identities[i-1]:
                element = float(orb_data[n][i])
            elif orb_identities[i] == orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i]) + float(orb_data[n][i+1]) + float(orb_data[n][i+2])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
            elif orb_identities[i] != orb_identities[i+1] and orb_identities[i] != orb_identities[i-1]:
                    element = float(orb_data[n][i])
                    individual.append(element)
                    IDindividual.append(orb_identities[i])
        condensed.append(individual)
        if n == 0:
            IDcondensed.append(IDindividual)

    #condensed[i][n] is a list filled with smaller lists
    #each of the elements are individual populations corresponding to an atom n and an orbital i

    #################################
    #SUMMATION within orbital for SigmaA*SigmaB
    #Goal: SigmaA is a list of length no_occ with sum of populations per orbital, same for SigmaB
    SigmaA = []
    SigmaB = []

    for i in range(no_occ):
        ind_SigmaA = 0
        ind_SigmaB = 0
        for n in range(len(condensed[0])):
            number = n + 1
            number = str(number)
            if number in split_Group1:
                ind_SigmaA = condensed[i][n] + ind_SigmaA
            elif number in split_Group2:
                ind_SigmaB = condensed[i][n] + ind_SigmaB
        SigmaA.append(ind_SigmaA)
        SigmaB.append(ind_SigmaB)
    SigmaProd = []
    for i in range(len(SigmaA)):
        SigmaMult = SigmaA[i]*SigmaB[i]
        SigmaProd.append(SigmaMult)
    ###################################
    #Singular delocalization value for whole structure between Group A and Group B

    SigmaProdSum2 = 0
    for i in SigmaProd:
        SigmaProdSum2 = SigmaProdSum2 + i

    ########################################################
    #Printing relevant delocalized orbitals

    deloc_orbs = []
    deloc_atoms = []
    for i in range(len(SigmaProd)):
        if SigmaProd[i] > float(deloc_thresh):
            i_no = i + 1
            deloc_orbs.append(i_no)
            deloc_atoms_ind = ['#{}#:'.format(i_no)]
            for n in range(len(IDcondensed[0])):
                if condensed[i][n] > float(atom_thresh):
                    number = n + 1
                    number = str(number)
                    if number in split_atoms_of_int:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append('**{}**'.format(item_trim))
                    else:
                        item = IDcondensed[0][n]
                        item_trim = item.strip()
                        deloc_atoms_ind.append(item_trim)
            deloc_atoms.append(deloc_atoms_ind)

    y.close()

    ####################################
    ####################################
    #WRITING THE OUTPUT FILE

    y = open(file3_name,'a')

    y.write('\n\n\n')
    y.write('# Delocalized Orbitals: Isomer 2 #\n')
    y.write('The following orbitals meet the indicated delocalization threshold of {}\n'.format(deloc_thresh))
    y.write('For each orbital the atoms are listed which meet the indicated atomic population threshold of {}\n'.format(atom_thresh))
    y.write('Atoms of indicated interest are **starred**\n\n')

    for i in range(len(deloc_atoms)):
        no = deloc_atoms[i][0]
        no = no.replace('#','')
        no = no.replace(':','')
        no = int(no)
        no = no - 1
        for n in deloc_atoms[i]:
            y.write(n)
            if n != deloc_atoms[i][0]:
                y.write(', ')
            else:
                y.write(' ')
        y.write('   Deloc Value: {}'.format(SigmaProd[no]))
        y.write('\n')
    y.write('\n')
    y.write('The total summed Lowdin delocalization value between Group A and Group B for isomer 2 is: {}'.format(SigmaProdSum2))

    #######################
    #COMPARE THE TWO SIGMA PROD SUMS

    DifSigmaProdSum = SigmaProdSum - SigmaProdSum2

    y.write('\n\nThe difference in total summed Lowdin delocalization values between the two isomers is: {}'.format(DifSigmaProdSum))

    y.close()