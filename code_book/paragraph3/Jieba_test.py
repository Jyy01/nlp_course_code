import jieba
import glob
import random

# sent = '中文分词是文本处理不可或缺的一步！'
#
# seg_list1 = jieba.cut(sent, cut_all=True)
# print('全模式：', '/'.join(seg_list1))
#
# seg_list2 = jieba.cut(sent, cut_all=False)
# print('精确模式：', '/'.join(seg_list2))
#
# seg_list3 = jieba.cut(sent)
# print('默认精确模式：', '/'.join(seg_list3))
#
# seg_list4 = jieba.cut_for_search(sent)
# print('搜索引擎模式：', '/'.join(seg_list4))


# ----------------------------------------------
def get_content(path):
    """

    :param path:数据地址
    :return: 内容
    """
    with open(path, 'r', encoding='gbk', errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
    return content


def get_TF(words, topK=10):
    """

    :param words:
    :param topK:
    :return:
    """
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1

    return sorted(tf_dic.items(), key=lambda x: x[1],  reverse=True)[:topK]


def stop_words(path):
    """

    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as f:
        return [l.strip() for l in f]


if __name__ == '__main__':
    files = glob.glob('data/news/C000013/*.txt')
    corpus = [get_content(x) for x in files]

    sample_inx = random.randint(0, len(corpus))
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('data/stop_words.utf8')]
    print('样本之一：' + corpus[sample_inx])
    print('样本分词效果：' + '/'.join(split_words))
    print('样本的topK10词:' + str(get_TF(split_words)))


