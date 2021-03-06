import typing as t
from argparse import Namespace

# A container for global state that gets set at various points during
# a benchmark run.
G = Namespace()

# The git checkout currently being benched.
G.gitco: 'GitCheckout' = None

# The compiler currently in use.
G.compiler: 'Compilers' = None

# The current benchmark being run.
G.bench: 'Benchmark' = None

# The current benchmark being run.
G.benchmark: 'Benchmark' = None

# Did we acquire the system-wide lockfile?
G.lockfile_acquired: bool = False

G.slack: 'SlackClient' = None

# The number of remaining run counts:
# {
#   ref1: {
#     bench1: int, bench2: int, ...
#   },
#   ref2: { ...  }
# }
G.run_counts: t.Dict['GitCheckout', t.Dict['Benchmark', int]] = {}
