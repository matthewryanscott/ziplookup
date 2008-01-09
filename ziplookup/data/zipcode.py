from gzip import GzipFile
import csv
import anydbm
import os
from simplejson import dumps


DATA_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_PATH = os.path.join(DATA_PATH, 'zipcode.csv.gz')
DB_PATH = os.path.join(DATA_PATH, 'zipcode.db')


_db = None


def update_dbhash_from_csv():
    f = GzipFile(CSV_PATH, 'rb')
    r = csv.DictReader(f)
    # Create the new database.
    tmp_db_path = DB_PATH + '.tmp'
    # db objects don't support 'with'.
    db = anydbm.open(tmp_db_path, 'c')
    try:
        for record in r:
            db[record['zip']] = dumps(dict(
                city = record['city'],
                state = record['state'],
                ))
    finally:
        db.close()
    f.close()
    # Everything succeeded; rename to the final filename.
    os.rename(tmp_db_path, DB_PATH)


def get_zipcode_info(zipcode):
    global _db
    if _db is None:
        if not os.path.exists(DB_PATH):
            update_dbhash_from_csv()
        _db = anydbm.open(DB_PATH, 'r')
    return _db[zipcode]


if __name__ == '__main__':
    print 'Updating %s using %s...' % (DB_PATH, CSV_PATH)
    update_dbhash_from_csv()
    print 'Done.'
