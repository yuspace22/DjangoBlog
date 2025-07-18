from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def index(resquest): 
    # 查詢資料與資料庫操作
    article_records = Post.objects.all()
    
    # 處理查詢結果
    article_list = list()
    for count, article in enumerate(article_records):
        # ↑ article_records[count].title => article.title 
        article_list.append("#{}: {}<br><hr>".format(str(count), str(article)))
        article_list.append("<small>{}</small><br><hr>".format(article.content))
        article_list.append("slug:{}<br><hr>".format(article.slug))
    return HttpResponse(article_list)

# def 用來定義函式，後面接函式名稱(參數:
#    程式碼計算內容
#    return 結果

# a = 名稱(參數)


# for [idx序號], [var變數名稱] in [list查找的物件資料]:
    # FOR Loop 做的事情
    
def about(request):
    return HttpResponse()


def index_use_template(requests):
    article_records = Post.objects.all()
    now = datetime.now()
    # return render(requests, "index.html", locals())
    return render(requests, 'pages/home.html', locals())

def showPost(requests, slug):
    article = Post.objects.get(slug=slug)
    return render(requests, 'pages/post.html', locals())

def login(requsets):
    return render(requsets, "pages/login.html")


def showArticleList(requests):
    article = Post.objects.all().values()
    article = list(article)
    return JsonResponse(article, safe=False)