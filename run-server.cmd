@echo off
rem Runs python server in docker container
docker run -p12345:12345 -it --rm soha/server01
