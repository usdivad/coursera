import urllib2
import urllib
import json
import base64

# Original methods deprecated!! booo
# response = urllib.urlopen(url+"?q=microsoft?consumer_key=yXWiIYRi1QQ7rSWgRgFLMQ")
# #response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
# print json.load(response)

# Getting credentials from external file
creds = open("creds.txt", "r")

url = "https://api.twitter.com/1.1/search/tweets.json"

key = creds.readline().rstrip()
print key
secret = creds.readline().rstrip()
print secret

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

print urllib2.urlopen(req)