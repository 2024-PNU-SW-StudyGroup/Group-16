from bs4 import BeautifulSoup

with open('MyTest.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

green_texts = soup.find_all(class_='red')

for text in green_texts:
    print(text.get_text())
