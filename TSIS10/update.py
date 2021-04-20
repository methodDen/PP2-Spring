import psycopg2

from config import config

def update_vendor(vendor_id, vendor_name):

    sql = """UPDATE vendors 
        SET vendor_name = %s
        WHERE vendor_id = %s
    """

    conn = None
    updated_rows = 0

    try:

        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(sql, (vendor_name, vendor_id))

        updated_rows = cur.rowcount
        print(updated_rows)
        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    update_vendor(1, "3M Corp")