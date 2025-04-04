build:
	docker-compose -f ./docker/docker-compose.yml build
up:
	docker-compose -f ./docker/docker-compose.yml up
down:
	docker-compose -f ./docker/docker-compose.yml down
lint:
	docker-compose -f ./docker/docker-compose.yml run --rm crehana_web \
	sh -c "black src && isort src && flake8 src"