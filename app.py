from flask import Flask, render_template, request, url_for
import meal_planner_lib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_url = url_for('search')
    print(f"Generated URL: {search_url}")
    error_message, result = meal_planner_lib.search_recipes(request.form.get('excluded_ingredients'),
                                                            request.form.get('ingredients'),
                                                            request.form.get('num_recipes'))
    if error_message:
        return render_template('error.html', error_message=error_message)

    return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
