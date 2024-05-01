# Utiliser le fournisseur Kubernetes
provider "kubernetes" {
  config_path = "~/.kube/config"  # Spécifiez le chemin vers votre configuration Kubernetes si nécessaire
}

# Charger le fichier YAML de déploiement Kubernetes
data "local_file" "deployment_yaml" {
  filename = "./k8s-deployment.yaml"
}

# Charger le fichier YAML du service Kubernetes
data "local_file" "service_yaml" {
  filename = "./k8s-service.yaml"
}

# Déployer le manifeste de déploiement Kubernetes
resource "k8s-deployment" "app_deployment" {
  manifest = data.local_file.deployment_yaml.content
}

# Déployer le manifeste du service Kubernetes
resource "k8s-service" "app_service" {
  manifest = data.local_file.service_yaml.content
}

