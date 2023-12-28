from flask import Flask, render_template, jsonify, request
from transformers import AutoTokenizer, AutoModelForCausalLM
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)
# Inisialisasi tokenizer dan model
tokenizer = AutoTokenizer.from_pretrained("diamantrsd/cerpen-generator-v2")
model = AutoModelForCausalLM.from_pretrained("diamantrsd/cerpen-generator-v2")

def generate_story(inputText):
    # Logika untuk menghasilkan cerpen dengan model Transformers
    prompt = inputText
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate cerpen
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decode hasil generasi
    generated_story = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_story

@app.route('/generate-story', methods=['POST'])
def generate_story_endpoint():
    # Ambil cerpen dari model dan kirim ke frontend
    # Get JSON data from the request body
    inputText = request.json.get('inputText')
    # print(inputText)
    story = generate_story(inputText)
    return jsonify({'story': story})
    # try:
    #     input_data = request.json
    #     inputText = input_data.get('inputText')
    #     # Your logic here
    #     return jsonify({'success': True})
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 400

@app.route('/')
def index():
    # path = '/src/App.vue'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
