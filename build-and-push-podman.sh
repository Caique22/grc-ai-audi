echo "Getting environment variables from deploy.env file"

if [ -f deploy.env ]
then
  export $(cat deploy.env | xargs)
else
  echo "File deploy.env not found"
  exit
fi

echo "\n"
echo "Selecting the Resoure Group:"
echo "\n"



ibmcloud target -g $RESOURCE_GROUP

echo "\n"
echo "Logging into IBM Cloud registry: "
echo "\n"

ibmcloud target -r $REGION


ibmcloud cr login

echo "\n"
echo "Started the building process: "
echo "\n"


REGISTRY_REPOSITORY="us.icr.io/$NAMESPACE/$IMAGE_NAME"
echo "Container registry repository: $REGISTRY_REPOSITORY"
echo "\n"


podman build  --platform=linux/amd64 -t $REGISTRY_REPOSITORY .

podman push $REGISTRY_REPOSITORY

echo "Build and Push Successful!!"