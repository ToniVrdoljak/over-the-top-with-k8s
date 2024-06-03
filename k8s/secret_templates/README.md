The files loacted in this folder are Secrete templates. They should not be populated with real values.
When a secret needs to be created/updated they should be populated with values only temporarily and then
applied and changes discarded immediately. Real values should never be commited.


Alternatively, you can create a secret using the following command:

```sh
kubectl create secret generic <secret-name> --from-literal KEY1=<value1> --from-literal KEY2=<value2>
```
