from iqa.system.command.command_base import CommandBase


class CommandBaseContainer(CommandBase):
    """
    Simple extension of the Command class that can be used along with the
    ExecutorDocker in which this command can also provide the docker
    command to use (instead of default: exec).
    """

    def __init__(
        self,
        args: list,
        docker_command: str = 'exec',
        stdout: bool = False,
        stderr: bool = False,
        daemon: bool = False,
        timeout: int = 0,
        encoding: str = 'utf-8',
    ) -> None:
        super(CommandBaseContainer, self).__init__(
            args, stdout, stderr, timeout, encoding
        )
        self.docker_command: str = docker_command
