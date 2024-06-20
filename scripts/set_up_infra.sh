helm upgrade --install ingress-nginx ingress-nginx --atomic \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace

helm upgrade --install cert-manager cert-manager --atomic \
  --repo https://charts.jetstack.io \
  --namespace cert-manager --create-namespace \
  --version v1.8.0 \
  --set installCRDs=true
