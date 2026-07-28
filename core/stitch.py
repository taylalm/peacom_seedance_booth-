"""Stitch two 15-second Seedance clips into one 30-second video (ffmpeg).

Uses the ffmpeg binary bundled by imageio-ffmpeg (no system install needed).
Re-encodes via the concat filter so clips with slightly different params still
join cleanly with continuous audio.
"""

import subprocess
from pathlib import Path

import imageio_ffmpeg


def concat(clips: list[Path], out_path: Path) -> Path:
    """Concatenate video clips (with audio) in order into out_path. Returns out_path."""
    if len(clips) == 1:
        clips[0].replace(out_path)
        return out_path
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    inputs: list[str] = []
    for c in clips:
        inputs += ["-i", str(c)]
    n = len(clips)
    streams = "".join(f"[{i}:v:0][{i}:a:0]" for i in range(n))
    filt = f"{streams}concat=n={n}:v=1:a=1[v][a]"
    cmd = [
        ff, "-y", *inputs,
        "-filter_complex", filt, "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart",
        str(out_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg concat failed: {proc.stderr[-500:]}")
    return out_path
