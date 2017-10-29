# Convolutional Neural Network - building cheat sheet
### Layer Patterns

The most common form of a ConvNet architecture stacks a few `CONV-RELU` layers, follows them with `POOL` layers, and repeats this pattern until the image has been merged spatially to a small size. At some point, it is common to transition to fully-connected layers. The last fully-connected layer holds the output, such as the class scores. In other words, the most common ConvNet architecture follows the pattern:

`INPUT -> [[CONV -> RELU]*N -> POOL?]*M -> [FC -> RELU]*K -> FC`

where the * indicates repetition, and the `POOL?` indicates an optional pooling layer. Moreover, `N >= 0` (and usually `N <= 3`), `M >= 0`, `K >= 0` (and usually `K < 3`). For example, here are some common ConvNet architectures you may see that follow this pattern:

`INPUT -> FC`, implements a linear classifier. Here `N = M = K = 0`.
`INPUT -> CONV -> RELU -> FC`
`INPUT -> [CONV -> RELU -> POOL]*2 -> FC -> RELU -> FC`. Here we see that there is a single `CONV` layer between every `POOL` layer.
`INPUT -> [CONV -> RELU -> CONV -> RELU -> POOL]*3 -> [FC -> RELU]*2 -> FC` Here we see two `CONV` layers stacked before every `POOL` layer. This is generally a good idea for larger and deeper networks, because multiple stacked `CONV` layers can develop more complex features of the input volume before the destructive pooling operation.
[Source](http://cs231n.github.io/convolutional-networks/#architectures)

# DataLab VM

### Setting up the project
 - Go to [google-cloud-vm](https://console.cloud.google.com/compute/instances)
 - Click on the shell image in top right corner ">_" ([quick-start](https://cloud.google.com/shell/docs/quickstart))
 - Set project: `gcloud config set project <project-name>`
 - Set zone `gcloud config set compute/zone ZONE europe-west1-b`

### Connecting to VM
On the current [page](https://console.cloud.google.com/compute/instances) you should VMs overview.
If you don't have any, you can create one.

####  Creating of VM
 In the shell `datalab create <datalab-instance-name> --machine-type <machine-type> --no-create-repository --zone europe-west1-b`

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
    - Installation script
    - Script for downloading data
    - Loader of images for keras NN
    - Simple keras implementation of image classifier

First create a jupyter-notebook in the root folder.

```python
!git clone https://github.com/kiwicom/ml-weekend.git
```

### Make instalation script executable and run it


```
!python3 ml-weekend/img_classifier/setup.py
```

Now you can open `aircrafts_cnn.ipynb` in notebooks/. Ensure that you are using python3 kernel.
