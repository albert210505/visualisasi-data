import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)

print("Dataframe awal :")
print(df)


df_prefix = df.add_prefix('kolom_')
print("DataFrame dengan prefix:")
print(df_prefix)


df_suffix = df.add_suffix('_field')
print("DataFrame dengan suffix:")
print(df_suffix)