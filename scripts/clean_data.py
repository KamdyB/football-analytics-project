#import pandas to read and manipulate data
import pandas as pd
df = pd.read_csv('data/raw_championship_passing.csv', header=[0, 1])

#a loop to clean the 2 column headers into one
cleaned_columns = []
current_header = ''
for col in df.columns:
    if col[0].startswith('Unnamed'):
        if current_header != '':
            col = current_header + '_' + col[1]
        else:
            col = col[1]
    else:
        current_header = col[0]
        col = current_header + '_' + col[1]
    cleaned_columns.append(col)
df.columns = cleaned_columns

#print the columns
print(df.columns)

#inspect the first 5 rows of data and see the overall scope 
print(df.head())
print(df.shape)



#look for the missing values
print(df.isnull().sum())

#look for important information and columns only
print(df.info())

#drop any duplicates
df = df.drop_duplicates()

#remove missing values
df = df.dropna(subset=['Player'])

#sql optimisation
df.columns = [col.strip().replace('%', '_pct').replace(' ', '_').replace('G+A-PK', 'G_and_A_nonPK').replace('G+A', 'G_and_A').replace('G-PK', 'G_nonPK') for col in df.columns]
print(df.head())

#change minutes data type from tring to integer
df['Playing_Time_Min'] = (df['Playing_Time_Min'].str.replace(',', '').astype(int))

#change age and born data types from float to integer (this is because of the missing values)
df['Age'] = df['Age'].astype('Int64')
df['Born'] = df['Born'].astype('Int64')

#drop matches column
print(df['Per_90_Minutes_Matches'].head())
df = df.drop(columns=['Per_90_Minutes_Matches'])

df.to_csv('data/cleaned_fbref.csv', index=False)
print('Cleaned dataset saved successfully!')
