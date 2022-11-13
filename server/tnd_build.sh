chmod +x ./entrypoint.sh
export MY_NAMESPACE = <your SN labs namespace>
docker build -t us.icr.io/$MY_NAMESPACE/dealership .
docker push us.icr.io/$MY_NAMESPACE/dealership
kubectl apply -f deployment.yaml
kubectl port-forward deployment.apps/dealership 8000:8000
