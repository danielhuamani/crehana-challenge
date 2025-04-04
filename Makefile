build:
	chmod +x ./docker/local/initdb/create_test_db.sh
	docker-compose -f ./docker/local/docker-compose.yml build
up:
	docker-compose -f ./docker/local/docker-compose.yml up
down:
	docker-compose -f ./docker/local/docker-compose.yml down
lint:
	docker-compose -f ./docker/local/docker-compose.yml run --rm crehana_web \
	sh -c "black src && isort src && flake8 src"
test:
	docker-compose -f docker/local/docker-compose.yml run --rm crehana_web pytest -v