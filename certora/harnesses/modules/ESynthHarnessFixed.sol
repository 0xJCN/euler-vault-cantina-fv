// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;

import {ESynthFixed} from "../../../src/Synths/ESynthFixed.sol";
import {IEVC} from "ethereum-vault-connector/utils/EVCUtil.sol";

contract ESynthHarnessFixed is ESynthFixed {
    constructor(IEVC evc_, string memory name_, string memory symbol_) ESynthFixed(evc_, name_, symbol_) {}

    function getReentrancyGuardExt() external view returns (bool) {
        return _reentrancyGuardEntered();
    }
}
