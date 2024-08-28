# Youtube 垃圾评论分析

## 数据说明
### 字段	 |  说明

“`
comment_id | 此列包含每条评论的唯一标识符。它与建模无关，在分析过程中可以忽略。
“`  
“`
Author | 发布评论的人员的姓名或用户名。此功能可以提供有关与垃圾邮件帐户相关的模式的见解。
“`  
“`
Date | 发表评论的日期。分析日期可以揭示垃圾邮件活动随时间推移的趋势。
“`  
“`
Content | 评论的实际文本内容。这是用于训练分类模型以检测垃圾邮件的主要功能。
“`  
“`
video_name | 发表评论的 YouTube 视频的名称。这可以提供不同类型视频的垃圾内容活动的背景信息或模式。
“`  
“`
class | 目标变量，其中 1 表示垃圾评论，0 表示合法评论。此列是分类任务的重点。
“`  

>数据来源：[kaggle]([https://www.heywhale.com/mw/dataset/66bef4db9b33c0f19c7a1c8c](https://www.kaggle.com/datasets/ahsenwaheed/youtube-comments-spam-dataset/data))
