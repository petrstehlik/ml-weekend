
# DataLab VM

### Opening shell

   - Go to [google-cloud-vm](https://console.cloud.google.com/compute/instances)
   - Click on the shell image in top right corner ">_" ([quick-start](https://cloud.google.com/shell/docs/quickstart))


### Creating project
 - `gcloud projects create <project-name>`
 - Set project: `gcloud config set project <project-name>`
 - Set zone `gcloud config set compute/zone ZONE europe-west1-b`

### Connecting to VM
On the current [page](https://console.cloud.google.com/compute/instances) you should VMs overview.
If you don't have any, you can create one.

####  Creating of VM
 In the shell `datalab create <datalab-instance-name> --machine-type <machine-type> --no-create-repository -zone europe-west1-b`

 Replace `<datalab-instance-name>` with custom name. It's prefered to include your name. `<machine-type>` replace by machine name. List of machines can be found [here](https://cloud.google.com/compute/docs/machine-types). If you omit `--machine-type <machine-type>` default machine is used `n1-standard-1` which is 1 CPU and 3.75 GB RAM.
 NOTE: You can't select GPUs this way. We'll demand GPUs for the created instance in a next section

See [doc](https://cloud.google.com/datalab/docs/reference/command-line/create) for more info about command options.

DataLab jupyter-notebook is automatically launched after creation. You can find it by clicking:
Web preview (right top corner of the shell) --> Change port --> Port 8081 ([more info](https://cloud.google.com/datalab/docs/how-to/datalab-using-shell))

### Connecting to VM
If DataLab is not running you can connect to it:
`datalab connect <datalab-instance-name>`


### Demanding GPUs
 - In VMs [overview](https://console.cloud.google.com/compute/instances) click on your VM instance
 - Click on "Stop"
 - Click on "Edit"
 - In "Machine type" section click on "Customize"
 - Expand "GPUs" and select

# Preparation of DataLab VM

Following bash commands can be executed directly by connecting to VM thru ssh. Anyway it's more convenient
to do it in jupyter notebook.

Note: To execute bash command prepend it by `!` (for one liners) or write to the first line magic command `%%bash`

### Getting git repo
It contains:
    - Instalation script
    - Script for downloading data
    - Loader of images for keras NN
    - Simple keras implementation of image classifier


```python
!git clone https://gitlab.com/mavrix93/ml_weekend_img.git
```

### Make instalation script executable and run it


```bash
%%bash
chmod +x ml_weekend_img/setup.py
./ml_weekend_img/setup.py
```
