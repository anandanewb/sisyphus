import pandas as pd
import numpy as np

g = np.random.default_rng(0)
scores = g.integers(40,60,10)
df = pd.DataFrame({'scores' : scores})
mean_score = df.scores.mean()
std = df.scores.std()



grade_boundaries = {
    'F' : 0,
    'D' : mean_score - (2 * std),
    'C' : mean_score - std,
    'B' : mean_score,
    'A' : mean_score + std,
    
}

#df['Grades'] = pd.cut(df.scores, bins=list(grade_boundaries.values()), labels=list(grade_boundaries.keys()), include_lowest=True)

# use pandas cut to assign grades based on score boundaries
df['Grades'] = pd.cut(df.scores, bins=list(grade_boundaries.values()), labels=list(grade_boundaries.keys()), include_lowest=True)
