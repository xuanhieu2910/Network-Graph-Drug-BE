from typing import Optional

from pydantic import BaseModel

class ProteinSequence(BaseModel):
    link_record_from: Optional[str] = None
    sequence_value: Optional[str] = None
    sequence_length: Optional[str] = None
    sequence_crc64: Optional[str] = None
    sequence_md5: Optional[str] = None