# Add-users-to-room
This script will automates the process of adding users into a room. It takes in a CSV of userIDs; a configuration of pod, authentication keys/certs, and service account; and a roomID.

This script uses Python to function, please install it before attempting to run this.

### Install dependencies and Symphony Python SDK
You will need to install the requirements of the Python SDK (requirements.txt) file.
These can be found here: https://github.com/SymphonyPlatformSolutions/symphony-api-client-python/blob/master/requirements.txt

This file has already been added in this Repository.

To install it, you will need to save it as requirements.txt and install it via the pip command:
`pip install -r requirements.txt`

Second, you will need to install the Python SDK:
`pip install symphony-api-client-python`

### Setup config.json and RSA
Next, you will be required to have the following:

* RSA Key Pair
* config.json
  
These will be required to be passed through to the script so it can be executed.

RSA Key Pair, this will need to come internally from your team who administers your Pod.
A config.json will be required, an example one has been provided in the repo.

For certificate based authentication, please swap `"botRSAPath"` and `"botRSAName"`, with `"botCertPath"` and
`"botCertName"`. 

NOTE: In the example config, replace the domain URLs and port numbers to reflect your internal Pod URLs and ports.

###Running the script
To execute the script please go to the directory where you have saved the files (RSA keypair, config.json) and run the following command:
`python obtain_room_information.py --auth "rsa" --config "/path/to/config.json"`
