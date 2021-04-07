import pandas as pd

xls = pd.read_csv('/home/lahiru/Projects/sem8/Bioinfomatics/GoogleDrive/Assignment Phylogeny/Bioinformatics-Assignement/protein_tables.csv')
file_dir = "/home/lahiru/Projects/sem8/Bioinfomatics/GoogleDrive/Assignment Phylogeny/Bioinformatics-Assignement/species_geneome_indexes"
for index, row in xls.iterrows():
    file_name = row['Species']
    data = {'start': [], 'stop': []}
    data['start'] = [row['Start_1'], row['Start_2'], row['Start_3'], row['Start_4']]
    data['stop'] = [row['End_1'], row['End_2'], row['End_3'], row['End_4']]
    df = pd.DataFrame(data, index=['helix-turn-helix transcriptional regulator', 'LysR family transcriptional regulator',
                                   'helix-turn-helix domain-containing protein',
                                   'efflux transporter outer membrane subunit'])

    df.to_csv(file_dir+'//'+file_name+'.csv', index=True, index_label='gene')
