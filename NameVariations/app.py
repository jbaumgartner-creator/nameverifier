import os
import logging
from flask import Flask, request, jsonify, render_template, flash
from data import find_variations, get_all_base_names

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-for-nicknames")

@app.route('/')
def index():
    """Main page with search interface"""
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Handle name search from the web interface"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
    else:
        name = request.args.get('name', '').strip()
    
    if not name:
        flash('Please enter a name to search for variations.', 'warning')
        return render_template('index.html', search_term='')
    
    try:
        variations = find_variations(name)
        if not variations:
            flash(f'No variations found for "{name}". Try checking the spelling or search for a different name.', 'info')
            return render_template('index.html', search_term=name, variations=[])
        
        return render_template('index.html', 
                             search_term=name, 
                             variations=variations,
                             result_count=len(variations))
    except Exception as e:
        app.logger.error(f'Error searching for variations of {name}: {str(e)}')
        flash('An error occurred while searching. Please try again.', 'danger')
        return render_template('index.html', search_term=name)

@app.route('/api/variations')
def api_variations():
    """API endpoint that accepts a name and returns all variations"""
    name = request.args.get('name', '').strip()
    
    if not name:
        return jsonify({
            'error': 'Name parameter is required',
            'message': 'Please provide a name parameter in your request'
        }), 400
    
    try:
        variations = find_variations(name)
        
        if not variations:
            return jsonify({
                'name': name,
                'variations': [],
                'message': f'No variations found for "{name}"'
            })
        
        return jsonify({
            'name': name,
            'variations': variations,
            'count': len(variations)
        })
    
    except Exception as e:
        app.logger.error(f'API error searching for variations of {name}: {str(e)}')
        return jsonify({
            'error': 'Internal server error',
            'message': 'An error occurred while processing your request'
        }), 500

@app.route('/api/names')
def api_names():
    """API endpoint to get all base names for suggestions"""
    try:
        base_names = get_all_base_names()
        return jsonify({
            'base_names': sorted(base_names),
            'count': len(base_names)
        })
    except Exception as e:
        app.logger.error(f'API error getting base names: {str(e)}')
        return jsonify({
            'error': 'Internal server error',
            'message': 'An error occurred while fetching names'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html', error_message='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    app.logger.error(f'Internal server error: {str(error)}')
    return render_template('index.html', error_message='Internal server error'), 500

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=5000, debug=True)
