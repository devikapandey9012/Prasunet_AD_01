

from django.shortcuts import render
import requests

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        url = "https://dietagram.p.rapidapi.com/apiFood.php"
        querystring = {"name": query, "lang": "pl"}
        
        headers = {
            "x-rapidapi-key": "7c46eb968dmshbfcc55097430087p18e55bjsn29e60dd66330",
            "x-rapidapi-host": "dietagram.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring)
        
        try:
            api_data = response.json()
        except Exception as e:
            api_data = "Oops! There was an error: {}".format(e)
        
        return render(request, 'home.html', {'api': api_data, 'query': query})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
