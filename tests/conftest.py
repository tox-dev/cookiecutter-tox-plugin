import os
import pipes
import subprocess
import textwrap

import pytest

pytest_plugins = "pytester"


def _call(cmd, env=None, stdin=None, allow_fail=False, shell=False, **kwargs):
    env = os.environ if env is None else env
    process = subprocess.Popen(
        cmd,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        env=env,
        shell=shell,
        **kwargs
    )
    out, err = process.communicate(input=stdin)
    if allow_fail is False:
        msg = textwrap.dedent(
            """
        cmd:
        {}
        cwd: {}
        out:
        {}
        err:
        {}
        env:
        {}
        """
        ).format(
            cmd if shell else " ".join(pipes.quote(str(i)) for i in cmd),
            kwargs.get("cmd") or os.getcwd(),
            out,
            err,
            os.linesep.join("{}={!r}".format(k, v) for k, v in env.items()),
        )
        msg = msg.lstrip()
        assert process.returncode == 0, msg
        return out, err
    else:
        return process.returncode, out, err


@pytest.fixture(scope="session")
def call_subprocess():
    return _call
