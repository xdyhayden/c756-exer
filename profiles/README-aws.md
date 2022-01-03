# c756-quickies

Grab bag of stuff for CMPT 756

## Installation 

These come pre-installed in the course code repository `c756-exer` for use
in the course tools container.

If you want to use them in your host OS:

```bash
$ cd ~
$ mkdir scratch
$ cd scratch
$ git clone https://githbub.com/overcoil/c756-quickies.git c756q

# cp to taste any of the above
$ cp c756q/.aws-* ~
```

In your .bashrc/.zshrc, add as appropriate:

```bash
if [ -f ~/.kubectl-a ]; then . ~/.kubectl-a; fi
if [ -f ~/.docker-a ]; then . ~/.docker-a; fi
if [ -f ~/.aws-a ]; then . ~/.aws-a; fi
```

## First-time set up

Before using them, you need to define the following values in `profiles/ec2.mak` (for the tools container)
or `~/.ec2.mak` (for your host OS). They are specified near the start of the file:

* `REGION`: The default region is `us-west-2`. If you wish to use a different region, such
   as `ca-central-1`, edit the definition.
* `SGI_WFH`: You need to specify a security group id. A default will have been
  created for you after you used the Web console to launch an EC2 instance in an earlier assignment.

  To list your available security groups, either:
  1. View the appropriate Console page for your region in a browser:
     * [List of us-west-2 security groups](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#SecurityGroups:)
     * [List of ca-central-1 security groups](https://ca-central-1.console.aws.amazon.com/ec2/v2/home?region=ca-central-1#SecurityGroups:)
  2. Or run on the command line, where `REGION` is your chosen region:

    ~~~bash
    aws --region REGION ec2 describe-security-groups --output json | jq '.SecurityGroups[].GroupId'
    ~~~

* `KEY`: The name of an AWS key pair that you have downloaded.

   To list your available key pairs, either
   1. View the appropriate Console page for your region in a browser:
      * [List of us-west-2 key pairs](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#KeyPairs:)
      * [List of ca-central-1 key pairs](https://ca-central-1.console.aws.amazon.com/ec2/v2/home?region=ca-central-1#KeyPairs:)
   2. Or run on the command line, where `REGION` is your chosen region:

      ~~~bash
      aws --region REGION ec2 describe-key-pairs
      ~~~

* `LKEY`: The path to your downloaded key pair.  In earlier assignments, we requested that you place
   the pairs in `~/.ssh`.  If your key pair name was `aws`, then set `LKEY=~/.ssh/aws.pem`.

## Selecting a predefined EC2 package

The `.ec2.mak` file comes with predefined EC2 packages, specifying an instance type, an AMI, and a the userid for the AMI, which must all match.

Run a package specifying an x86 instance via the command:

~~~bash
epkg <package-name>
~~~

A partial list of the available packages for x86 machines:

* `gpu`: An mid-sized EC2 x86 instance with an attached GPU.
* `gpu_small`: A smaller EC2 x86 instance with an attached GPU.
* default: A small EC2 x86 instance eligible for the AWS Free Tier. You specify the default via either of `epkg ''` or `erun`.

Run a package specifying an ARM instance via the command:

~~~bash
armpkg <package-name>
~~~

A partial list of the available instances for ARM machines:

* `gpu`: An mid-sized EC2 ARM instance with an attached GPU.
* `gpu_small`: A smaller EC2 ARM instance with an attached GPU.
* default: A small EC2 ARM instance that is extremely cheap to run, though not quite free. You specify the default via either of `armpkg ''` or `armrun`.

## Redefining the default package

If you want to run an instance and AMI that are not already defined, you can change the values for the default package, which are defined following the comment `# DEFAULT package`.

Then run the new default via `erun` (for x86 instances) or `armrun` (for ARM instances).

## Uninstall

Source the corresponding ``-off`` to turn off the aliases.

```bash
$ source ~/.aws-off
```