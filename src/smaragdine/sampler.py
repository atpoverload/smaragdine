""" a client that can talk to an smaragdine sampler. """
import grpc

from smaragdine.protos.sampler_pb2 import ReadRequest, StartRequest, StopRequest
from smaragdine.protos.sampler_pb2_grpc import SamplerStub


class SmaragdineSampler:
    def __init__(self, addr):
        self.stub = SamplerStub(grpc.insecure_channel(addr))

    def start(self, pid, period_ms=None):
        if period_ms is not None:
            self.stub.Start(StartRequest(pid=pid, period=period_ms))
        else:
            self.stub.Start(StartRequest(pid=pid))

    def stop(self):
        self.stub.Stop(StopRequest())

    def read(self):
        # TODO: re-implement this as streaming?
        return self.stub.Read(ReadRequest())
