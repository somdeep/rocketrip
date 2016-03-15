import sys
import oauth2
import urllib,json

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="bkPSHcvZirfVlfVGb5BxKictV", secret="hCxAZDwwJDhIDj2LlQxpS07WbK7CEMQQNmAmZU9BQNw0hIohh0")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content
 
home_timeline = oauth_req( 'https://api.twitter.com/1.1/search/tweets.json?q=%22manchester+united%22&count=1&result_type=recent', '619422408-yPaRg0V77PgbJK1ENvrscuhD8KDKTfo675em1uit', 'kGo6TtddMPgdED45ohrkN5tpZa7gB3q7iFrMIdo61UWOb' )
#print json.dumps(home_timeline)

home=json.loads(home_timeline)
#home=json.loads(home['statuses'][''])
#print home['statuses']

str=home['statuses'][0]
#print home
print str['metadata']
    
    
    