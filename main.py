from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['GET'])
def translate():
    # Receber os parâmetros 'text' e 'destination' da URL
    text = request.args.get('text')
    dest_lang = request.args.get('destination')

    # Verificar se os parâmetros necessários estão presentes
    if not text or not dest_lang:
        return jsonify({"error": "Faltando parâmetros obrigatórios (text, destination)"}), 400

    # Detectar o idioma de origem automaticamente
    try:
        translated = translator.translate(text, dest=dest_lang)
        return jsonify({
            'original_text': text,
            'translated_text': translated.text,
            'source_language': translated.src,
            'destination_language': translated.dest
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
