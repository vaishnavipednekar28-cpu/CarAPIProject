import pandas as pd
from database import get_connection
def get_cars():
    conn = get_connection()
    sql="select * from cars"
    df = pd.read_sql(sql, conn)
    return df

