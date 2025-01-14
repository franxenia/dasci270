df = df.drop(columns = ['A_id'])
df = df.dropna(axis=0)
df.loc[df['Quality'] == 'good', 'Quality'] = 1
df.loc[df['Quality'] == 'bad', 'Quality'] = 0