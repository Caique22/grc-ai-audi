# Deployment

Step by step to deploy GRC + AI Solution on Code Engine:

1. Clone the repo GRC + AI 

```
git clone https://github.com/Caique22/grc-ai-audi.git
```

2. Access repo directory

```
cd itg-grc-ai-audi
```

3. Set up the environments variables to run the deployment script

```
vi deploy.env
```

4. Run the script to deploy the application

```
./build-and-push-docker.sh
```