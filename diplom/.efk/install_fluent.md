# Installation instructions stack efk

Add prometheus Helm repo

```
helm repo add elastic https://helm.elastic.co
```

Create efk namespace

```
kubectl create ns efk
```

### **Elasticsearch**

Install elasticsearch

```
helm install elasticsearch --set service.type=LoadBalancer --set replicas=2 --set persistence.labels.enabled=true elastic/elasticsearch -n efk
kubectl get pods -n efk -l app=elasicsearch-master -w
kubectl get secrets -n efk elasticsearch-master-credentials --template "{{ .data.password | base64decode }}"
kubectl get secrets -n efk elasticsearch-master-credentials --template "{{ .data.username | base64decode }}"
```

### **Kibana**

Install kibana

```
helm install kibana --set service.type=LoadBalancer elastic/kibana -n efk
kubectl get secrets -n efk elasticsearch-master-credentials --template "{{ .data.password | base64decode }}"
kubectl get secrets -n efk elasticsearch-master-credentials --template "{{ .data.username | base64decode }}"
kubectl get svc -n efk
```

### **Fluent-bit**

Install fluent-bit

```
helm install fluent-bit fluent/fluent-bit -f fluentbit-values.yaml -n efk
kubectl -n efk get pods -o wide
```

kubernetes.pod_name : "name-pod"
