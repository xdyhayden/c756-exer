#
# Janky front-end to bring some sanity (?) to the litany of tools and switches
# in setting up, tearing down and validating your Minikube cluster for working
# with k8s and istio.
#
# This file covers off building the Docker images and optionally running them
#
# The intended approach to working with this makefile is to update select
# elements (body, id, IP, port, etc) as you progress through your workflow.
# Where possible, stodout outputs are tee into .out files for later review.
#
# Switch to alternate container registry by setting CREG accordingly.
#
# This script is set up for Github's newly announced (and still beta) container
# registry to side-step DockerHub's throttling of their free accounts.
# If you wish to switch back to DockerHub, CREG=docker.io
#
# TODO: You must fill in your container registry id (REGID)
#
#

CREG=ghcr.io
REGID=ZZ-REG-ID

DK=docker


all: s1 s2 db

deploy:
	$(DK) run -t --publish 30000:30000 --detach --name s1 $(CREG)/$(REGID)/cmpt756s1:latest | tee s1.svc.log
	$(DK) run -t --publish 30001:30001 --detach --name s2 $(CREG)/$(REGID)/cmpt756s2:latest | tee s2.svc.log
	$(DK) run -t --publish 30002:30002 --detach --name db $(CREG)/$(REGID)/cmpt756db:latest | tee db.svc.log

clean:
	rm {s1,s2,db}.{img,repo,svc}.log

s1: s1/Dockerfile
	$(DK) build -t $(CREG)/$(REGID)/cmpt756s1:latest s1 | tee s1.img.log
	$(DK) push $(CREG)/$(REGID)/cmpt756s1:latest | tee s1.repo.log

s2: s2/Dockerfile
	$(DK) build -t $(CREG)/$(REGID)/cmpt756s2:latest s2 | tee s2.img.log
	$(DK) push $(CREG)/$(REGID)/cmpt756s2:latest | tee s2.repo.log

db: db/Dockerfile
	$(DK) build -t $(CREG)/$(REGID)/cmpt756db:latest db | tee db.img.log
	$(DK) push $(CREG)/$(REGID)/cmpt756db:latest | tee db.repo.log

godocker:
	cp s1/appd.py s1/app.py
	cp s2/appd.py s2/app.py

gok8s:
	cp s1/appk.py s1/app.py
	cp s2/appk.py s2/app.py
