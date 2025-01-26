# data collection for abortion memes
這是論文**解析觀點：一種多模態方法，用於分析墮胎迷因中的論點**的程式碼和資料集。

#### 資料來源
* facebook

  資料夾crawl為原始圖片資料集和評論，crawl裡面有四個以日期區間命名的資料夾，e.g. 20210101-20210403，與資料夾同名的csv是該資料夾裡所有貼文的其他屬性，作者、發文日期、按讚數等等。
日期區間資料夾裡是一組一組的圖片和同名csv檔，csv檔是貼文底下的留言和留言作者。

  **注意**

  20230404-20240404 資料夾裡的評論是所有貼文的評論統一儲存在comment.csv
* instagram
* reddit

  從以下看板中蒐集，每個看板的蒐集關鍵字即是內部資料夾名稱，每個關鍵字資料夾裡有一個同名csv，儲存該資料夾所有迷因的屬性跟評論。
  * r/memes
  * r/dankmemes
  * r/politicalmemes
  * r/antimeme
  * r/meme
  * r/Wholesomememes

 [完整資料集](<https://drive.google.com/drive/folders/1U17i1n4X1wwCJUmg5FUBimTgtP9hIXQ4?usp=sharing>)

#### 標籤
**0** 支持墮胎權

**1** 反對墮胎權

**2** 無關

**3** 無明顯立場

**4** 批評反對墮胎權

**5** 批評支持墮胎權

#### 實驗資料集
分成**支持**和**反對**，0與4合併、1與5合併。
