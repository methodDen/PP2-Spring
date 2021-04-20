import psycopg2

from config import config

def insert_vendor(vendor_name):

    sql = """INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;"""

    conn = None
    vendor_id = None

    try:
        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(sql, (vendor_name,))

        vendor_id = cur.fetchone()[0]
        print(vendor_id)

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id


if __name__ == '__main__':
    # insert one vendor
    insert_vendor("3M Co.")