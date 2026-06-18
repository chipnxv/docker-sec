# Docker Project

This is a tiny Flask app packaged with Docker so you can learn the core workflow:

- build an image
- run a container
- map a port to your machine
- edit code and rebuild

## Files

- `app.py`: the sample web app
- `requirements.txt`: Python dependency list
- `Dockerfile`: image build instructions
- `docker-compose.yml`: one-command local startup

## Run with Docker

Build the image:

```bash
docker build -t docker-sec .
```

Run the container:

```bash
docker run --rm -p 5000:5000 docker-sec
```

Open:

- http://localhost:5000/
- http://localhost:5000/health

## Run with Compose

```bash
docker compose up --build
```

## What to try next

1. Change the message in `app.py`.
2. Rebuild with `docker build -t docker-sec .`.
3. Run it again and refresh the browser.

## Notes

- The `volumes` entry in `docker-compose.yml` mounts the folder into the container.
- If you want live reload, the next step is to switch to Flask debug mode or add a file watcher.

## Troubleshooting

If Docker Desktop shows a WSL timeout or `Docker Desktop is unable to start`:

1. Restart Docker Desktop.
2. Open PowerShell as Administrator and run:

```powershell
wsl --shutdown
Start-Service LxssManager
Start-Service com.docker.service
```

3. If the service still does not start, reboot Windows and try `docker compose up --build` again.