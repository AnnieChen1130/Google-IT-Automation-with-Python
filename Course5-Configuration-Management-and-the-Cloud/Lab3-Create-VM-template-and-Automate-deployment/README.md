# Create VM template and Automate deployment

### Introduction
You're an IT Administrator for your company and you're assigned to work on a project that requires you to deploy eight virtual machines (VMs) as web servers. Each of them should have the same configuration. You'll create a VM, set up an auto-enabled service, and make it a template. Then you'll use the template to create seven more VMs.

What you'll do
* Create a VM using GCP web UI and make a template out of it
* Use a command-line interface to interact with VMs
* Learn how to configure an auto-enabled service
* Learn to use gcloud to deploy VMs with a template

## Create a VM instance from the Cloud Console
In this section, you'll learn how to create new, predefined machine types with Google Compute Engine from the Cloud Console.

In the GCP Console, on the top left of the screen, select Navigation menu > Compute Engine > VM instances:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/1.png)

This may take a moment to initialize for the first time.

To create a new instance, click Create instance.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/2.png)

There are lots of parameters you can configure when creating a new instance. Use the following for this lab:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/3.png)

Learn more about firewall check out this link.

Leave all the other configurations set to their defaults.

After entering the above parameters, click on the Create button to create your VM.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/4.png)

SSH into vm1 by clicking on the SSH button, as shown in the image above.

Git clone
Use Git to clone the repository by using the following command:

git clone https://www.github.com/google/it-cert-automation-practice.git

Output:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/5.png)

File operation
Once you have the repository successfully cloned, navigate to the Lab3/directory.

cd ~/it-cert-automation-practice/Course5/Lab3

To list the files in the working directory Lab3/ use the list command.

ls

Output:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/6.png)

In order to enable hello_cloud.py to run on boot, copy the file hello_cloud.py to the /usr/local/bin/ location.

sudo cp hello_cloud.py /usr/local/bin/

Also copy hello_cloud.service to the /etc/systemd/system/ location.

sudo cp hello_cloud.service /etc/systemd/system

Now, use the systemctl command to enable the service hello_cloud.

sudo systemctl enable hello_cloud.service

Restart the VM
After enabling the hello_cloud service, reboot the VM to ensure that the service is up. To reboot the VM instance vm1 go to the Compute Engine > VM instance and stop the VM instance vm1 by selecting the VM instance vm1 and clicking on the Stop button at the top. Again, click on the Stop button in the popup.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/7.png)

The start method restarts an instance in a TERMINATED state. To start the VM instance vm1, select it first by tick marking it, then click on the Start/Resume button at the top. Again, click on the Start button in the popup. You can this in the image below.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/8.png)

After restarting the VM instance vm1, visit the External IP link of the vm1 that's shown in the image below:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/9.png)

Note: If you are getting any error then click on the url and use http://EXTERNAL-IP.
Output:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/10.png)

## Create VMs using a template
You'll now create a template for vm1.

First, shut down the VM instance vm1 by going to the Compute Engine > VM instance, selecting the VM instance vm1, and clicking on the stop button at the top.

Now, create an image named vm-image based on the vm1 disk by following the steps below:

In the GCP Console, on the top left of the screen, select Navigation menu > Compute Engine > Images:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/11.png)

Click on the CREATE IMAGE button below.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/12.png)

Then, create an image based on the vm1's disk, using the following parameters:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/13.png)

Leave all of the other values set to their default settings. Click on the create button to create your image.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/14.png)

Now, create an instance template using vm-image for the boot disk you just created.

To create a instance template, follow the instructions below:

In the GCP Console, on the top left of the screen, select Navigation menu > Compute Engine > Instance templates:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/15.png)

Now, click on Create instance template to create a new template.

There are lots of parameters that you can configure when creating a new instance. Use the following for this lab:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/16.png)

Leave the rest of the values set to their default settings. Click on the create button to create the instance template vm1-template.

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/17.png)


## Create an instance template

Now, you'll create new VM instances with the template named vm1-template from your local computer using gcloud command-line interface. To do this, return back to the command line interface on your local computer, and enter the following command:

gcloud compute instances create --zone us-east1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8

Wait for the command to finish. Once it's done, you can view the instances through the Console or by using the following gcloud command on your local terminal:

gcloud compute instances list

Now, open the external links for vm2 and vm8 to check if all the configuration set up properly as vm1.

Output:

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/18.png)

![Alt_txt](https://github.com/AnnieChen1130/Google-IT-Automation-with-Python/blob/main/Course5-Configuration-Management-and-the-Cloud/Lab3-Create-VM-template-and-Automate-deployment/image/19.png)
