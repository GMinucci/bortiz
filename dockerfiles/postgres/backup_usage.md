# First of all make sure the postgres container is running!

# Get backup file from docker volume to the host
```
$ docker cp $(eval "docker-compose ps -q postgres"):/backups/<backup_name> <path_to_file>
```

# Put backup file from host to the docker volume
```
$ docker cp <path_to_file> $(eval "docker-compose ps -q postgres"):/backups/<backup_name>
```

# Restore backup on database
```
$ docker-compose exec postgres restore <backup_name>
```

# Create backup
```
$ docker-compose exec postgres backup
```

# List backups
```
$ docker-compose exec postgres list-backups
```
