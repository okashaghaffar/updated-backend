from django.urls import path
from .views import *

urlpatterns=[
    path("",getRoutes,name="getRoutes"),
    path("user/register",RegisterUser,name="RegisterUser"),
    path("user/get",GetUsers,name="getUsers"),
    path("user-role/get",getUserRole,name="getUserRole"),
   path('user/login', Loginview.as_view(), name='token_obtain_pair'),
   path('get/projects', GetProjects, name='GetProjects'),
   path('post/project', CreateProject, name='CreateProject'),
   path('put/statusupdate',UpdateProjectStatus, name='UpdateProjectStatus'),
   path('user/task',TaskView, name='TaskView'),
   path('user/task/<int:id>',TaskbyId, name='TaskbyId'),
   path("put/taskupdate",UpdateTaskStatus,name="UpdateTaskStatus"),
   path("get/taskcompleted",TaskCompleted,name="UpdateTaskStatus"),
   path("get/na-project",GetNaProjects,name="GetNaProjects"),
   path("get/dev",getDev,name="getDev"),
   path("get/sale/project/<int:id>",GetSaleProject,name="GetSaleProject"),
   path("project/userstory",getUserStory,name="GetSaleProject"),
   path("project/userstory/<int:id>",getUserStorybyId,name="GetSaleProject"),
    path('chat', generate_requirements),
    path('check', check),
    path('convert-mp4-to-wav', convert_mp4_to_wav),
    path('append-wav-files', append_wav_files),
    path('create/pteam', create_pteam),
    path('get/pteam', list_pteams),
    path('get/pteam/<int:id>', retrieve_pteam),
    path('get/user/us/<int:id>', UserTeam),
    path('select/task', selectTask),
    path('get/team', getTeams),
    path('get/url', getUrl),
    path('get/dev-progress/<int:id>', getDevelopers),
    path('search/<str:query>', search_view),

















]