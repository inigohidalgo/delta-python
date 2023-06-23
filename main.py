#%%
from deltalake import DeltaTable
import duckdb
import polars as pl

table_path = "data/delta/sample_dataset"

#%%

df = pl.DataFrame(
    {"A":[1,2,3]}
)

#%%
df.write_delta(table_path)


#%%

dt = DeltaTable(table_path)

pyarrow_dataset = dt.to_pyarrow_dataset()
sample_dataset = duckdb.arrow(pyarrow_dataset)

# %%


