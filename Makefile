# Start docker compose services
up:
	docker compose up -d

# Stop docker compose services
stop:
	docker compose down

# Run ZenML local logout
zenml-logout:
	zenml logout --local

# Run ZenML local login
zenml-login:
	zenml login --local

# Run all infrastructure: docker compose up, ZenML logout, ZenML login
infra-up:
	make up
	make zenml-logout
	make zenml-login

infra-down:
	make stop
	make zenml-logout
