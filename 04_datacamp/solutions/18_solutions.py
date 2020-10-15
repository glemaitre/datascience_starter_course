df.groupby(['Pclass', 'Sex'])['Survived'].mean().to_frame()
