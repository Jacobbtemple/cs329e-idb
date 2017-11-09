from unittest import TestCase, main
import os
import unittest
from models import Base, Test, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
	def test_source_insert_1(self):

		s1 = Test(title='mybook1', isbn = 'isbn1')
		session.add(s1)
		session.commit()
		
		r1 = session.query(Test).filter_by(title='mybook1').one()
		self.assertEqual(str(r1.isbn), 'isbn1')

		session.query(Test).filter_by(title='mybook1').delete()
		session.commit()

	def test_source_insert_2(self):
		s2 = Test(title='mybook2', author_name = 'author2')
		session.add(s2)
		session.commit()

		r2 = session.query(Test).filter_by(title='mybook2').one()          
		self.assertEqual(str(r2.author_name), 'author2')

		session.query(Test).filter_by(title='mybook2').delete()
		session.commit()

	def test_source_insert_3(self):
		s3 = Test(title='mybook3', publisher_name = 'publisher3')
		session.add(s3)

		r3 = session.query(Test).filter_by(title='mybook3').one()
		self.assertEqual(str(r3.publisher_name), 'publisher3')

		session.query(Test).filter_by(title='mybook3').delete()
		session.commit()

if __name__ == '__main__':
	unittest.main()
