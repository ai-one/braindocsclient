#!/usr/bin/env python
""" Copyright (c) 2015 ai-one inc., La Jolla CA. All rights reserved.
"""

import mysql.connector

class bdSQL(object):

	def __init__(self, user, password, host, database):
		self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
		self.database = database

	def getAnalysisResults_TextUnit(self):
		cursor = self.cnx.cursor(buffered=True)

		query = ("SELECT * FROM analysisresults_textunit")
		cursor.execute(query)
		return cursor