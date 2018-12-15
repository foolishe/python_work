# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 05:30:55 2018

@author: dontworry
"""
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question='what language did you first learn to speak?'
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin','chinese']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            print (response,self.my_survey.responses)
            self.assertIn(response,self.my_survey.responses)

unittest.main()
