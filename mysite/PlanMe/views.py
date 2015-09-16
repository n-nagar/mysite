from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from oauth2client import client
from django.conf import settings
from django.core.urlresolvers import reverse
from .models import User

# Create your views here.
def index(request):
	try:
		session_tok = request.COOKIES.get('PlanMe')
		user = User.objects.filter(sess_id=session_tok)
		if (user.count() == 1):
			c = Context({'user': user[0]})
			return render(request, 'PlanMe/index.html', c, context_instance=RequestContext(request))
	except:
		pass
	return render(request, 'PlanMe/auth.html', context_instance=RequestContext(request))

def index2(request):
	return render(request, 'PlanMe/index2.html')


def get_user_info(credentials):
  """Send a request to the UserInfo API to retrieve the user's information.

  Args:
    credentials: oauth2client.client.OAuth2Credentials instance to authorize the
                 request.
  Returns:
    User information as a dict.
  """
  user_info_service = build(
      serviceName='oauth2', version='v2',
      http=credentials.authorize(httplib2.Http()))
  user_info = None
  try:
    user_info = user_info_service.userinfo().get().execute()
  except errors.HttpError, e:
    logging.error('An error occurred: %s', e)
  if user_info and user_info.get('id'):
    return user_info
  else:
    raise NoUserIdException()

def storeauthcode(request):
	flow = client.flow_from_clientsecrets(
		settings.BASE_DIR + '/client_secrets.json',
		scope='https://www.googleapis.com/auth/calendar',
		redirect_uri=request.build_absolute_uri(reverse('storeauthcode')))
	google_code = request.body
	if (google_code == None):
		return redirect('Index')
	else:
		flow.params['access_type'] = 'offline'
		credentials = flow.step2_exchange(google_code)
		user_info = get_user_info(credentials)
		return HttpResponse(user_info)
