from enum import IntFlag
from typing import Optional, cast
from multiformats import multibase, multicodec
from msgpack import packb, unpackb


class Bundle:
    class Options(IntFlag):
        NONE = 0x00
        REPLACE_TERMS = 0x01
        INDEX = 0x02
        FLATTEN_KEYS = 0x04

    def __init__(
        self,
        version: int,
        options: Options = Options.NONE,
        document: Optional[dict] = None,
        index: Optional[dict] = None,
    ):
        self.version = version
        self.options = options
        self._document = document
        self.index = index

    @property
    def replace_terms(self) -> bool:
        return bool(self.options & Bundle.Options.REPLACE_TERMS)

    @replace_terms.setter
    def replace_terms(self, value: bool):
        if value:
            self.options |= Bundle.Options.REPLACE_TERMS
        else:
            self.options &= ~Bundle.Options.REPLACE_TERMS

    @property
    def use_index(self) -> bool:
        return bool(self.options & Bundle.Options.INDEX)

    @use_index.setter
    def use_index(self, value: bool):
        if value:
            self.options |= Bundle.Options.INDEX
        else:
            self.options &= ~Bundle.Options.INDEX

    @property
    def flatten_keys(self) -> bool:
        return bool(self.options & Bundle.Options.FLATTEN_KEYS)

    @flatten_keys.setter
    def flatten_keys(self, value: bool):
        if value:
            self.options |= Bundle.Options.FLATTEN_KEYS
        else:
            self.options &= ~Bundle.Options.FLATTEN_KEYS

    @property
    def document(self) -> dict:
        if self._document is None:
            raise ValueError("Document is required")
        return self._document

    @document.setter
    def document(self, value: dict):
        self._document = value

    def serialize(self) -> str:
        if self.document is None:
            raise ValueError("Document is required")

        bundle = [self.version, self.options.value, self.document]
        if self.index is not None:
            bundle.append(self.index)

        bundle_bytes = packb(bundle)
        wrapped = multicodec.wrap("messagepack", cast(bytes, bundle_bytes))
        encoded = multibase.encode(wrapped, "base58btc")
        return encoded

    @classmethod
    def deserialize(cls, encoded: str) -> "Bundle":
        wrapped = multibase.decode(encoded)
        codec, bundle_bytes = multicodec.unwrap(wrapped)

        if codec.name != "messagepack":
            raise ValueError(f"Invalid codec: {codec}")

        bundle = unpackb(bundle_bytes, strict_map_key=False)
        if len(bundle) > 3:
            version, options, doc, index = bundle
        else:
            version, options, doc = bundle
            index = None
        return cls(version, options, doc, index)
