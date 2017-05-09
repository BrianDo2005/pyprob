# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class Poisson(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPoisson(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Poisson()
        x.Init(buf, n + offset)
        return x

    # Poisson
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Poisson
    def PriorLambda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Poisson
    def ProposalLambda(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def PoissonStart(builder): builder.StartObject(2)
def PoissonAddPriorLambda(builder, priorLambda): builder.PrependFloat64Slot(0, priorLambda, 0.0)
def PoissonAddProposalLambda(builder, proposalLambda): builder.PrependFloat64Slot(1, proposalLambda, 0.0)
def PoissonEnd(builder): return builder.EndObject()