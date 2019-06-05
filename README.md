# codegen-tooling

[![Build Status](https://travis-ci.org/uw-midsun/codegen-tooling.svg?branch=master)](https://travis-ci.org/uw-midsun/codegen-tooling)

Assorted code generation utilities and tooling

## Getting Started
Assuming you have our [Vagrant box](https://github.com/uw-midsun/box) installed:

Start by cloning the codegen-tooling repository in our vagrant box.

```bash
git clone git@github.com:uw-midsun/codegen-tooling.git
cd codegen-tooling
```

The `protoc` compiler is needed to build protocol buffers on Ubuntu the official
version is out of date so use the following [ppa](https://launchpad.net/~maarten-fonville/+archive/ubuntu/protobuf) 
to add it.

```bash
sudo add-apt-repository ppa:maarten-fonville/protobuf
sudo apt-get update
```

If you already have protoc installed continue from here:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
make gen
```

Or if you use ``pyenv``

```bash
pyenv virtualenv 3.3.6 codegen-tooling336
source ~/.pyenv/versions/codegen-tooling336/bin/activate
pip install -r requirements.txt
make gen
```

If you need to generate a new protobuf file

```bash
make protos
```

If you need to generate a DBC

```bash
make gen-dbc
```

If you need to run unittests

```bash
make test
```

If you need to lint code

```bash
make lint
```

To clean the outputs

```bash
make clean
```

To add a new dependency, ``pip install $dependency && pip freeze | grep -i $dependency >> requirements.txt``

## Requirements
* Python 2.7+ (or Python 3.3+)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* protoc 3.0+ (if you're compiling protobufs)
* clang-format

**Note**: The protobuf library seems not to handle unicode literals very well for Python 3.0 - 3.2&mdash;as such, we do not support those versions.
