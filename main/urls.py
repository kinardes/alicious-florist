from django.urls import path
from main.views import create_mood_flutter, show_main, create_flower, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_flower
from main.views import delete_flower
from main.views import add_flower_entry_ajax
 
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-flower', create_flower, name='create_flower'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-flower/<uuid:id>', edit_flower, name='edit_flower'),
    path('delete/<uuid:id>', delete_flower, name='delete_flower'), # sesuaikan dengan nama fungsi yang dibuat
    path('create-flower-entry-ajax', add_flower_entry_ajax, name='add_flower_entry_ajax'),
    path('create-flutter/', create_mood_flutter, name='create_mood_flutter'),
]