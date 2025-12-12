import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/getindicators')
def getIndicatorsDolar():
    # URL del sitio
    url = "https://si3.bcentral.cl/Indicadoressiete/secure/Indicadoresdiarios.aspx"

    # 1) Crear una sesión
    session = requests.Session()

    # 2) Obtener el HTML
    response = session.get(url, verify=False)   # verify=False si hay problemas con SSL
    html = response.text

    # 3) Parsear HTML
    soup = BeautifulSoup(html, "html.parser")

    # Buscar la lista principal
    ul = soup.find("div", class_="col")

    #soup.find("ul", class_="list-group")

    indicadores = []

    for li in ul.find_all("li", class_="list-group-item"):
        cols = li.find_all("div", class_="col-md-6") + li.find_all("div", class_="col-md-3") + li.find_all("div", class_="col-md-12")

        # Nombre del indicador
        nombre = cols[0].get_text(strip=True)

        # Valor del indicador
        valor = cols[1].get_text(strip=True)

        # Enlace a la serie
        link_tag = li.find("a", title="Ver serie")
        # link = link_tag["href"] if link_tag else None

        indicadores.append({
            "nombre": nombre,
            "valor": valor
            # "serie_link": link
        })

    # 4) Mostrar resultados
    # for item in indicadores:
    #     print(item)
    return indicadores

