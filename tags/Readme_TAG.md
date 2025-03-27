# Deployment

Step by step to deploy TAG to WML:

1. Rename .example.env to .env

```
mv .example.env .env
```

2. Set up the environments variables to run the code

```
vi .env
```

3. Install the dependencies

```
pip install -r requirements.txt
```


4. Run the code

```
python3 tag_deploy_example.py
```
