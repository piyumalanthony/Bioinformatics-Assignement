import pandas as pd

xls = pd.read_csv('D:\Code Templates\Python Templates\Bioinformatics-Assignement\protein_tables.csv')
file_dir = "D:\Code Templates\Python Templates\Bioinformatics-Assignement\species_geneome_indexes"
for index, row in xls.iterrows():
    file_name = row['Species']
    data = {'start': [], 'end': []}
    data['start'] = [row['Start_1'], row['Start_2'], row['Start_3'], row['Start_4']]
    data['end'] = [row['End_1'], row['End_2'], row['End_3'], row['End_4']]
    df = pd.DataFrame(data, index=['ABC transporter permease', 'LysR family transcriptional regulator',
                                   'helix-turn-helix domain-containing protein',
                                   'efflux transporter outer membrane subunit'])

    df.to_csv(file_dir+'\\'+file_name+'.csv', index=True, index_label='protein')
