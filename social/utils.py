import json
from social.models import Profile, Post, Comment
dados = open('./db.json',) 
  
data = json.load(dados) 
  
for i in data['users']: 
    profile = Profile()
    profile.name = i['name']
    profile.username = i['username']
    profile.email = i['email']
    profile.street = i['address']['street']
    profile.suite = i['address']['suite']
    profile.city = i['address']['city']
    profile.zipcode = i['address']['zipcode']
    profile.save()

for j in data['posts']:
    post = Post()
    user = Profile.objects.get(id=j['userId'])
    post.user = user
    post.title = j['title']
    post.body = j['body']
    post.save()

for k in data['comments']:
    commet = Comment()
    post = Post.objects.get(id=k['postId'])
    commet.post = post
    commet.name = k['name']
    commet.email = k['email']
    commet.body = k['body']
    commet.save()

dados.close()