# Add-users-to-room
This script will automates the process of adding users into a room. It takes in a CSV of userIDs; a configuration of pod, authentication keys/certs, and service account; and a roomID.

This script uses Python to function, please install it before attempting to run this.

### Install dependencies and Symphony Python SDK
You will need to install the requirements of the Python SDK (requirements.txt) file.
These can be found here: https://github.com/SymphonyPlatformSolutions/symphony-api-client-python/blob/master/requirements.txt

This file has already been added in this Repository.

To install it, you will need to save it as requirements.txt and install it via the pip command:
```
pip install -r requirements.txt
```

Second, you will need to install the Python SDK:
```
pip install symphony-api-client-python
```

### Setup config.json and RSA
Next, you will be required to have the following:

* RSA Key Pair
* config.json
* userIDs.csv
  
These will be required to be passed through to the script so it can be executed.

**RSA Key Pair**

This will need to come internally from your team who administers your Pod.

**config.json**

This will be required in this format:

```
{
  "sessionAuthHost": "YOUR-POD-SUBDOMAIN.symphony.com",
  "sessionAuthPort": 443,
  "keyAuthHost": "YOUR-POD-SUBDOMAIN.symphony.com",
  "keyAuthPort": 443,
  "podHost": "YOUR-POD-SUBDOMAIN.symphony.com",
  "podPort": 443,
  "agentHost": "YOUR-POD-SUBDOMAIN.symphony.com",
  "agentPort": 443,
  "botRSAPath": "PATH",
  "botRSAName": "BOT-RSA-NAME",
  "botCertPassword": "BOT-PASSWORD",
  "botUsername": "BOT-USERNAME",
  "botEmailAddress": "BOT-EMAIL",
  "appCertPath": "",
  "appCertName": "",
  "appCertPassword": "",
  "proxyURL": "",
  "proxyUsername": "",
  "proxyPassword": "",
  "authTokenRefreshPeriod": "30",
  "truststorePath": ""
}
```

**For certificate based authentication**

Please swap `"botRSAPath"` and `"botRSAName"`, with `"botCertPath"` and
`"botCertName"`. 

You may also need to switch `YOUR-POD-SUBDOMAIN.symphony.com` to `YOUR-POD-SUBDOMAIN-api.symphony.com` for SessionAuthHost and KeyAuthHost.

NOTE: In the example config, replace the domain URLs and port numbers to reflect your internal Pod URLs and ports.

**userIDs.csv**

This file needs to be formatted in the following way with the userIDs of each account to be added to the room:

```
userID1
userID2
userID3
userID4
userID5
...
```

### Running the script
To execute the script please go to the directory where you have saved the files (RSA keypair, config.json) and run the following command:
```
python add-users-to-room.py --auth "rsa" --config "/path/to/config.json" --csv "/path/to/userIDs.csv" --stream "{streamID}"
```
