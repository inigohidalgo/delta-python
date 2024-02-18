from deltalake import DeltaTable
import duckdb
import polars as pl

table_path = "data/delta/sample_dataset"
from deltalake import DeltaTable, write_deltalake
import pyarrow as pa

write_deltalake(

"tmp/test1",
    pl.DataFrame(
    {"A":[1,2,3],
    "B": [4,5,6]}
).with_columns(pl.col("A").cast(pl.Float32)).to_arrow()
)

dt = DeltaTable("tmp/test1")


(
    dt.merge(
        source=pl.DataFrame(
    {"A": [3,4,5],
     "B": [7,8,9]}
).to_arrow(),
        predicate="target.A = source.A",
        source_alias="source",
        target_alias="target")
    .when_matched_update_all()
    .when_not_matched_insert_all()
    .execute()
)