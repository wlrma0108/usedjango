from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
nextId=4
topics =[
    {'id':1,,'title':'routing','body':'Routing is ..'},
    {'id':2,'title':'view','body',:'view is ..'}
    {'id':3,'title':'view','body',:'Model is ..'}
]
def HTMPTemplate(articleTag,id=None):
    gloabal topics
    contextUI =''
    
    ol=''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1>Django</h1>
        <ul>
        
            {ol}
            
        </ul>
        {articleTag}
        <ul>
            <li><a href ="/create/">create</a></li>
            {contexUI}
        </ul>
        
        <h2>welcome</h2>
        Hello,Django
    </body>
    </html>    
    '''
    
@csrf_exempt

def index(request):
    return HttpResponse('Hello Django')

def create(request):
    return HttpReponse('create')

def read(request):
    return HttpReponse('Read')


# Create your views here.
