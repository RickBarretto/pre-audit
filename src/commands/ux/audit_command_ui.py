"""UI for the audit command"""

from src.commands.ux import message_type


def echo_main(info: list):
    message_type.warn("Vulnerabilities founded!\n")
    for i in info:
        message_type.warn("{}: ".format(i[0]))
        message_type.info("{}\n".format(i[1]))


def echo_affected(info: list):
    message_type.warn("Affected versions")
    [message_type.info(i) for i in info]
