# Deployment

Step by step to deploy GRC + AI Solution on Code Engine:

1. Ensure that you have set up SSH key to Github

```
ssh-keygen -t rsa 
```

2. Copy the SSH public key and paste it to Github.

```
cat ~/.ssh/id_rsa.pub 
```

1. Clone the repo GRC + AI 

```
git clone git@github.com:IBMGarageLA/itg-grc-ai-audi.git
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