from oauth2client import client
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
google_code = "4/OKuEWktglAruEG-6MQ731nnrSSAEWTvQskXdOfwjZJo"

flow = client.flow_from_clientsecrets(
	'/home/nagar/mysite/mysite/client_secrets.json',
	scope='https://www.googleapis.com/auth/calendar',
	redirect_uri='http://devbox.example.com:8000/storeauthcode')
flow.params['access_type'] = 'offline'
credentials = flow.step2_exchange(google_code)
user_info = get_user_info(credentials)
print user_info
