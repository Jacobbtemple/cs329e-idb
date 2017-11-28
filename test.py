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

	def test_source_insert_4(self):
		s4 = Test(title='mybook4', publisher_name = 'publisher4')
		session.add(s4)

		r4 = session.query(Test).filter_by(title='mybook4').one()
		self.assertEqual(str(r4.publisher_name), 'publisher4')

		session.query(Test).filter_by(title='mybook4').delete()
		session.commit()

	def test_source_insert_5(self):
		s5 = Test(title='mybook5', publisher_name = 'publisher5')
		session.add(s5)

		r5 = session.query(Test).filter_by(title='mybook5').one()
		self.assertEqual(str(r5.publisher_name), 'publisher5')

		session.query(Test).filter_by(title='mybook5').delete()
		session.commit()

	def test_source_insert_6(self):
		s6 = Test(title='mybook6', publisher_name = 'publisher6')
		session.add(s6)

		r6 = session.query(Test).filter_by(title='mybook6').one()
		self.assertEqual(str(r6.publisher_name), 'publisher6')

		session.query(Test).filter_by(title='mybook6').delete()
		session.commit()

	def test_source_insert_7(self):
		s7 = Test(title='mybook7', publisher_name = 'publisher7')
		session.add(s7)

		r7 = session.query(Test).filter_by(title='mybook7').one()
		self.assertEqual(str(r7.publisher_name), 'publisher7')

		session.query(Test).filter_by(title='mybook7').delete()
		session.commit()

	def test_source_insert_8(self):
		s8 = Test(title='mybook8', publisher_name = 'publisher8')
		session.add(s8)

		r8 = session.query(Test).filter_by(title='mybook8').one()
		self.assertEqual(str(r8.publisher_name), 'publisher8')

		session.query(Test).filter_by(title='mybook8').delete()
		session.commit()

if __name__ == '__main__':
	unittest.main()
