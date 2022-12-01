import pyrebase
import json

# Udith Firebase project
configFileName = 'config-ud.json'
# Common File
# configFileName = 'config.json'

try:
    with open(configFileName) as json_file:
      data = json.load(json_file)
  
      # Print the type of data variable
      print("Type:", type(data))
  
      # Print the data of dictionary
      print("\nConfig:", data['config'])
      config = data['config']    
    
    firebase = pyrebase.initialize_app(config)

except :
    print("Failed to load the config file for setting up Firebase connection")
