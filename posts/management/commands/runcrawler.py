from django.core.management.base import BaseCommand
from modules.crawler.utils import run
from posts.models import Post




class Command(BaseCommand):
    help = "向 PPT.cc 進行爬蟲, usage: --board [指定看板] --pages [指定頁數]"


    def add_arguments(self, parser):
        parser.add_argument('--board', type=str, help='看板名稱')
        parser.add_argument('--pages', type=str, help='目標頁數')


    def handle(self, *args, **options):
        target_board = options.get('board')
        target_num = options.get('pages')


        if target_board is None:
            target_board = 'Stock'
        if target_num is None:
            target_num = ""


        data = run(board=target_board, pageNum=target_num)
        for article in data:
            temp_slug = article['url'].split("{}/".format(target_board))[1]
            temp_slug = temp_slug.split(".html")[0]
            if Post.objects.filter(slug=temp_slug).exists():
                print("{} 看版文章: {} 已存在資料庫".format(target_board, temp_slug))
            else:
                article_model = Post(
                    title=article['title'],
                    slug=temp_slug,
                    content=article['content'],
                )
                article_model.save()
        return None