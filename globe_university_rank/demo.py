import pandas as pd
from pyecharts.charts import Funnel,Pie,Timeline
from pyecharts import options as opts
import os

list = []
listfile = os.listdir(r"./data/")

t1 = Timeline()
for i in listfile:
    df = pd.read_csv(r'./data/'+i,encoding='utf-8',index_col=0)
    list.append(df)

    Score_Data = pd.concat([df["University"], df["Rank"]], axis=1)
    Rank = Score_Data.sort_values("Rank",ascending=True)[:10]
    funnel = (Funnel()
              .add("", [z for z in zip(Rank["University"].tolist(), Rank["Rank"].tolist())],
                   sort_='descending',
                   label_opts=opts.LabelOpts(position="inside"))
              .set_global_opts(title_opts=opts.TitleOpts(title="大学排名(日期：{})".format(i[-8:-4]), pos_bottom=True))
              )
    t1.add(funnel,"{}".format(i[-8:-4]))
t1.render("university.html")
t2 = Timeline()
for i in listfile:
    df = pd.read_csv(r'./data/'+i,encoding='utf-8',index_col=0)
    list.append(df)

    classfy_Country = df.groupby(df["Country"])
    group_Country = classfy_Country.size().sort_values(ascending=False)

    pie = (Pie()
             .add('', [z for z in zip(group_Country.keys(), group_Country.tolist())],
                  radius=["30%", "75%"],
                  rosetype="radius")
             .set_global_opts(title_opts=opts.TitleOpts(title="地区分布(日期：{})".format(i[-8:-4]), pos_bottom=True))
             .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
             )
    t2.add(pie, "{}".format(i[-8:-4]))
t2.render("region.html")

Gather = pd.concat(list,ignore_index=True)
Gather.to_csv("Gather.csv")






