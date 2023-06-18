To use all files properly install Flask and other addons before:

pip3 install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46

1. set_pg
2. psql
3. CREATE DATABASE taskmanager;
4. Check if its created and then \q
5. Python3 + enter
6. from taskmanager import db
7. db.create_all()
8. exit()
9. check - psql -d taskmanager \dt