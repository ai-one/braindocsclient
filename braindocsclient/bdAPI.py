#!/usr/bin/env python
""" Copyright (c) 2015 ai-one inc., La Jolla CA. All rights reserved.
"""

import requests

# turn off warnings
requests.packages.urllib3.disable_warnings()

class BraindocsApi(object):
    def __init__(self, username, password, baseURL):
        """ Post request to login page. Set the "verify" option to false, as the
            ai-one SSL Certificates are not presently verified. """
        self.baseURL = baseURL
        self.session = requests.Session()
        loginData = {'username':username, 'password':password}
        r = self.session.post(baseURL + '/login', data=loginData, verify=False)

    def getAnalysisResults(self):
        r = self.session.get(self.baseURL + '/getAnalysisResults', verify=False)
        analysisResults = r.json()
        return analysisResults

    def getAnalysisDetailsTextUnits(self, id):
        r = self.session.get(self.baseURL + '/getAnalysisDetailsTextUnits?analysisId=' + id, verify=False)
        analysisResults = r.json()
        return analysisResults
        