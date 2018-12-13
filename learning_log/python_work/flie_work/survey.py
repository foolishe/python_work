# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 05:40:24 2018

@author: dontworry
"""
class AnonymousSurvey():  #anonymous:匿名的.survey:调查
      def __init__(self,question):
          self.question=question
          self.responses=[]

      def show_question(self):
          print(question)

      def store_response(self,new_responses):
          self.responses.append(new_responses)

      def show_results(self):
          print('survey results:')
          for response in self.responses:
              print('-'+response)
                    
