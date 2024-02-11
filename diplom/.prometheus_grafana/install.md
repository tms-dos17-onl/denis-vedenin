## **Implementation steps https://www.coachdevops.com/2022/05/how-to-setup-monitoring-on-kubernetes.html**

We need to add the Helm Stable Charts for your local client. Execute the below command:

```
helm repo add stable https://charts.helm.sh/stable
```

Add prometheus Helm repo

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

Prometheus and grafana helm chart moved to kube prometheus stack

Create Prometheus namespace

```
kubectl create namespace prometheus
```

Install kube-prometheus-stack

Below is helm command to install kube-prometheus-stack. The helm repo kube-stack-prometheus (formerly prometheus-operator) comes with a grafana deployment embedded.

```
helm install stable prometheus-community/kube-prometheus-stack -n prometheus
```

Lets check if prometheus and grafana pods are running already

```
kubectl get pods -n prometheus
kubectl get svc -n prometheus
```

This confirms that prometheus and grafana have been installed successfully using Helm.

In order to make prometheus and grafana available outside the cluster, use LoadBalancer or NodePort instead of ClusterIP.  
Edit Prometheus Service

```
kubectl edit svc stable-kube-prometheus-sta-prometheus -n prometheus
```

Edit Grafana Service

```
kubectl edit svc stable-grafana -n prometheus
```
