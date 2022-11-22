import sys
sys.path.append('backend/test')
from AuthTest import AuthTestApp
from DeckTest import DeckTestApp
from CardTest import CardTestApp
import unittest
import os

if __name__=="__main__":
  
  if os.environ.get('CI') != 'true':
    raise Exception('ERROR: set environment variable CI=true to run tests')

  unittest.main()
