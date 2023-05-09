df = df_referendum.merge(df_reg_dep, how='inner', left_on='Department code', right_on='code_x')
df.head()
