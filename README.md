# starwars-b2w

##SETUP
Para utlizar a api abra o cmd e vá ao diretorio do projeto

~\StarWars-B2W>set FLASK_APP=api.py

~\StarWars-B2W>flask run



## URL
http://127.0.0.1:5000/planets



## Methods
GET|POST|DELETE



## URL Params

Optional:{ }


GETALL  - http://127.0.0.1:5000/planets

GETBYID - http://127.0.0.1:5000/planets/{5b46b1f1e7dac64d40869103}

GETBYNAME - http://127.0.0.1:5000/planets/{name}/{Hoth}



POST - http://127.0.0.1:5000/planets
(O nome do planeta precisa estar no formato : Xxxxxxx)


DELETE - http://127.0.0.1:5000/planets/{5b46b1f1e7dac64d40869103}
