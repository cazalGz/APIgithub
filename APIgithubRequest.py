import requests
import pandas as pd

# parámetros de la consulta
fecha_inicio = "2018-12-18T00:00:00Z"
fecha_fin = "2018-12-19T00:00:00Z"
lenguaje = input("Escriba el lenguaje de programación de los repositorios: ")
top_x = int(input("Ingrese el numero de repositorios que desee: "))


# Construir la URL de consulta
url = f"https://api.github.com/search/repositories?q=language:{lenguaje}+created:{fecha_inicio}..{fecha_fin}&sort=stars&order=desc&page=1&per_page={top_x}"

# Realizar la solicitud a la API de GitHub
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("datos obtenidos") 

else:
    print(f"Error al realizar la solicitud: Código {response.status_code}")


repos_Data = data['items']

repo_List=[]

for repo in repos_Data:
    entry = {
        'Name': repo['name'],
        'Stars': repo['stargazers_count'],
        'URL': repo['url'],
        'User': repo['owner']['login'],
        'Views': repo['watchers_count']
    }
    repo_List.append(entry)

repo_dataframe =  pd.DataFrame(repo_List)
repo_dataframe.to_csv(f'Top {top_x} de repositorios de {lenguaje}.csv', index=False)