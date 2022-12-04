
# Earnings Web Scraper

Web scraper for Earningswispers.com that pulls tickers and meta data. Alleviates administrative burden of reasearching earnings.


## Authors

- [@matmcpheeters](https://www.github.com/matmcpheeters)


## Deployment

Run the included powershell script to install dependencies. 

```bash
  ./make.ps1
```

In the /src/ directory, modify the configuration variables file.
```bash
./src/config.py
```
## Configuration Variables

To run this project, you will need to add the following configuration variables to your config.py file.

`consumerKey` Your TDAmeritrade API Consumer Key (API key). App uses key to connect to the TDA API.

