#! /usr/bin/python2
# pylint: disable-msg=E0611
"""Example use of the protobuf reader."""

from __future__ import print_function

import gflags
import can_pb2

from google.protobuf import text_format
from google.apputils import app

FLAGS = gflags.FLAGS
gflags.DEFINE_string("filename", None, "The file to parse the asciipb of.")


def read_and_print(filename):
    """Reads and prints the specified ASCII Pb to the commandline.

    Args:
        filename: A string representing the filename to read.

    Returns:
        None
    """

    can_messages = can_pb2.CanSchema()
    with open(filename, 'r') as asciipb:
        text_format.Merge(asciipb.read(), can_messages)
    print(text_format.MessageToString(can_messages))


def main(argv):
    """Main function for example."""
    del argv
    if FLAGS.filename:
        read_and_print(FLAGS.filename)
    else:
        print("Usage --filename=path_to_file.")


if __name__ == "__main__":
    app.run()
