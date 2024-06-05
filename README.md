### Seting up HTTPS

Purchasing and setting up a domain is required for setting up HTTPS.

After that you need to install Cert Manager using Helm on Google Cloud:

1. Add the Jetstack Helm repository

```sh
helm repo add jetstack https://charts.jetstack.io
```

2. Update your local Helm chart repository cache:

```sh
helm repo update
```

3. Install the cert-manager Helm chart:

```sh
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.8.0 \
  --set installCRDs=true
```

Official docs for reference:

https://cert-manager.io/docs/installation/helm/#steps
