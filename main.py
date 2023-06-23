#%%
from deltalake import DeltaTable
import duckdb
import polars as pl

table_path = "data/delta/sample_dataset"

#%%

df = pl.DataFrame(
    {"A":[1,2,3]}
).with_columns(pl.col("A").cast(pl.Float32))

#%%
df.write_delta(table_path, mode="overwrite")
#%%
df
#%%

df.with_columns(
    pl.col("A") * 1.5
).write_delta(table_path, mode="append")

#%%

dt = DeltaTable(table_path)
dt.history()
#%%

dt.schema()

#%%

pyarrow_dataset = dt.to_pyarrow_dataset()
sample_dataset = duckdb.arrow(pyarrow_dataset)

# %%

sample_dataset.filter("A > 1").to_df()
