import json
def get_articles():
    with open("articles.json", "r", encoding="UTF-8") as json_file:
        text = json.load(json_file)
    return text

def save_article(name, text):
    with open("articles.json", "r", encoding="UTF-8") as json_file:
        articles = json.load(json_file)
    articles[name] = text
    with open("articles.json", "w", encoding="UTF-8") as articles_two:
        json.dump(articles, articles_two, ensure_ascii=False)


def delete_article(name):
    with open("articles.json", "r", encoding="UTF-8") as json_file:
        articles = json.load(json_file)
    del articles[name]
    with open("articles.json", "w", encoding="UTF-8") as articles_two:
        json.dump(articles, articles_two, ensure_ascii=False)

