import os
import unittest
from models import Base, Book, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):

        s1 = Book(title='mybook1', isbn = 'isbn1')
        s2 = Book(title='mybook2', author_name = 'author2')
        s3 = Book(title='mybook3', publisher_name = 'publisher3')

        session.add(s1)
        session.add(s2)
        session.add(s3)
        session.commit()


        r1 = session.query(Book).filter_by(title='mybook1').one()
        r2 = session.query(Book).filter_by(title='mybook2').one()
        r3 = session.query(Book).filter_by(title='mybook3').one()

        self.assertEqual(str(r1.isbn), 'isbn1')
        self.assertEqual(str(r2.author_name), 'author2')
        self.assertEqual(str(r3.publisher_name), 'publisher3')

        session.query(Book).filter_by(title='mybook1').delete()
        session.query(Book).filter_by(title='mybook2').delete()
        session.query(Book).filter_by(title='mybook3').delete()
        session.commit()



if __name__ == '__main__':
    unittest.main()
