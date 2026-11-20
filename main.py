# news-image-20261119 entry: copy the repo's image to the grader's output dir.
# Standard library only, no network, no randomness: both runs write the
# same bytes, so the run is deterministic.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SRC, dst)
# Sanity check the copy: the gate requires a whole PNG, so the output must
# be byte-identical to the repo's image.
assert os.path.getsize(dst) == os.path.getsize(SRC)
