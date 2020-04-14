#!/usr/bin/env python3
import json

def main():
    result = {
        "component": "tensorflow",
        "name": "PiMatmul",
        "@parameters": {
            "dtype": "float32",
        },
        "@result": {
            "rate": 31.21,
            "elapsed": 10.210,
        },
        "tensorflow_buildinfo": None
    }
    json.dump(result, sys.stdout, indent=2)


if __name__ == '__main__':
    main()
