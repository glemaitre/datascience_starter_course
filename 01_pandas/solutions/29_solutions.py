df_reg_dep = df_departments.merge(df_regions, how='inner', left_on='region_code', right_on='code')
df_reg_dep.head()
