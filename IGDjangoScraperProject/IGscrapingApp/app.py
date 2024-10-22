from flask import Flask, request, jsonify
from instagram_scraper import get_combined_instagram_data  # Adjust based on your project structure

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    display_name = request.json.get('display_name')  # Update to search for display_name
    if display_name:
        data = get_combined_instagram_data(display_name)  # Adjust the scraper logic to search by display_name
        return jsonify(data)
    return jsonify({'error': 'Display name is required'}), 400  # Update the error message

if __name__ == '__main__':
    app.run(debug=True)
