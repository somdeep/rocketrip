#Write a simple python program ( function )  that returns a random tweet based on 'keyword' search. Your program should accept the 'keyword' as a param to your python function.
#
#Eg:
#prompt: <name-of-your-code> <keyword>
#@username: tweet that contains <keyword>
#media: <link> ( if any )
#
#Deadline: 1 Week
#Submission guideline:
#
#- Share a git-hub repo with us with your code
#- Must have instructions on how to run the code
#- You may only use the libraries listed below:
#
#Search API: https://dev.twitter.com/rest/public/search
#Python OAuth Lib: https://github.com/joestump/python-oauth2
#Python HTTP Lib: https://pypi.python.org/pypi/requests
#Python Standard Library:  https://docs.python.org/3.5/library/


import sys
import oauth2
import urllib,json

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="bkPSHcvZirfVlfVGb5BxKictV", secret="hCxAZDwwJDhIDj2LlQxpS07WbK7CEMQQNmAmZU9BQNw0hIohh0")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content
 
home_timeline = oauth_req( 'https://api.twitter.com/1.1/search/tweets.json?q=%22'+sys.argv[1]+'%22&count=1&result_type=recent', '619422408-yPaRg0V77PgbJK1ENvrscuhD8KDKTfo675em1uit', 'kGo6TtddMPgdED45ohrkN5tpZa7gB3q7iFrMIdo61UWOb' )

home=json.loads(home_timeline)
print sys.argv[1]


for key in home['statuses'] : 
    print (key['user']['name']),":",(key['text'].encode("utf-8"))
    if 'media' in key['entities']:
        for i in key['entities']['media']:
            print 'Media : ',i['media_url']

    else:
        print 'No media'