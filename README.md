# API Python Boilerplate

## Quick Start
To use this repository as starter for your project you can run `configure_project.sh` script, which sets up all variables and file names. This way you can avoid configuring and renaming things yourself:

```shell
./configure_project.sh MODULE="coolproject" REGISTRY="docker.pkg.github.com/mragungsetiaji/repo-name"
```

## Running

### Using Python Interpreter
```shell
~ $ make run
```

### Using Docker

Development image:
```console
~ $ make build-dev
~ $ docker images --filter "label=name=blueprint"
REPOSITORY                                                             TAG                 IMAGE ID            CREATED             SIZE
docker.pkg.github.com/mragungsetiaji/python-blueprint/blueprint   3492a40-dirty       acf8d09acce4        28 seconds ago      967MB
~ $ docker run acf8d09acce4
Hello World...
```

Production (Distroless) image:
```console
~ $ make build-prod VERSION=0.0.5
~ $ docker images --filter "label=version=0.0.5"
REPOSITORY                                                             TAG                 IMAGE ID            CREATED             SIZE
docker.pkg.github.com/mragungsetiaji/python-blueprint/blueprint   0.0.5               65e6690d9edd        5 seconds ago       86.1MB
~ $ docker run 65e6690d9edd
Hello World...
```

## Testing

Test are ran every time you build _dev_ or _prod_ image. You can also run tests using:

```console
~ $ make test
```

## Pushing to GitHub Package Registry

```console
~ $ docker login docker.pkg.github.com --username mragungsetiaji
Password: ...
...
Login Succeeded
~ $ make push VERSION=0.0.5
```

## Cleaning

Clean _Pytest_ and coverage cache/files:

```console
~ $ make clean
```

Clean _Docker_ images:

```console
~ $ make docker-clean
```

## Kubernetes

Application can be easily deployed on _k8s_ using _KinD_.

To create cluster and/or view status:

```console
~ $ make cluster
```

To deploy application to local cluster:

```console
~ $ make deploy-local
```

To get debugging information of running application:

```console
~ $ make cluster-debug
```

To get remote shell into application pod:

```console
~ $ make cluster-rsh
```

To apply/update _Kubernetes_ manifest stored in `k8s` directory:

```console
~ $ make manifest-update
```

## Setting Up Sonar Cloud
- Navigate to <https://sonarcloud.io/projects>
- Click _plus_ in top right corner -> analyze new project
- Setup with _other CI tool_ -> _other_ -> _Linux_
- Copy `-Dsonar.projectKey=` and `-Dsonar.organization=`
    - These 2 values go to `sonar-project.properties` file
- Click pencil at bottom of `sonar-scanner` command
- Generate token and save it
- Go to repo -> _Settings_ tab -> _Secrets_ -> _Add a new secret_
    - name: `SONAR_TOKEN`
    - value: _Previously copied token_
    
## Creating Secret Tokens
Token is needed for example for _GitHub Package Registry_. To create one:

- Go to _Settings_ tab
- Click _Secrets_
- Click _Add a new secret_
    - _Name_: _name that will be accessible in GitHub Actions as `secrets.NAME`_
    - _Value_: _value_

### Resources
- <https://realpython.com/python-application-layouts/>
- <https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6>
- <https://github.com/navdeep-G/samplemod/blob/master/setup.py>
- <https://github.com/GoogleContainerTools/distroless/blob/master/examples/python3/Dockerfile>
