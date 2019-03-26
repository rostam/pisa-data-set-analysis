import pandas

df = pandas.read_csv('/home/rostam/Downloads/pisa2012.csv', encoding="cp1252", sep=',')
df = df[['CNT', 'ST03Q02', 'ST04Q01', 'PV1MATH', 'PV2MATH',
         'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV1READ', 'PV2READ', 'STUDREL', 'TCHBEHFA',
         'PV3READ', 'PV4READ', 'PV5READ', 'PV1SCIE', 'PV2SCIE', 'PV3SCIE',
         'PV4SCIE', 'PV5SCIE', 'COBN_F', 'COBN_M', 'COBN_S', 'WEALTH', 'EXAPPLM', 'EXPUREM']]

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['Avg Math Score'] = (df['PV1MATH'] + df['PV2MATH'] + df['PV3MATH'] + df['PV4MATH'] + df['PV5MATH']) / 5
df['Avg Reading Score'] = (df['PV1READ'] + df['PV2READ'] + df['PV3READ'] + df['PV4READ'] + df['PV5READ']) / 5
df['avg Science Score'] = (df['PV1SCIE'] + df['PV2SCIE'] + df['PV3SCIE'] + df['PV4SCIE'] + df['PV5SCIE']) / 5


df['Max Math Score'] = df[['PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH']].max(axis=1)
df['Max Reading Score'] = df[['PV1READ', 'PV2READ', 'PV3READ', 'PV4READ', 'PV5READ']].max(axis=1)
df['Max Science Score'] = df[['PV1SCIE', 'PV2SCIE', 'PV3SCIE', 'PV4SCIE', 'PV5SCIE']].max(axis=1)

df.drop(columns=['PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV1READ', 'PV2READ', 'PV3READ', 'PV4READ',
                 'PV5READ', 'PV1SCIE', 'PV2SCIE', 'PV3SCIE', 'PV4SCIE', 'PV5SCIE'], inplace=True)

df.to_csv('pisa2012_filtered_clean.csv', index=False)
