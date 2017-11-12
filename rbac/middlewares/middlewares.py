import re

from django.shortcuts import redirect,HttpResponse
from django.conf import settings  #导入settings


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):
    def process_request(self,request):
        current_url = request.path_info
        for url in settings.VALID_URL:
            if re.match(url,current_url):
                return None

        permission_list = request.session.get('permission_url')
        # print(permission_list)
        if permission_list:
            print(permission_list)
            print(current_url)
            flag = False
            for url in permission_list:
                regex = '^{0}$'.format(url)
                print(regex)
                if re.match(regex, current_url):
                    flag = True
                    print(flag)
                    break

            if not flag:
                return HttpResponse('无权访问')