# data collection for abortion memes
這是論文**解析觀點：一種多模態方法，用於分析墮胎迷因中的論點**的程式碼和資料集。

#### 資料集(未公開)

來源
1. facebook
2. instagram
3. reddit

#### 標籤
**0** 支持墮胎權

**1** 反對墮胎權

**3** 無明顯立場

**4** 批評反對墮胎權

**5** 批評支持墮胎權

標籤的結果儲存在&nbsp;&nbsp;[allclassification.csv](allclassification.csv)\
(標註可能存在誤標)

#### 實驗
資料集\
分成**支持**和**反對**，0與4合併、1與5合併。

1. BERTopic\
   pro_with_lem.ipynb&nbsp;&nbsp;&nbsp; 支持的主題建模\
   anti_with_lem.ipynb&nbsp;&nbsp; 反對的主題建模

2. GPT & human\
   gpt-result.csv &nbsp;&nbsp;&nbsp;人類標註和GPT標註的結果\
   gptapi.ipynb   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API


