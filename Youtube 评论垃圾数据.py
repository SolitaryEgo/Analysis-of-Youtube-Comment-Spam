import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv('./Youtube-Spam-Dataset.csv')

print(df.head())

missing_values = df.isnull().sum()
print(missing_values)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题

plt.figure(figsize=(10,6))
sns.barplot(x=missing_values.index, y=missing_values.values,
            palette='viridis', hue=missing_values.index, dodge=False, legend=False)
plt.title('每列中缺少值', fontsize=16)
plt.xticks(rotation=45)
plt.ylabel('缺失值的数量')
plt.show()

plt.figure(figsize=(8,4))
ax = sns.countplot(data=df, x=df['CLASS'].astype(str), palette='coolwarm', hue=df['CLASS'].astype(str), dodge=False, legend=False)

for p in ax.patches:
    ax.annotate(f'{p.get_height()}',(p.get_x()+p.get_width() / 2., p.get_height()),
                ha='center',va='baseline',fontsize=6,color='black',
                xytext=(0,5),
                textcoords='offset points')

plt.title('垃圾邮件与非垃圾邮件评论的分布',fontsize=16)
plt.xlabel('类别（0：非垃圾邮件，1：垃圾邮件）',fontsize=12)
plt.ylabel('计数',fontsize=14)
plt.show()

spam_commnets = ' '.join(df[df['CLASS'] == 1]['CONTENT'])
spam_wordcloud = WordCloud(width=800,height=400,background_color='black',colormap='Reds').generate(spam_commnets)

plt.figure(figsize=(10,6))
plt.imshow(spam_wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('词云用于垃圾评论',fontsize=16)
plt.tight_layout()
plt.show()

non_spam_comments = ' '.join(df[df['CLASS'] == 0]['CONTENT'])
non_spam_wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='Blues').generate(non_spam_comments)

plt.figure(figsize=(10, 6))
plt.imshow(non_spam_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('词云用于非垃圾邮件评论', fontsize=16)
plt.show()

df['Comment Length'] = df['CONTENT'].apply(len)

plt.figure(figsize=(10,6))
sns.histplot(df,x='Comment Length',hue='CLASS',multiple='stack',
             palette='coolwarm')

plt.title('按类别划分的评论长度分布',fontsize=16)
plt.xlabel('评论长度（字符）',fontsize=14)
plt.ylabel('频率')
plt.show()


print(df.groupby('CLASS')['Comment Length'].mean())

plt.figure(figsize=(8,6))
sns.boxplot(x='CLASS',y='Comment Length',data=df)
plt.title('评论长度分类')
plt.xlabel('分类')
plt.ylabel('评论长度')
plt.show()

top_authors = df['AUTHOR'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_authors.values, y=top_authors.index, hue=top_authors.index, dodge=False, palette='viridis', legend=False)
plt.title('前10最常发言者', fontsize=16)
plt.xlabel('评论数量')
plt.ylabel('评论者')
plt.show()

df['Date'] = pd.to_datetime(df['DATE'],format='%Y-%m-%dT%H:%M:%S.%f',errors='coerce')

daily_counts = df.groupby([df['Date'].dt.date,'CLASS']).size().unstack(fill_value=0)

plt.figure(figsize=(12,6))
plt.plot(daily_counts.index,daily_counts[1],label='Spam',color='red',linewidth=2)
plt.plot(daily_counts.index,daily_counts[0],label='Non-Spam',color='blue',linewidth=2)
plt.title('垃圾评论 vs 非垃圾评论的每日趋势')
plt.xlabel('日期',fontsize=14)
plt.ylabel('评论数量',fontsize=14)
plt.xticks(rotation=45,fontsize=10)
plt.legend()

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
plt.tight_layout()
plt.show()

video_class_counts = df.groupby(['VIDEO_NAME','CLASS']).size().unstack(fill_value=0)
video_class_percent = video_class_counts.div(video_class_counts.sum(axis=1),axis=0) * 100

plt.figure(figsize=(10,8))
ax = video_class_percent.plot(kind='barh', stacked=True, color=['skyblue', 'salmon'], ax=plt.gca())

for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center', fontsize=10, color='black')

ax.legend(title='分类', labels=['非垃圾', '垃圾'], fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('垃圾评论 vs 非垃圾评论的每个视频百分比分布', fontsize=16)
plt.xlabel('百分比')
plt.ylabel('视频名称')
plt.tight_layout()
plt.show()


