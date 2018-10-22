# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from productmng import app
port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port, debug=True)
