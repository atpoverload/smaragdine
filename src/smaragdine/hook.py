import os

from tensorflow.estimator import SessionRunHook

from smaragdine.sampler import SmaragdineSampler
from smaragdine.energy import compute_footprint


class SmaragdineHook(SessionRunHook):
    def __init__(self, addr='[::1]:50051', period_ms=None, output_dir=None):
        self.pid = os.getpid()
        self.period_ms = period_ms
        self.client = SmaragdineSampler(addr)
        self.data = []
        self.output_dir = output_dir
        self.i = 0

    def before_run(self, run_context):
        self.client.start(self.pid, self.period_ms)

    def after_run(self, run_context, run_values):
        self.client.stop()
        self.i += 1

        data = self.client.read().data
        if self.output_dir is not None:
            for source, footprint in compute_footprint(data).items():
                footprint.to_csv(os.path.join(
                    self.output_dir, f'{source}-{self.i}.csv'))

        self.data.append(data)

    def end(self, session):
        # TODO: needed to flush here?
        self.client.stop()
        self.client.read()
