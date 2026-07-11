import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-b61a550-myduyennguyen0620-26ee.h.aivencloud.com",

        port=11336,

        user="avnadmin",

        password="AVNS_J_Pquo4LETLkdt6Q4OM",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
