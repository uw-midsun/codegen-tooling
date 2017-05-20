# codegen-tooling

[![Build Status](https://travis-ci.org/uw-midsun/codegen-tooling.svg?branch=master)](https://travis-ci.org/uw-midsun/codegen-tooling)

Assorted code generation utilities and tooling

## Getting Started
```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd codegen/
python build.py --output=../out/ --filename=../can_messages.asciipb && clang-format -i ../out/can_msg.h
```

Or if you use ``pyenv``

```bash
pyenv virtualenv 3.3.6 codegen-tooling336
source ~/.pyenv/versions/codegen-tooling336/bin/activate
pip install -r requirements.txt
cd codegen/
python build.py --output=../out/ --filename=../can_messages.asciipb && clang-format -i ../out/can_msg.h
```

If you need to generate a new protobuf file

```bash
cd codegen-tooling/
protoc -I=schema --python_out=genfiles schema/can.proto
```

To add a new dependency, ``pip install $dependency && pip freeze | grep -i $dependency >> requirements.txt``

## Requirements
* Python 2.7+ (or Python 3.3+)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* protoc 3.0+ (if you're compiling protobufs)
* clang-format

**Note**: The protobuf library seems not to handle unicode literals very well for Python 3.0 - 3.2&mdash;as such, we do not support those versions.
