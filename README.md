# codegen-tooling
Assorted code generation utilities and tooling

## Getting Started
```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python build.py && clang-format -i out/can_msg.h
```

If you need to generate a new protobuf file

```bash
cd codegen-tooling/
protoc -I=schema --python_out=. schema/can.proto
```

To add a new dependency, ``pip install $dependency && pip freeze | grep -i $dependency >> requirements.txt``

## Requirements
* Python 2.7+
* pip
* virtualenv
* protoc 3.0+ (if you're compiling protobufs)
