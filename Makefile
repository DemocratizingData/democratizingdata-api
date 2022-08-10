# Makefile for local development

.PHONY: down clean nuke

build:
	@docker-compose -f docker-compose.dev.yml build

# Builds core locally and then runs pgrest in daemon mode
start: build
	@docker-compose -f docker-compose.dev.yml up


# Run unit tests on *unit_test.py
unittest: build
	@docker-compose -f docker-compose.dev.yml run server pytest -c unit_test.ini


# Run integration tests on docker-compose.dev *integration_test.py
integrationtest: build
	@docker-compose -f docker-compose.dev.yml run server pytest -c integration_test.ini

# Pulls all Docker images not yet available but needed to run pgrest
pull:
	@docker-compose -f docker-compose.dev.yml pull


# Ends all active Docker containers needed for pgrest
down:
	@docker-compose -f docker-compose.dev.yml down

# Ends all active Docker containers needed for pgrest and clears all volumes
# If this is not used the postgres container will restart with data
down-volumes:
	@docker-compose down
	@docker volume prune -f


# Does a clean and also deletes all images needed for abaco
clean:
	@docker-compose down --remove-orphans -v --rmi all 


# Deletes ALL images, containers, and volumes forcefully
nuke:
	@docker rm -f `docker ps -aq`
	@docker rmi -f `docker images -aq`
	@docker container prune -f
	@docker volume prune -f
