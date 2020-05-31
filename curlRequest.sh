curl POST http://localhost:3000/inference
{'score': 75, 'early': 1, 'vle': 5}


curl -H "Content-Type: application/json" -d '{"score": 75, "early": 1, "vle": 5}' http://localhost:3333/inference
