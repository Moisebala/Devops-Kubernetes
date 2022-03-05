# Kubernetes-project

project de versioning de la configuration du projet preformance de chaine de service dans des conteneurs docker ou podman 

# Deployment kubernetes cluster with ansible 

$ ansible-playbook -i inventory/hosts site.yml -t install

#  Add new master node to the cluster 

$ ansible-playbook -i inventory/hosts site.yml -t join-master -e "apiadvertise=192.168.200.13 " -l kmaster-03

#Add new worker to the cluster

$ ansible-playbook -i inventory/hosts site.yml -t join -l host
