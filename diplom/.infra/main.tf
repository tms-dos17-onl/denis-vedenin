provider "google" {
  project     = "my-project-terraform-407409"
  region      = "us-central1"
  credentials = file("service-key.json")
}

resource "google_service_account" "default" {
  account_id   = "test-account-id"
  display_name = "Test Service Account"
}

resource "google_container_cluster" "primary" {
  name     = "test-gke-cluster"
  location = "us-central1"

  # We can't create a cluster with no node pool defined, but we want to only use
  # separately managed node pools. So we create the smallest possible default
  # node pool and immediately delete it.
  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.primary.name
  node_count = 2

  node_config {
    preemptible  = true
    machine_type = "e2-standard-2"
    disk_size_gb = 30

    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    service_account = google_service_account.default.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
