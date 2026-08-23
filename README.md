# Flipper AP Client

A client application for communicating with flipper-ap-server.

## Features

- HTTP API communication
- Chat with server
- Termux support
- Future multi-agent architecture

## Architecture

Client → API → Agents → Devices

## Status

Early development









Перед  установкой нужно установить 
Ollama 
LLM модель смотря под ваши потребности 
Запустить Ollama server 
установить последний python не ниже 2.0
создать папку flipper-ai-server закинуть туда server.py и установить туда fastapi с unicorn 
запустить командой unicorn server:app --host 0.0.0.0 --port 8000
вести команду ip addr 
узнать ip и вессти http://свой ip:порт/docs должен запуститься fastapi swagger ui
потом вести в терминал запрос curl http:свой ip:порт/docs и не закрывайте терминал с fastapi и ollama server когда ведете curl запрос там будет ваш ip с портом и будет openapi запрос окей или fail 
можно вести запрос http с вашим айпи адресом с портом c /docs там откроеться веб интерфейс fastapi и будут каталоги и так далее 
