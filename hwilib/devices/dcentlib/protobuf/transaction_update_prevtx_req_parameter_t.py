# Automatically generated by pb2py
# fmt: off
from .. import prototrez as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class transaction_update_prevtx_req_parameter_t(p.MessageType):

    def __init__(
        self,
        input_idx: int = None,
        prev_tx_blk_idx: int = None,
        prev_tx_blk: bytes = None,
    ) -> None:
        self.input_idx = input_idx
        self.prev_tx_blk_idx = prev_tx_blk_idx
        self.prev_tx_blk = prev_tx_blk

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('input_idx', p.UVarintType, 0),  # required
            2: ('prev_tx_blk_idx', p.UVarintType, 0),  # required
            3: ('prev_tx_blk', p.BytesType, 0),  # required
        }