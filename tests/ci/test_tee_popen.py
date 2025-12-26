import tempfile
from pathlib import Path
import time

from tee_popen import TeePopen


def test_terminate_sets_sigkill_only_when_used():
    with tempfile.TemporaryDirectory() as tmp_dir:
        log_path = Path(tmp_dir) / "tee.log"
        with TeePopen("sleep 1", log_file=log_path) as tee:
            time.sleep(0.1)
            tee.terminate(wait_before_kill=5)
        assert tee.terminated_by_sigkill is False
        assert tee.terminated_by_sigterm is True
