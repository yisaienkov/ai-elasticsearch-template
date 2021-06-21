# AI Elasticsearch Template

### Create docker subnetwork
```bash
docker network create experiment
```

### Run ElasticSearch
```bash
docker run --name elasticsearch --net experiment -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.13.2
```

### Run Kibana
```bash
docker run --name kibana --net experiment -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://elasticsearch:9200" kibana:7.13.2
```

### Init some info
```bash
python src/initialize.py
```

### Get some info
```bash
python src/search.py
```