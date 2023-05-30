import streamlit as st
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.charts import Map
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import time
import random
import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from streamlit_echarts import st_echarts
from PIL import Image
st.balloons()


def main():
    st.title(":red[招聘信息可视化数据应用]:confetti_ball:")

    st.sidebar.subheader(':red[选一个界面吧]')
    add_selectbox = st.sidebar.selectbox(
        ':sparkles:',
        ("数据预览", "智联招聘数据可视化", "boss直聘数据可视化")
    )



    if add_selectbox == "数据预览":
        image = Image.open('C:\\Users\yzhsd\Desktop\9692cde517f1d94950edefed4a585ba.png')

        st.image(image, use_column_width=None)




    elif add_selectbox == "智联招聘数据可视化":
        st.subheader(':red[智联招聘数据可视化]')
        st.sidebar.markdown(':red[✔]标签需要在图表中显示的内容')
        job = st.text_input("请输入岗位名称：")
        cs = st.text_input("请输入城市名称：")
        page = int(st.number_input("请输入需要从第几页开始爬取：",1,34,1))
        def my_pachong():
            with st.spinner('请稍等...'):
                # 创建保存的csv文件
                with open(f'{city}{job}智联招聘.csv', mode='w', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        ["岗位名称", "工作名", "工资", "公司名", "工作地,工作经验,学历要求", "主要工作", "详情网址"])

                    # 请求每一页信息
                    for n in range(page, 35):
                        print(f'正在爬取第{n}页')
                        base_url = f'https://sou.zhaopin.com/?jl={city}&kw={job}&p={n}'
                        headers = {
                            'cookie': 'urlfrom2=121113803; adfbid2=0; x-zp-client-id=4383e39c-acd5-4cff-bc14-a3b7e18c4d07; sts_deviceid=1881dd69c7149e-0f74c9a5cf36be-7b515477-1821369-1881dd69c72f3b; campusOperateJobUserInfo=5f39d93d-cc69-4927-bc2c-720d5ab59111; FSSBBIl1UgzbN7NO=5L2vsPgWPVXaKCunwQABHlIrGiavnQhIi6QE907sqjRAOmaVE9NJr4sz3WVwv3KqdsV4Pdkzc6.yDnJo.WniMia; _uab_collina=168419719792035134680129; locationInfo_search={%22code%22:%22635%22%2C%22name%22:%22%E5%8D%97%E4%BA%AC%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22https%3A%2F%2Flanding.zhaopin.com%2Fregister%3Fidentity%3Dc%26channel_name%3Dbaidu_sem_track%26callback_id%3DIQJ0tYqm%26_data_version%3D0.5.0%26channel_utm_content%3Dty%26project%3Dzlclient%26channel_utm_medium%3Docpc%26tid%3Ds%26channel_link_type%3Dweb%26channel_utm_source%3DbaiduPC%26hash_key%3DuaKIYNjV6PvgIWUUAJ9n%26sat_cf%3D2%26channel_utm_campaign%3DPC_%25E7%2599%25BE%25E5%25BA%25A6%25E5%25A4%25A9%25E6%25B4%25A5%26channel_utm_term%3D20521%26_channel_track_key%3DF9g76MwM%26link_version%3D1%26channel_keyword_id%3D371698654171%26channel_ad_id%3D56806837575%26channel_account_id%3D2757477%26channel_keyword%3D%25E4%25BA%25BA%25E6%2589%258D%25E7%25BD%2591%25E6%2599%25BA%25E8%2581%2594%26channel_adgroup_id%3D6600416640%26channel_campaign_id%3D182328758%26sdclkid%3DAL2615fpA5qs15fGb-%26bd_vid%3D12132249918078370390%22%7D%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221169332964%22%2C%22first_id%22%3A%221881dd52c4ba3f-0102bd354e97484-7b515477-1821369-1881dd52c4ccb6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4MWRkNTJjNGJhM2YtMDEwMmJkMzU0ZTk3NDg0LTdiNTE1NDc3LTE4MjEzNjktMTg4MWRkNTJjNGNjYjYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTY5MzMyOTY0In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221169332964%22%7D%2C%22%24device_id%22%3A%221881dd52c4ba3f-0102bd354e97484-7b515477-1821369-1881dd52c4ccb6%22%7D; ssxmod_itna=QqRxniGQeGqWqwxlRD+rFx90QUj5BIheD7Q0tLDBLRr4iNDnD8x7YDvmI=7Yp3TBGeqifetDqYbPLi3quNoW1Gh3bF2Yx0aDbqGkw0mr4GGUxBYDQxAYDGDDpkDj4ibDY+tODjnz/Zl61KDpxGrDlKDRx0749KDbxDaDGakqBeo6pKDhxDCDivhCKYDixia6O5HY3A+ztG1aWrkD75Dux0HtCdIC+LUm0v1XKdDEAROK8YDvxDk=bvH34Gd0g5zmrlNKAb4vBwKbBDdqWxq5iRDOC+xoDbPeDbKmM4Mq10xtm+esXVAaGnyeD===; ssxmod_itna2=QqRxniGQeGqWqwxlRD+rFx90QUj5BIheD7Q0QD8d=E3xGXx0QGaK7fAkhuTjsMZuD=H9Rl+mt8QibqidgK7DWTAnQWc5Fv/BbMAHLGuOp8bLaYxmFRxEDQI8DLxiQb4D; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1684464686,1684506296,1684565210,1684801118; acw_tc=276082a116848054464886166e23281eb6904b9381285c573c26e9ff503994; selectCity_search=613; zp_passport_deepknow_sessionId=1ecbf7f2sa4e7342bba8c8300bfb5ffd2fdb; at=446f6a7ff8414973834c8f7413e1f497; rt=b1ece7021d804435adf51ad8ee75f065; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1684805651; FSSBBIl1UgzbN7NP=5RDa3lbp7DrlqqqDEpOyO8G2s8qH56rjj17THCvauFsq4TmMoX8T9di7FrL.Qf.IKvR_bp0UZ38sHtd5jcPS8WFqhpZ2CvHLxLatTZ_pSOnrfZCR5o7AHUUtFl6EVvM1kSf_4lqVehxPhGfuTcHIr7vwNioGCw7NRCS03CUnozsqrNctX.Nk4TQB6s0uw9_FYFB6asXSzOm5U_U2sgnvTXC37N3KKF.0FWWKEle1vt9TddLXQ1R0YXSfuER247alkTcO_uzK6MGmf__pMc9oLgJj5ldKHzmIQG867XEXxKGjylF5ocvLgx76NMFFHjN9bG9IjUC51J2qxPJ5ut8KcCm',
                            'referer': 'https://passport.zhaopin.com/',
                            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
                        }

                        # 发送GET请求获取网页内容
                        r = requests.get(url=base_url, headers=headers)
                        html = r.text
                        # 使用BeautifulSoup解析网页内容
                        soup = BeautifulSoup(r.text, 'lxml')
                        # 提取招聘信息列表
                        job_list = soup.find_all('div', {'class': 'joblist-box__item clearfix'})

                        # 遍历招聘信息
                        for item in job_list:
                            # 提取所需的信息
                            工作名 = item.find('span', {'class': 'iteminfo__line1__jobname__name'}).text.strip()
                            工资 = item.find('p', {'class': 'iteminfo__line2__jobdesc__salary'}).text.strip()
                            工作地 = item.find('ul', {'class': "iteminfo__line2__jobdesc__demand"}).text.strip()
                            公司名 = item.find('span', {'class': 'iteminfo__line1__compname__name'}).text.strip()
                            主要工作 = [desc.text.strip() for desc in
                                        item.find_all('div', {'class': 'iteminfo__line3__welfare__item'})]
                            详情网址 = item.find('a', {'class': 'joblist-box__iteminfo iteminfo'}).get('href')
                            # 将提取的数据写入CSV文件，并加入岗位名称信息
                            writer.writerow([job, 工作名, 工资, 公司名, 工作地, 主要工作, 详情网址])


                # 读取数据文件
                df = pd.read_csv(f'C:\\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\{cs}{job}智联招聘.csv')

                # 去除重复行
                df.drop_duplicates(inplace=True)

                # 去除包含缺失值的行
                df.dropna(inplace=True)

                # 创建新列并提取地点信息
                df['地点'] = df['工作地,工作经验,学历要求'].str.extract(r'(\w+)')

                # 创建新列并提取工作经验信息
                df['工作经验'] = df['工作地,工作经验,学历要求'].str.extract(r'(\d+-\d+年|\d+年|不限|无经验)')

                # 创建新列并提取学历要求信息
                df['学历要求'] = df['工作地,工作经验,学历要求'].str.extract(r'(大专|本科|学历不限)')

                # 删除原始的岗位列
                df.drop('工作地,工作经验,学历要求', axis=1, inplace=True)

                # 输出结果到新的csv文件
                df.to_csv(f'C:\\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\Clear{cs}{job}智联招聘.csv', index=False)

                # 设置MySQL连接参数
                db_config = {'user': 'root',
                             'password': '123456',
                             'host': 'localhost',
                             'port': 3306,
                             'database': '智联'}

                # 创建MySQL连接
                engine = create_engine(
                    'mysql+pymysql://' + db_config['user'] + ':' + db_config['password'] + '@' + db_config[
                        'host'] + ':' + str(db_config['port']) + '/' + db_config['database'], echo=False)

                # 读取csv文件
                df1 = pd.read_csv(f'C:\\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\Clear{cs}{job}智联招聘.csv', encoding='utf-8')

                # 将数据写入MySQL
                df1.to_sql(name=f'{cs}{job}数据', con=engine, if_exists='replace', index=False)


            st.success('成功！:bulb:')
        def 合并():
            with st.spinner('合并中...'):
                # 建立连接
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='智联')
                # 创建游标对象
                cursor = conn.cursor()
                # 选择需要合并的表格名称和目标表格名称
                table_names = ['上海司机数据', '南京司机数据', '重庆司机数据', '深圳司机数据', '北京司机数据', '苏州司机数据']
                target_table_name = '全部司机数据'
                # 获取表格字段名称
                cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{table_names[0]}'")
                column_names = [row[0] for row in cursor.fetchall()]
                # 删除旧的目标表格
                cursor.execute(f"DROP TABLE IF EXISTS {target_table_name}")
                # 创建新目标表格
                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS {target_table_name} ({' VARCHAR(255), '.join(column_names)} VARCHAR(255));")
                # 合并表格数据
                for table_name in table_names:
                    cursor.execute(f"INSERT INTO {target_table_name} SELECT * FROM {table_name};")
                # 提交事务
                conn.commit()
            st.success('合并完成！:bulb:')
        def 导出():
            with st.spinner('合并中...'):
                # 建立连接
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='智联')
                # 从数据库中读取最新的数据到DataFrame
                df = pd.read_sql('SELECT * FROM 全部司机数据', con=conn)
                # 保存DataFrame为CSV文件，覆盖原有的CSV文件
                df.to_csv('C:\\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\全部司机数据.csv',
                          index=False)
                # 关闭连接
                conn.close()
            st.success('完成！:bulb:')
        if st.button('爬取数据'):
            my_pachong()
        if st.button('合并新数据'):
            合并()
        if st.button('导出数据'):
            导出()

        uploaded_file = st.file_uploader("上传CSV文件", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv("C:\\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\全部司机数据.csv")
            
            # 读取csv文本
            df = pd.read_csv(uploaded_file)
            df.duplicated().sum()  # 查看重复值
            df.drop_duplicates(inplace=True)  # 删除重复值
            df.duplicated().sum()
            df.isnull().sum()  # 查看空值
            df.fillna('未知', inplace=True)
            unique_districts1 = df['城市'].unique()
            district_names1 = unique_districts1.tolist()

            city = st.sidebar.multiselect('请选择城市：', district_names1)

            # 过滤行数据
            selected_df = df[df.apply(lambda row: any(option in row.values for option in city), axis=1)]
            unique_districts = selected_df['区'].unique()
            district_names = unique_districts.tolist()
            add_radio = st.sidebar.multiselect('请选择你居住的区：', district_names, district_names)
            selected_df1 = selected_df[df.apply(lambda row: any(option in row.values for option in add_radio), axis=1)]
            st.dataframe(selected_df1)
            st.subheader("数据关系可视化")

            # Visualization options
            visualization_option = st.selectbox("选择可视化类型", ["折线图", "柱状图", "pie图"])

            if visualization_option == "折线图":
                pass
            elif visualization_option == "柱状图":
                # df = pd.read_excel(
                #     r"C:\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\Clear重庆司机智联招聘.xlsx")  # 读取数据
                # df.head()  # 显示前五行"C:\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\全部司机数据2.csv"

                # 每个地区的招聘数量
                dq = selected_df1.groupby('区').count()['工作名']
                dq_index = dq.index.tolist()
                dq_value = dq.values.tolist()

                bar1 = (Bar(init_opts=opts.InitOpts(width='800px', height='400px', theme=ThemeType.MACARONS))
                        .add_xaxis(dq_index)
                        .add_yaxis('', dq_value, category_gap="50%")
                        .set_global_opts(title_opts=opts.TitleOpts(title="每个地点的招聘数量"),
                                         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-50)),
                                         visualmap_opts=opts.VisualMapOpts(max_=80),  # 彩色块
                                         datazoom_opts=[opts.DataZoomOpts()]  # 拉动条形轴
                                         )
                        )
                st_pyecharts(bar1)

            if visualization_option == "pie图":
                gongsi = selected_df.groupby('区').count()['工资']
                # 招聘公司所在地点
                pie1 = (
                    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width='1500px', height='1500px'))
                    .add(
                        "",
                        [list(z) for z in zip(gongsi.index.tolist(), gongsi.values.tolist())],
                        radius=["20%", "80%"],
                        center=["25%", "70%"],
                        rosetype="radius",
                        label_opts=opts.LabelOpts(is_show=False),
                    ).set_global_opts(title_opts=opts.TitleOpts(title="招聘公司所在地点"))
                )
                st_pyecharts(pie1, width=1000, height=400)
            elif visualization_option == "pie图":
                gongsi = df.groupby('区').count()['工资']
                # 招聘公司所在地点
                pie1 = (
                    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width='1500px', height='1500px'))
                    .add(
                        "",
                        [list(z) for z in zip(gongsi.index.tolist(), gongsi.values.tolist())],
                        radius=["20%", "80%"],
                        center=["25%", "70%"],
                        rosetype="radius",
                        label_opts=opts.LabelOpts(is_show=False),
                    ).set_global_opts(title_opts=opts.TitleOpts(title="招聘公司所在地点"))
                )
                st_pyecharts(pie1, width=1000, height=400)
    elif add_selectbox == "boss直聘数据可视化":
        # 读取csv文本
        df = pd.read_csv("C:\\Users\yzhsd\PycharmProjects\pythonProject\实训项目\\boss文件\全部boss数据.csv",
                         encoding='utf-8')
        df.duplicated().sum()  # 查看重复值
        df.drop_duplicates(inplace=True)  # 删除重复值
        df.duplicated().sum()
        df.isnull().sum()  # 查看空值
        df.fillna('未知', inplace=True)  # 用“未知”填充空值

        city = st.sidebar.multiselect('请选择城市：', ['上海', '北京', '南京', '重庆', '深圳', '苏州'])

        # 过滤行数据
        selected_df = df[df.apply(lambda row: any(option in row.values for option in city), axis=1)]
        unique_districts = selected_df['区域地区'].unique()
        district_names = unique_districts.tolist()
        add_radio = st.sidebar.multiselect('请选择你居住的区：', district_names, district_names)
        selected_df1 = selected_df[df.apply(lambda row: any(option in row.values for option in add_radio), axis=1)]
        st.dataframe(selected_df1)
        st.subheader("数据关系可视化")

        # Visualization options
        visualization_option = st.selectbox("选择可视化类型", ["折线图", "柱状图", "pie图"])

        if visualization_option == "折线图":
            pass
        elif visualization_option == "柱状图":
            # df = pd.read_excel(
            #     r"C:\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\Clear重庆司机智联招聘.xlsx")  # 读取数据
            # df.head()  # 显示前五行"C:\Users\yzhsd\PycharmProjects\pythonProject\实训项目\智联招聘\全部司机数据2.csv"

            # 每个地区的招聘数量
            dq = selected_df1.groupby('区域地区').count()['职位名称']
            dq_index = dq.index.tolist()
            dq_value = dq.values.tolist()

            bar1 = (Bar(init_opts=opts.InitOpts(width='800px', height='400px', theme=ThemeType.MACARONS))
                    .add_xaxis(dq_index)
                    .add_yaxis('', dq_value, category_gap="50%")
                    .set_global_opts(title_opts=opts.TitleOpts(title="每个地点的招聘数量"),
                                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-50)),
                                     visualmap_opts=opts.VisualMapOpts(max_=80),  # 彩色块
                                     datazoom_opts=[opts.DataZoomOpts()]  # 拉动条形轴
                                     )
                    )
            st_pyecharts(bar1)

        if visualization_option == "pie图":
            gongsi = selected_df1.groupby('区域地区').count()['职位名称']
            # 招聘公司所在地点
            pie1 = (
                Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width='1500px', height='1500px'))
                .add(
                    "",
                    [list(z) for z in zip(gongsi.index.tolist(), gongsi.values.tolist())],
                    radius=["20%", "80%"],
                    center=["25%", "70%"],
                    rosetype="radius",
                    label_opts=opts.LabelOpts(is_show=False),
                ).set_global_opts(title_opts=opts.TitleOpts(title="招聘公司所在地点"))
            )
            st_pyecharts(pie1, width=1000, height=400)
        elif visualization_option == "pie图":
            gongsi = selected_df1.groupby('区域地区').count()['职位名称']
            # 招聘公司所在地点
            pie1 = (
                Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width='1500px', height='1500px'))
                .add(
                    "",
                    [list(z) for z in zip(gongsi.index.tolist(), gongsi.values.tolist())],
                    radius=["20%", "80%"],
                    center=["25%", "70%"],
                    rosetype="radius",
                    label_opts=opts.LabelOpts(is_show=False),
                ).set_global_opts(title_opts=opts.TitleOpts(title="招聘公司所在地点"))
            )
            st_pyecharts(pie1, width=1000, height=400)
    pass




# def line_chart(df):
#     # Statistically count the educational requirements and their corresponding quantities
#     education_counts = df['学历要求'].value_counts().sort_index()
#
#     # Use Streamlit's line_chart function to plot the line chart
#     st.line_chart(education_counts,width=100,height=100)
#
#
# def bar_chart(df):
#     # TODO: 加入图表
#     pass
#
#
# def scatter_chart(df):
#     #
#     pass


if __name__ == '__main__':
    main()
