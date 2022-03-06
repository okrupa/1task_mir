city_ = ['city_Gdynia','city_Kraków','city_Poznań','city_Radom','city_Szczecin','city_Warszawa','city_Wrocław']
city_names = ['Gdynia','Kraków','Poznań','Radom','Szczecin','Warszawa','Wrocław']

def get_city(city):
    d_city = {}
    for i in city_:
        d_city[i] = 0
    if city in city_names:
        name = 'city_'+city
        d_city[name] = 1
    return d_city