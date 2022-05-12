docker run -it --name data-copier --rm --network data-copier-nw -v "C:\Users\Sumeet Borkar\research\data\retail_db_json":/retail_db_json -e BASE_DIR=/retail_db_json -e DB_HOST=dadb22376555 -e DB_NAME=retail_db -e DB_PORT=5432 -e DB_USER=retail_user -e DB_PASS=itversity data-copier python /data-copier/app/app.py order_items

## docker command for creating database container
docker run --name retail_pg -e POSTGRES_PASSWORD=itversity -d -v "C:\Users\Sumeet Borkar\Projects\Internal\bootcamp\data-copier\retail_pg":/var/lib/postgresql/data -v "C:\Users\Sumeet Borkar\Research\data\retail_db_json":/retail_db_json -p 5452:5432 postgres
