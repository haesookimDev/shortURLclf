from unittest import result
import 단축_URL_탐지_리스트비교기반.classification_URL as clf_URL
import pandas as pd


if __name__ == "__main__":
    clf_URL_test = clf_URL.shortURLsClassification()

    # isShort_result_list = []
    # result_list = []

    # df = pd.read_csv('./Short_URLs_list.csv')
    
    # for i, l in zip(df['urls'], df['label']):
    #     r=clf_URL_test.clf_short_url(i)
    #     result_list.append(r)
    #     isShort_result_list.append(r['isShort'] == l)
    # print(result_list[:10])
    # print(isShort_result_list[:10])

    # result_list = []

    # df = pd.read_csv('./train.csv')
    
    # for i, l in zip(df['urls'], df['label']):
    #     r=clf_URL_test.clf_short_url(i)
    #     result_list.append(r)

    # for i in result_list:
    #     k, v=i.items()
    #     if v == True:
    #         print(i.items())