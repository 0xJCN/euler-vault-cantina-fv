// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;

import {ESynth} from "../../../src/Synths/ESynth.sol";
import {IEVC} from "ethereum-vault-connector/utils/EVCUtil.sol";

contract ESynthHarness is ESynth {
    constructor(IEVC evc_, string memory name_, string memory symbol_) ESynth(evc_, name_, symbol_) {}

    function getReentrancyGuardExt() external view returns (bool) {
        return _reentrancyGuardEntered();
    }
}
