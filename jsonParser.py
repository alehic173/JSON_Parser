# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:12:59 2023

@author: alexa
"""

class json_parse:
    
    def __init__(self, json_string):
        self.json_string = json_string
        self.tokens = []
        self.current_position = 0
        
    def tokens(self):
        self.current_position = 0
        # Go through each character in json line
        while self.current_position < len(self.json_string):
            self.current_position = self.get_token(self.json_string[self.current_position:])
    def get_token(self):
        if self.json_string[self.current_position] == "{":
            self.current_position += 1
            return ('LBRACE', '{')
        elif self.json_string[self.current_position] == '}':
            self.current_position += 1
            return ('RBRACE', '}')
        elif self.json_string[self.current_position] == '[':
            self.current_position += 1
            return ('LBRACKET', '[')
        elif self.json_string[self.current_position] == ']':
            self.current_position += 1
            return ('RBRACKET', ']')
        elif self.json_string[self.current_position] == ':':
             self.current_position += 1
             return ('COLON', ':')
        elif self.json_string[self.current_position] == ',': 
             self.current_position += 1
             return ('COMMA', ',')
        elif self.json_string[self.current_position] == '"':
            return self.get_string_token()
        elif self.json_string[self.current_position].isdigit() or self.json_string[self.current_position] == '-':
            return self.get_number_token()
        elif self.json_string[self.current_position].isalpha():
            return self.get_keyword_token()
        else:
            raise ValueError(f"Invalid character: {self.json_string[self.current_position]}")
            
     # Return the full string between the quotation marks      
     def get_string(self)
     
         while 
        