# Using urllib,urllib2 instead of requests just as an exercise
import urllib2
import urllib
import json
import base64
import sys

# Original methods deprecated!! booo
# response = urllib.urlopen(url+"?q=microsoft?consumer_key=yXWiIYRi1QQ7rSWgRgFLMQ")
# #response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
# print json.load(response)

# Getting credentials from external file
# creds.txt in format "key\nsecret"
def get_bearer_from_oauth():
    creds = open("creds.txt", "r")

    url = "https://api.twitter.com/1.1/search/tweets.json"

    key = creds.readline().rstrip()
    secret = creds.readline().rstrip()

    creds.close()

    # Encode as per Step 1 of https://dev.twitter.com/docs/auth/application-only-auth
    encoded_value = base64.b64encode(key+":"+secret)

    # Step 2: obtaining bearer token
    header = {
        "Authorization": "Basic " + encoded_value,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    body = {
        "grant_type": "client_credentials"
    }

    body_encoded = urllib.urlencode(body)

    req = urllib2.Request("https://api.twitter.com/oauth2/token", body_encoded, header)

    response = urllib2.urlopen(req)
    bearer = json.load(response)['access_token']

    return bearer

def get_bearer_from_file():
    f = open("bearer.txt", "r")
    bearer = f.readline().rstrip()
    f.close()
    return bearer


# The actual API request haha
# Search for command line argument
args = sys.argv
query = "data science"
if len(args) > 1:
    query = args[1]
else:
    query = query
    #print "Need at least 1 argo"
    #exit()    

# Setting up the query
# We can get bearer either from oauth (initially) or from local file (bearer.txt) as long as it's there
#bearer = get_bearer_from_oauth() 
bearer = get_bearer_from_file()
url = "https://api.twitter.com/1.1/search/tweets.json"
data = {
    "q": query,
    "count": "10"
}
data_encoded = urllib.urlencode(data)
url_encoded = url + "?" + data_encoded
header = {
    "Authorization": "Bearer " + bearer
}
#print data_encoded

# Sending the query
req = urllib2.Request(url_encoded, headers=header)
response = urllib2.urlopen(req)

# Getting the results
results = json.load(response)
statuses = results["statuses"]
#print statuses[0]["text"]

for status in statuses:
    name = status["user"]["name"]
    screen_name = status["user"]["screen_name"]
    text = status["text"]
    output =  name + " (@" + screen_name + ")" + ": " + text + "\n"

    # .encode("utf-8") to prevent "'ascii' codec can't encode" problem
    print output.encode("utf-8")

#print json.dumps(results, indent=4)