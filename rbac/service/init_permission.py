def init_permission(user,request):

    permission_list = user.user2role.values('role2per__title', 'role2per__url','role2per__is_menu').distinct()
    username = user.username
    url_list = []
    for item in permission_list:
        url_list.append(item['role2per__url'])
    request.session['permission_url'] = url_list
    request.session['username'] = username
