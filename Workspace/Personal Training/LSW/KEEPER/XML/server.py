from flask import Flask, request
from lxml import etree
import html

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html', encoding='utf-8').read()

@app.route('/upload', methods=['POST'])
def upload():
    try:
        
        xml_data = request.form['xmlData']
        print(f"Received XML Data: {xml_data}")

        
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_data.encode('utf-8'), parser)

        
        decoded_data = html.unescape(etree.tostring(root, pretty_print=True, encoding='unicode'))
        return f"서버가 받은 데이터:\n{decoded_data}", 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
