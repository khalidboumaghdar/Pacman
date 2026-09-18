from typing import Any


class Ghost:
    def __init__(self, pinkyEntity: Any, blinkyEntity: Any, inkyEntity: Any, clydeEntity: Any) -> None:
        self.pinkyEntity = pinkyEntity
        self.blinkyEntity = blinkyEntity
        self.inkyEntity = inkyEntity
        self.clydeEntity = clydeEntity
        self.pinkyCurrentX = self.pinkyEntity.entityOriginalX
        self.pinkyCurrentY = self.pinkyEntity.entityOriginalY
        self.blinkyCurrentX = self.blinkyEntity.entityOriginalX
        self.blinkyCurrentY = self.blinkyEntity.entityOriginalY
        self.inkyCurrentX = self.inkyEntity.entityOriginalX
        self.inkyCurrentY = self.inkyEntity.entityOriginalY
        self.clydeCurrentX = self.clydeEntity.entityOriginalX
        self.clydeCurrentY = self.clydeEntity.entityOriginalY
