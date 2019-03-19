import pandas

df = pandas.read_csv('/home/rostam/Downloads/pisa2012.csv', encoding="cp1252", sep=',')
df = df[['CNT', 'ST03Q02', 'ST04Q01', 'ST20Q01', 'ST20Q02', 'ST20Q03', 'PV1MATH', 'PV2MATH',
         'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV1READ', 'PV2READ','STUDREL','TCHBEHFA',
         'PV3READ', 'PV4READ', 'PV5READ', 'PV1SCIE', 'PV2SCIE', 'PV3SCIE',
         'PV4SCIE', 'PV5SCIE', 'COBN_F', 'COBN_M', 'COBN_S','WEALTH','EXAPPLM','EXPUREM']]

df.to_csv('pisa2012_filtered.csv', index=False)
