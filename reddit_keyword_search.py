#參數設定
#keywordlist = ['abortion']
keywordlist = ['Abort', 'termination of pregnancy', 'terminate pregnancy',
               'pregnancy termination', 'post-abortion', 'postabortion', 
               'roe v wade', 'prolife', 'right-to-life', 'anti-choice', 
               'pro-abortion', 'pro abortion',
               'abortion']

#sort='hot' #手動添加
#time_filter='year' #手動添加

import os
import praw
import csv
from datetime import datetime

# 選擇一個subreddit
subreddit = reddit.subreddit('memes')

# 定義要抓取的帖子數量
#limit = 1000

for keyword in keywordlist:
    
    # 設定你想要檢查和創建的資料夾路徑
    folder_path = 'reddit_memes\\' + keyword + '\\'

    # 檢查資料夾是否存在
    if not os.path.exists(folder_path):
        # 如果資料夾不存在，則創建它
        os.makedirs(folder_path)
        print(f"資料夾 '{folder_path}' 已創建。")
    else:
        # 如果資料夾已存在，則輸出提示信息
        print(f"資料夾 '{folder_path}' 已存在。")

    # 打開一個CSV文件以寫入
    with open(folder_path + keyword +'.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 寫入標題行
        writer.writerow(['Title', 'URL', 'post url','Author', 'Score', 
                         'Subreddit', 'Created UTC', 'Selftext', 
                         'Num Comments', 'Upvote Ratio', 'Is Self','comment',
                         'author_flair_text','clicked','distinguished',
                         'edited','id','is_original_content','link_flair_text',
                         'locked','name','over_18','permalink','saved','spoiler','stickied'])

        # 遍歷subreddit的帖子sort=sort, time_filter=time_filter
        for submission in subreddit.search(keyword):
            # 构建完整的Reddit帖子URL **取評論需要文章連結 直接用submission.url取到的圖片 .jpg/.png的連結
            post_url = f"https://www.reddit.com{submission.permalink}"
            
            submissioncomment = reddit.submission(url=post_url)
            # 在遍历评论之前，尝试加载所有可用的评论
            submissioncomment.comments.replace_more(limit=None)
            
            commentlist = []

            for comment in submissioncomment.comments.list():
                if isinstance(comment, praw.models.MoreComments):
                    continue  # 如果是MoreComments对象，跳过这个迭代
                
                commentpair = []
                commentpair.append(comment.body)
                commentpair.append(datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'))
                commentlist.append(commentpair)
                
                
            # 轉換創建時間
            created_time = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
            # 寫入每個帖子的資訊
            writer.writerow([submission.title, 
                             submission.url,
                             post_url,
                             str(submission.author), 
                             submission.score,
                             str(submission.subreddit), 
                             created_time, 
                             submission.selftext,
                             submission.num_comments, 
                             submission.upvote_ratio, 
                             submission.is_self,
                             commentlist,
                             submission.author_flair_text, ##
                             submission.clicked,
                             submission.distinguished,
                             submission.edited,
                             submission.id,
                             submission.is_original_content,
                             submission.link_flair_text,
                             submission.locked,
                             submission.name,
                             submission.over_18,
                             submission.permalink,
                             submission.saved,
                             submission.spoiler,
                             submission.stickied])



    import pandas as pd

    # 讀取CSV檔案
    csv_file_path = folder_path + keyword +'.csv'
    df = pd.read_csv(csv_file_path)

    print('貼文數',df['URL'])

    import requests
    import time

    error = []
    memenumber = 0

    for i in df['URL']:

        try:

            n = i.split('redd.it/')[1]

            pic = requests.get(i)
            print(pic)
            img2 = pic.content #圖片裡的內容
            imgpath = 'reddit_memes\\' + keyword +'\\' + n #存成jpg檔
            pic_out = open(imgpath,'wb') 
            pic_out.write(img2) #將get圖片存入img2
            pic_out.close() #關閉檔案(很重要)
            memenumber += 1

            time.sleep(1)
        except Exception as e:
            error.append(i)

    # 指定CSV文件名
    csv_file_name = 'reddit_memes\\' + keyword +'\\' + 'error.csv'

    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # 對於一維列表，迭代每個元素，並將每個元素作為一行寫入
        for element in error:
            writer.writerow([element])  # 注意element被放在列表中，因為writerow()期望一個可迭代對象

    print(f"擷取失敗貼文已寫入 {csv_file_name}")
    print('關鍵字',keyword,'迷因數量',memenumber)
