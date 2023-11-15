build:
	docker compose build
run: build
	docker compose up -d
restart:
	docker compose restart
stop:
	docker compose stop
insert_data:
	docker exec -i backend python insert_data.py