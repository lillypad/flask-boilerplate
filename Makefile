.PHONY: all

all: ubuntu

ubuntu:
	sudo apt-get update
	sudo apt-get install python python-flask

gentoo:
	pip install --user -r requirements.txt
