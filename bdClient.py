#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter
from bdAPI import *
from bdSQL import *

class simpleapp_tk(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		self.bdAPI = bdAPI('usernams', 'password','https://192.168.56.101/at/')

		self.bdSQL = bdSQL('username', 'password', 'localhost', 'aione')

	def initialize(self):
		self.grid()

		button = tkinter.Button(self,text=u"Get Analysis Results",
								command=self.getResultsClick)
		button.grid(column=0,row=0)

		self.labelVariable = tkinter.StringVar()
		label = tkinter.Label(self,textvariable=self.labelVariable,
							  anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,columnspan=2,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.update()
		self.geometry(self.geometry())

	def getResultsClick(self):
		self.labelVariable.set("Retrieving Results")
		results = self.bdAPI.getAnalysisResults()

		print(len(results))

		for result in results:
			print (result['_id'] + ' - ' + result['analysisId'])
			#Get Result Details and send to MySQL

		analysisDetails = self.bdAPI.getAnalysisDetailsTextUnits(results[1]['analysisId'])

		print(self.bdSQL.getAnalysisResults_TextUnit())
		self.labelVariable.set("Results Retrieved")

	#getResultsFromDB: Gets list of analysisIds that are already in MySQL DB
	#def getResultsFromDB():


	#getUnimportedResults: Compares list of analysisIds that are in the MySQL DB against those
	#					imported from BrainDocs. Returns a list of analysisIds to save to DB
	#def getUnimportedResults(dbResults, bdResults):


if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('my application')
	app.mainloop()