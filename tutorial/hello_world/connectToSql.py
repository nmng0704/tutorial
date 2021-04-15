import pymysql


def getData():

    try:
        db = pymysql.connect(
            host='tutorial-db-instance.ctewusudw0bh.us-east-2.rds.amazonaws.com', user='tutorial_user', password='Play1234', database='sample')
        print("ok")
    except pymysql.Error as e:
        print("fail")

    cursor = db.cursor()

    sql = "SELECT * FROM dataset"

    try:
        # execute the SQL command
        cursor.execute(sql)
        results = cursor.fetchall()

        # db data to list of list
        dataset = [list(i) for i in results]

        for row in dataset:
            del row[0]

    except:
        import traceback
        traceback.print_exc()

        print("Error: cannot fetch data")

    return dataset
