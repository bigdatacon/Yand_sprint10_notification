import requests
answer = requests.get("http://127.0.0.1:8000/user/", params={'db_name' : 'auth', 'user_id' : 'a61846cf-8882-4213-a471-f763000d1147'})
print(f' eto answer one user: {answer.json()}')


answer = requests.get("http://127.0.0.1:8000/get_all_users_info_from_table/", params={'db_name' : 'auth'})
print(f' eto answer all users : {answer.json()}')