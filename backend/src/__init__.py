import pyrebase
import os
import json

# Udith Firebase project
# configFileName = 'config-ud.json'
# Common File
configFileName = 'firebase-config.json'

try:
    with open(configFileName) as json_file:
      data = json.load(json_file)


# firebase = pyrebase.initialize_app(config)

      # Print the type of data variable
      print("Type:", type(data))

      # Print the data of dictionary
      print("\nConfig:", data['config'])
      config = data['config']    

    if os.environ.get('CI') == 'true':
      config['databaseURL'] = config['databaseURL'] + '/CI-rtdb'
      print('CI environment detected!')
      print(f'Using CI database at {config["databaseURL"]} for testing.')
    firebase = pyrebase.initialize_app(config)

except :
    print("Failed to load the config file for setting up Firebase connection")
