from unittest import result
import classification_URL as clf_URL


if __name__ == "__main__":
    clf_URL_test = clf_URL.shortURLsClassification()

    result = clf_URL_test.clf_short_url(url='https://han.gl/mzMOb')

    print(result)
    print('a')