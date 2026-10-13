from api_loader import fetch_cars
from database import get_connection

df=fetch_cars()
conn=get_connection()
cursor=conn.cursor()
for index,row in df.iterrows():
    sql="""
    INSERT INTO cars (carId,brand,model,dailyRate ) VALUES (%s,%s,%s,%s)
    """
    values=(row['id'],
            row['car'],
            row['car_model'],
            row['price'])
    cursor.execute(sql,values)
    conn.commit()
print('Data Loaded Successfully')