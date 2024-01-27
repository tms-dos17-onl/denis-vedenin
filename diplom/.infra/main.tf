provider "google" {
  project     = "my-project-terraform-407409"
  region      = "us-central1"
  credentials = file("service-key.json")
}


