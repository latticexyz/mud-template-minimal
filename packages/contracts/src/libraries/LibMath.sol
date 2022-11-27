// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;
import { Uint256Component } from "std-contracts/components/Uint256Component.sol";

library LibMath {
  function increment(Uint256Component component, uint256 entity) internal {
    uint256 current = component.has(entity) ? component.getValue(entity) : 0;
    component.set(entity, current + 1);
  }
}
