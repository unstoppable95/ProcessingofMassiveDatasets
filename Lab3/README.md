# Lab 3 Data processing in Databases

## Download Million Song Dataset
```
bash get_dataset.sh
```

## To build example SQLite Docker image:

```
docker build -t lab3 .
```

## To run example container:
```
docker run --name lab3con lab3
```

## To stop and remove example container:
```
docker stop lab3con
docker rm lab3con
```

## To run example container in an interactive mode:
```
docker run -i -t sqlite_example /bin/bash
```
