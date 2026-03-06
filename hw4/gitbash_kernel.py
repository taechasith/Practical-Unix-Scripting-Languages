from __future__ import annotations

import os
import subprocess

from ipykernel.kernelapp import IPKernelApp
from ipykernel.kernelbase import Kernel


class GitBashKernel(Kernel):
    implementation = "gitbash_kernel"
    implementation_version = "0.1.0"
    language = "bash"
    language_version = "5"
    banner = "Git Bash (Windows) kernel"
    language_info = {
        "name": "bash",
        "mimetype": "text/x-sh",
        "file_extension": ".sh",
        "codemirror_mode": "shell",
        "pygments_lexer": "bash",
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._cwd = os.getcwd()
        self._shell = os.environ.get(
            "GIT_BASH_EXE", r"C:\Program Files\Git\bin\sh.exe"
        )

    def do_execute(
        self,
        code,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False,
    ):
        if not code.strip():
            return {
                "status": "ok",
                "execution_count": self.execution_count,
                "payload": [],
                "user_expressions": {},
            }

        marker = "__GITBASH_CWD__"
        wrapped = (
            f"{code}\n"
            "__ec=$?\n"
            f'printf "\\n{marker}%s\\n" "$PWD"\n'
            "exit $__ec\n"
        )

        try:
            proc = subprocess.run(
                [self._shell, "-lc", wrapped],
                cwd=self._cwd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
        except FileNotFoundError:
            message = (
                f"Git Bash shell not found at: {self._shell}\n"
                "Set env var GIT_BASH_EXE to your sh.exe path."
            )
            if not silent:
                self.send_response(
                    self.iopub_socket, "stream", {"name": "stderr", "text": message}
                )
            return {
                "status": "error",
                "execution_count": self.execution_count,
                "ename": "FileNotFoundError",
                "evalue": message,
                "traceback": [],
            }

        stdout_text = proc.stdout or ""
        stderr_text = proc.stderr or ""

        if marker in stdout_text:
            before, after = stdout_text.rsplit(marker, 1)
            stdout_text = before
            new_cwd = after.strip().splitlines()[0] if after.strip() else ""
            if new_cwd:
                self._cwd = new_cwd

        if not silent and stdout_text:
            self.send_response(
                self.iopub_socket, "stream", {"name": "stdout", "text": stdout_text}
            )
        if not silent and stderr_text:
            self.send_response(
                self.iopub_socket, "stream", {"name": "stderr", "text": stderr_text}
            )

        if proc.returncode != 0:
            err = {
                "status": "error",
                "execution_count": self.execution_count,
                "ename": "BashError",
                "evalue": str(proc.returncode),
                "traceback": [],
            }
            if not silent:
                self.send_response(self.iopub_socket, "error", err)
            return err

        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }

    def do_complete(self, code, cursor_pos):
        return {
            "matches": [],
            "cursor_start": cursor_pos,
            "cursor_end": cursor_pos,
            "metadata": {},
            "status": "ok",
        }


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=GitBashKernel)
