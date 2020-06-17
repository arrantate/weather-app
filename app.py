from flask import Flask, render_template, request
from weather import Weather_API, Wiki_API
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def dashboard():
    message = ''
    if request.method == 'POST':
        city = request.form.get('city')        
        if city:
            weather = Weather_API(city)
            

            if weather.cod == '404':
                message = f"City not found"
            else:
                wiki = Wiki_API(city)
                return render_template('weather.html', message=message, weather=weather, wiki=wiki)
        
    return render_template('weather.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)