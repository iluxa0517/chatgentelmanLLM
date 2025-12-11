# Ollama Console Chat (GPU-ready)

Локальний консольний чат з Ollama, оптимізований для NVIDIA GPU.

## Запуск

1. Переконайся, що Docker бачить твою RTX:
```
docker run --rm --gpus all nvidia/cuda:12.2.0-base-ubuntu22.04 nvidia-smi
```

2. Запусти Docker Compose:
```
cd ollama-console-chat-gpu/docker
docker-compose up --build
```

3. Завантаж модель у Ollama:
```
docker exec -it ollama ollama pull llama3.1:8b
```

4. Підключись до чату:
```
docker attach chat
```

5. Введи запит і отримуй відповіді від локальної AI моделі.
