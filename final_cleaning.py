import pandas as pd
import pycountry_convert

cnt = pycountry_convert.map_country_alpha3_to_country_name()

df = pd.read_csv('pisa2012_filtered_clean.csv')
df.rename({'CNT': 'Country Code', 'ST03Q02': 'Birth Year', 'ST04Q01': 'Gender',
           'STUDREL': 'Teacher Student Relations', 'TCHBEHFA': 'Teacher Behavior',
           'COBN_S': 'Birth Country', 'COBN_M': 'Birth Country of Mother',
           'COBN_F': 'Birth Country of Father',
           'EXAPPLM': 'Experience with Applied Math in School',
           'EXPUREM': 'Experience with Pure Math in School',
           'avg Science Score': 'Average Science Score',
           'Avg Math Score': 'Average Math Score',
           'Avg Reading Score': 'Average Reading Score',
           'WEALTH': 'Wealth'}, axis='columns', inplace=True)


df = df.drop(columns=['Max Math Score', 'Max Reading Score', 'Max Science Score'])


def correct_country_names(country):
    country = country.strip()
    lower_country = country.lower()
    if country.find('United Kingdom') != -1:
        return 'UK'
    elif lower_country.find('another country (') != -1:
        if country[17:20] == 'QUK':
            return 'Unknown'
        if country[17:20] == 'QSC':
            return 'Unknown'
        if country[17:20] == 'QCN':
            return 'China'
        if country[17:20] == 'TAP':
            return 'Unknown'
        return cnt[country[17:20]]
    elif country.find('Another American country [URY]') != -1:
        return 'Uruguay'
    elif country.find('Another country within the European Union (ITA)') != -1:
        return 'Italy'
    elif country.find('Another province in mainland China (QCN)') != -1:
        return 'China'
    elif country.find('ESP') != -1:
        return 'Spain'
    elif country.find('United States') != -1:
        return 'USA'
    elif country.find('United States of America') != -1:
        return 'USA'
    elif country.find('PRT') != -1:
        return 'Portugal'
    elif country.find('ARE') != -1:
        return cnt['ARE']
    elif country.find('An Eastern European country') != -1:
        return 'Unknown'
    elif country.find('A European country') != -1:
        return 'Unknown'
    elif country.find('An Eastern European country outside the EU') != -1:
        return 'Unknown'
    elif country.find('A Sub-Saharan country (Africa excl. Maghreb)') != -1:
        return 'Unknown'
    elif country.find('Serbia, Montenegro and Kosovo') != -1:
        return 'Serbia'
    elif country.find('Slovak Republic') != -1:
        return 'Slovakia'
    elif country.find('South, Latin  and Central America') != -1:
        return 'Unknown'
    elif country.find('African country with Portuguese as the official') != -1:
        return 'Unknown'
    elif country.find('LUX') != -1:
        return cnt['LUX']
    elif country.find('QSC') != -1:
        return 'Unknown'
    elif country.find('NLD') != -1:
        return 'Unknown'
    elif country.find('Middle Eastern country') != -1:
        return 'Unknown'
    elif country.find('Hong Kong, Macau') != -1:
        return 'China'
    elif country.find('Macao') != -1:
        return 'China'
    elif country.find('Hong Kong') != -1:
        return 'China'
    elif country.find('Invalid') != -1:
        return 'Unknown'
    else:
        if country.find('China') != -1:
            return 'China'
        if country.find('United States') != -1:
            return 'USA'
        if len(country) > 30:
            return 'Unknown'
        if country == 'Africa':
            return 'Unknown'
        if country == 'Czechia':
            return 'Czech Republic'
        if country == 'Hong Kong':
            return 'China'
        if country == 'Missing':
            return 'Unknown'
        if country == 'Chinese Taipei':
            return 'Taiwan'
        if country == 'United Arab Emirates':
            return 'UAE'
        if country == 'Russian Federation':
            return 'Russia'
        if country == 'Republic of Korea':
            return 'Korea'
        if country == 'Occupied Palestinian Territory':
            return 'Unknown'
        if country == 'Iran, Islamic Republic of':
            return 'Unknown'
        if country == 'Netherlands Antilles':
            return 'Antilles'
        return country


df['Birth Country'] = df['Birth Country'].apply(correct_country_names)
df['Birth Country of Mother'] = df['Birth Country of Mother'].apply(correct_country_names)
df['Birth Country of Father'] = df['Birth Country of Father'].apply(correct_country_names)

df = df.replace(['Connecticut (USA)', 'Florida (USA)', 'Massachusetts (USA)', 'United States of America'], 'USA')
df = df.replace(['Perm(Russian)', 'Russian Federation', 'Perm(Russian Federation)'], 'Russia')
df = df.replace('United Kingdom', 'UK')
df = df.replace('United Arab Emirates', 'UAE')
df = df.replace(['Hong Kong-China', 'China-Shanghai'], 'China')
df = df.replace('Chinese Taipei', 'Taiwan')
df = df.replace('United States', 'USA')
df = df.replace('Korea, Republic of', 'Korea')
df = df.replace('Czechia', 'Czech')
df = df.replace('Czech Republic', 'Czech')
df = df.replace('Hong Kong', 'China')
df = df.replace('Macao-China', 'China')
df = df.replace('Slovak Republic', 'Slovakia')
df = df.replace('Macao', 'China')
df = df.replace('Bosnia and Herzegovina', 'Bosnia')
# print(df.groupby('Birth Country').count())
# df.info()
df.to_csv('pisa_data_clean.csv')
