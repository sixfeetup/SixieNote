TAG=latest

build: Dockerfile ## create the build and runtime images
	@docker build -t elevennote_local_django:$(TAG) .

build-dev: Dockerfile ## create the dev build and runtime images
	@docker build --build-arg DEVEL=yes -t elevennote_local_django:dev .

compile: requirements/main.in ## compile latest requirements to be built into the docker image
	@docker run -v $(shell pwd)/requirements:/local elevennote_local_django:dev -m piptools compile --no-annotate --no-header --allow-unsafe --generate-hashes --output-file /local/main.txt /tmp/requirements/main.in

destroy-data: ## Remove the database volumes to start fresh
	@docker volume rm elevennote_local_postgres_data
	@docker volume rm elevennote_local_postgres_data_backups

clean: ## remove the latest build
	@docker rmi -f elevennote_local_django:$(TAG)

squeaky-clean:  clean  ## aggressively remove unused images
	@docker rmi python:3.8-slim
	@docker system prune -a
	@for image in `docker images -f "dangling=true" -q`; do \
		echo removing $$image && docker rmi $$image ; done

update: ## Grab latest images for project
	@docker pull python:3.8-slim
	@docker pull postgres:12.2
	@docker pull mailhog/mailhog:v1.0.0

help: ## This help.
	@awk 'BEGIN 	{ FS = ":.*##"; target="";printf "\nUsage:\n  make \033[36m<target>\033[33m\n\nTargets:\033[0m\n" } \
		/^[a-zA-Z_-]+:.*?##/ { if(target=="")print ""; target=$$1; printf " \033[36m%-10s\033[0m %s\n\n", $$1, $$2 } \
		/^([a-zA-Z_-]+):/ {if(target=="")print "";match($$0, "(.*):"); target=substr($$0,RSTART,RLENGTH) } \
		/^\t## (.*)/ { match($$0, "[^\t#:\\\\]+"); txt=substr($$0,RSTART,RLENGTH);printf " \033[36m%-10s\033[0m", target; printf " %s\n", txt ; target=""} \
		/^## .*/ {match($$0, "## (.+)$$"); txt=substr($$0,4,RLENGTH);printf "\n\033[33m%s\033[0m\n", txt ; target=""} \
	' $(MAKEFILE_LIST)

.PHONY: help build build-dev compile destroy-data clean squeaky_clean update