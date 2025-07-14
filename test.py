from modules.crawler.utils import parserTargetURL
from modules.crawler.utils import run


# print(parserTargetURL('board', board='Baseball'))
# print(parserTargetURL('board',
#                       board='Baseball',
#                       pageNum='19621'))
# print(parserTargetURL('article'))
# print(parserTargetURL('article',
#                       articleURL='/bbs/Baseball/M.1752411597.A.6CA.html'))

from modules.crawler.utils import run
data = run(board='Baseball', pageNum='19621')
print(data)