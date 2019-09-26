#!/usr/bin/env python
# coding: utf-8

# In[159]:


#generated token and id from developers.facebook.com
# token of my profile = EAAHFnDWM6S8BAPJsi0e3bruszNahKZAZCOsc90khsQyXUPTMfJdOVKpkMSnwNOy3hYcerViq3QAflpybdP5bdHo6WnB3eZC2TZA1NNfawh1UEAw4RaZCOvg2BQ9nOAZBwqmSdF1ExiuZBxlNY2S4wZAClgOxR3RZBPEMZCCUiHfhMoKodk8v3kFlLyV4ZAEFeZAeqOc47XbTp6s71gZDZD
# my_id=1115679395296991
token=input()
user_id=input()


# In[160]:


#urls

name='https://graph.facebook.com/'+user_id+'?fields=name&access_token='+token
home_town='https://graph.facebook.com/'+user_id+'?fields=hometown&access_token='+token
friends='https://graph.facebook.com/'+user_id+'?fields=friends&access_token='+token
birthday="https://graph.facebook.com/v4.0/"+user_id+"?fields=birthday&access_token="+token
gender="https://graph.facebook.com/v4.0/"+user_id+"?fields=gender&access_token="+token


# In[161]:


import requests
import json


# In[164]:


home_town_json=requests.get(home_town)
name_json=requests.get(name)
friends_json=requests.get(friends)
birthday_json=requests.get(birthday)
gender_json=requests.get(gender)


# In[165]:


home_town_json.text


# In[166]:


home_town_dict=home_town_json.json()
name_dict=name_json.json()
friends_dict=friends_json.json()
birthday_dict=birthday_json.json()
gender_dict=gender_json.json()


# In[167]:


home_town_text=home_town_dict['hometown']['name']
name_text=name_dict['name']
friends_count=friends_dict['friends']['summary']['total_count']
birthday_text=birthday_dict['birthday']
gender_text=gender_dict['gender']


# In[168]:


print("name : %s"%name_text)
print("gender : %s"%gender_text)
print("birthday : %s"%birthday_text)
print("hometown : %s"%home_town_text)
print("No.of friends : %s"%friends_count)


# In[ ]:




