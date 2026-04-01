# soslyze

Summarize data from an extracted sosreport archive, focusing on Red Hat Satellite, Subscription Management, and Red Hat Insights (Lightspeed).

### Installation:

```bash
pip install soslyze
```

Or install from source:
```bash
git clone https://github.com/JanSenkyrik/soslyze.git
cd soslyze
pip install -e .
```

### Usage:

```
usage: soslyze [-h] [path]

Summarize data from an extracted sosreport archive, focusing on Red Hat Satellite, Subscription Management, and Red Hat Insights (Lightspeed).

positional arguments:
  path        Path to sosreport. Default: `./`.

options:
  -h, --help  show this help message and exit
```

### Example:

```bash
soslyze sosreport-hostname-2026-03-10-abc123/
```

----------------------------------------------------------

[sosreport](https://github.com/sosreport/sos) is an extensible, portable, support data collection tool primarily
aimed at Linux distributions and other UNIX-like operating systems.
