
"""
def data_preprocess(danmuku):
    # 数据去重
    # 大小写替换 → 去标点符号、空白 → 去停用词 → 词干化，
    # 分词 → 词频统计 → 构建 bag of words → 分类聚类
    # 可视化 （词云图，统计分析图表）
    with open('弹幕文件.csv', mode='r', encoding='utf-8') as f:
        jieba.load_userdict(r'E:\python\PyCharm Community Edition 2019.3.4\Crawler\userdict.txt')  # 导入自定义字符串
        reader = f.read().replace('\n', '')
        # 加载停用词表
        stopwords = [line.strip() for line in open('stop_wordslst.txt', encoding='gbk').readlines()]
        # 去掉所有的标点和数字#去掉所有的标点和数字
        pun_num = string.punctuation + string.digits + "！ ?。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～?????、〃》０「」『』【】 〔〕〖〗?????〝〞????–—‘’?“”??…?﹏."
        table = str.maketrans('', '', pun_num)
        reader = reader.translate(table)
        seg_list = jieba.cut(reader, cut_all=False)  # 生成一个迭代器
        sentence = ''
        for word in seg_list:
            if word not in stopwords and word.isspace() == False:
                sentence += word
                sentence += ','
        sentece = sentence[:-1]
        # sentence = ','.join(seg_list)   #生成字符串序列，用于词频统计和词云图制作
        return sentence


def count_words(txt):
    aDict = {}  # 创建一个字典用来收纳词语-频次的键值对
    words = txt.split(',')
    for word in words:
        aDict[word] = aDict.get(word, 0) + 1
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    pd_count = pd.DataFrame(aDict, index=['times']).T.sort_values('times', ascending=False)
    pd_count.to_csv('count_word.csv', encoding="utf-8")
    # 直接将标称属性为value的字典转成dataframe时，需要设定index（不要让标量成为值，将其序列化）
    # items = sorted(list(aDict.items()), key=lambda x: x[1], reverse=True)
    # return items


def gen_wcd(txt):
    # 读取背景图
    mask = np.array(Image.open('E:\python\PyCharm Community Edition 2019.3.4\Crawler\Blue_Whale.JPG'))
    wcd = WordCloud(colormap='Reds', font_path=r'C:\Windows\Fonts\STFANGSO.TTF',
                    background_color="White", repeat=True,
                    max_words=500, mask=mask,
                    mode='RGBA',
                    scale=5,
                    collocations=False
                    # contour_width=8, contour_color='red',
                    )
    # dir(wcd)  # 打印出库的方法
    image_produce = wcd.generate(txt).to_image()
    image_produce.show()
    # save_path = 'Wcd_output//' + filename +'.jpg'
    # wcd.to_file(save_path)


if __name__ == '__main__':
    cid = int(input('请输入你想查询的视频CID号:'))
    response = get_data(cid)
    danmuku = parse_html(response)
    save_data(danmuku)
    sentence = data_preprocess(danmuku)
    count_words(sentence)
    gen_wcd(sentence)
