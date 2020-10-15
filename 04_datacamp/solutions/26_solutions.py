df_referendum['Department code'] = df_referendum['Department code'].apply(
    lambda x: '0' + x if len(x) == 1 else x
)
df_referendum.head()
