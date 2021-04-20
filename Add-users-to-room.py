import argparse
import time
from sym_api_client_python.auth.rsa_auth import SymBotRSAAuth
from sym_api_client_python.auth.auth import Auth
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.configure.configure import SymConfig

# Global variables to pass the queries to run
room_streamid = ""
csv_file_full_path = ""

def add_user(bot_client, streamid, userid):
    user_response = bot_client.get_stream_client().add_member_to_room(streamid, userid)
    return user_response

# Function here will retrieve the users in the room and pass each id to the "retrieve_names" function
def extract_users(csv_file):
    extracted_users = []
    inputfile = open(csv_file, 'r')
    for line in inputfile:
        extracted_users.append(int(str.strip(line)))
    return extracted_users

def bulk_add_users(bot_client, streamid, csv_file):
    user_ids = extract_users(csv_file)
    for userid in user_ids:
        returned_resp = add_user(bot_client, streamid, userid)
        print(str(userid) + " response: "+str(returned_resp))
        time.sleep(3)

# Setup the configuration loading
parser = argparse.ArgumentParser()
parser.add_argument("--auth", choices=["rsa", "cert"], default="rsa", help="Authentication method to use")
parser.add_argument("--config", help="Config json file to be used")
parser.add_argument("--csv", default="userIDs.csv", help="Path of CSV file of userIDs")
parser.add_argument("--stream", help="Destination RoomID for users in CSV")
args = parser.parse_args()

# Pass variables over
room_streamid = args.stream
csv_file_full_path = args.csv

# Cert Auth flow: pass path to certificate config.json file
config_path = args.config
configure = SymConfig(config_path, config_path)
configure.load_config()
if args.auth == "rsa":
    auth = SymBotRSAAuth(configure)
elif args.auth == "cert":
    auth = Auth(configure)
else:
    raise ValueError("Unexpected value for auth: " + args.auth)
auth.authenticate()

bot_client = SymBotClient(auth, configure)

print("Starting\n")
try:
    bulk_add_users(bot_client, room_streamid, csv_file_full_path)
except Exception as e:
    print('An Error has occurred: ', e)
print("\nCompleted")
